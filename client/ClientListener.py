from threading import Thread
from StatusCode import StatusCode
from ClientSender import ClientSender
import struct
from time import sleep
from Database import Database
class Listener:
    def __init__(self, client):
        self.client = client
        self.thread = None
        self.success = False
        self.response_code = StatusCode()
        self.running = True
    def start(self):
        pass
    def stop(self):
        # Add any cleanup or additional shutdown logic here
        self.running = False
        sleep(1)
        self.client.close()
    def receive_message(self, conn):
        # Receive the packed length as a 4-byte integer
        packed_length = conn.recv(4)
        if not packed_length:
            return None  # Connection closed
        # Unpack the length
        length = struct.unpack("!I", packed_length)[0]
        # Receive the actual message
        message = conn.recv(length).decode('utf-8')
        print(f"Received message: {message}")
        return message
    def listen(self):
        pass
    def isSuccessful(self):
        pass
class ClientListener(Listener):
    def __init__(self, client):
        super().__init__(client)
    def start(self):
        self.thread = Thread(target=self.listen)
        self.thread.start()
    def listen(self):
        try:
            while self.running:
                response_code = self.client.recv(3).decode('utf-8')
                if response_code:  # Connection closed by the server
                    if response_code == self.response_code.OK():
                        print("Login successful.")
                        self.success = True
                    elif response_code == self.response_code.USER_NOT_FOUND():
                        print("User not found.")
                    elif response_code == self.response_code.WRONG_PASSWORD():
                        print("Wrong password.")
                    elif response_code == self.response_code.USER_ALREADY_EXISTS():
                        print("User already exists.")
                    elif response_code == self.response_code.UPLOAD_SUCCESS():
                        print("File uploaded successfully.")
                    elif response_code == self.response_code.PING():
                        data = self.receive_message(self.client)
                        message = f"ping {data}"
                        length = len(message)
                        packed_length = struct.pack("!I", length)
                        print (f"Sending message: {message}")
                        self.client.sendall(packed_length)
                        self.client.sendall(message.encode())
                    elif response_code == self.response_code.FETCH_SUCCESS():
                        self.local_respiratory = Database()
                        data = self.receive_message(self.client)
                        file_data = data.split(",")
                    elif response_code == self.response_code.FILE_NOT_FOUND():
                        print("File not found.")
                    elif response_code == self.response_code.STOP():
                        self.success = False
                        self.stop()
                    elif response_code == self.response_code.BAD_REQUEST():
                        print("Bad request.")
        except ConnectionAbortedError:
            print("Connection to the server was aborted.")
        except OSError:
            print("Connection to the server was forcibly closed.")
        except Exception as e:
            print(f"Exception in client listener: {e}")
        finally:
            self.stop()
    def isSuccessful(self):
        return self.success
class PeerListener(Listener):
    def __init__(self, client):
        super().__init__(client)
    def start(self):
        self.client.listen(1)
        while self.running:
            conn, addr = self.client.accept()
            self.thread = Thread(target=self.listen, args=(conn, addr))
            self.thread.start()
        
    def listen(self, conn, addr):
        try:
            while self.running:
                response_code = self.receive_message(conn)
                if response_code:
                    command = response_code.split(" ")[0]
                    parameter = response_code.split(" ")[1:]
                    if command == "download":
                        self.client.local_respiratory = Database()
                        file_data = self.client.local_respiratory.get_file(parameter[0])
                        # read the file
                        file_path = os.path.join(self.client.local_respiratory_dir, file_data[1])
                        file = open(file_path, "rb")
                        while True:
                            data = file.read(1024)
                            if not data:
                                break
                            conn.sendall(data)
                        file.close()
                        print("File sent.")

        except ConnectionAbortedError:
            print("Connection to the server was aborted.")
        except OSError:
            print("Connection to the server was forcibly closed.")
        except Exception as e:
            print(f"Exception in client listener: {e}")
        finally:
            self.stop()
        