from threading import Thread
from StatusCode import StatusCode
from ClientSender import ClientSender
import struct
from time import sleep
from Database import Database
import ast
import os
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
        self.fetch_peer = None
    def get_fetch_peers(self):
        return self.fetch_peer
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
                        peers = self.receive_message(self.client)
                        peers = ast.literal_eval(peers)
                        print("List of peers that have the file:")
                        for peer in peers:
                            print(f"Hostname: {peer[0]}, IP Address: {peer[1]}")
                        selected_peer = int(input("Enter the index of the peer you want to download from: "))
                        self.fetch_peer = peers[selected_peer]
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
        self.local_repository_dir = None
    def set_local_repository(self, local_repository_dir):
        self.local_repository_dir = local_repository_dir
    def start(self):
        self.client.listen(1)
        while self.running:
            try:
                conn, addr = self.client.accept()
                self.thread = Thread(target=self.listen, args=(conn, addr))
                self.thread.start()
            except Exception as e:
                if not self.running:
                    break
                else:
                    print(f"Exception in peer listener: {e}")
    def listen(self, conn, addr):
        try:
            while self.running:
                data = self.receive_message(conn)
                if data:
                    command = data.split(" ")[0]
                    parameter = data.split(" ")[1:]
                    if command == "download":
                        file_name = parameter[0]
                        # read the file
                        file_path = os.path.join(self.local_repository_dir, file_name)
                        with open(file_path, "rb") as file:
                            while True:
                                data = file.read(4096)  # Use a larger buffer size for optimization
                                if not data:
                                    break
                                conn.sendall(data)
                        conn.sendall(b"EOF")
                        print("File sent.")
                        conn.close()

        except ConnectionAbortedError:
            print("Connection to the server was aborted.")
        except OSError:
            print("Connection to the server was forcibly closed.")
        except Exception as e:
            print(f"Exception in client listener: {e}")
        finally:
            self.stop()
        