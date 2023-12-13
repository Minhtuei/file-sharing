import ast
import os
import struct
from threading import Thread
from time import sleep
from datetime import datetime
from Modules.ClientSender import ClientSender
from Modules.Database import Database
from Modules.StatusCode import StatusCode


class Listener:
    def __init__(self, client):
        self.client = client
        self.thread = None
        self.success = False
        self.statusCode = StatusCode()
        self.running = True
        self.notifications = []
    def start(self):
        pass
    def stop(self):
        # Add any cleanup or additional shutdown logic here
        self.running = False
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
    def get_notifications(self):
        return self.notifications
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
                    print(f"Received response code: {response_code}")
                    if response_code == self.statusCode.LOGIN_SUCCESS():
                        print("Login successful.")
                        self.success = True
                        self.notifications.append((datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), response_code ,"Login successful."))
                    elif response_code == self.statusCode.REGISTER_SUCCESS():
                        print("Registration successful.")
                        self.notifications.append((datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), response_code ,"Registration successful."))
                    elif response_code == self.statusCode.USER_NOT_FOUND():
                        print("User not found.")
                        self.notifications.append((datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), response_code ,"User not found."))
                    elif response_code == self.statusCode.WRONG_PASSWORD():
                        print("Wrong password.")
                        self.notifications.append((datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), response_code ,"Wrong password."))
                    elif response_code == self.statusCode.USER_ALREADY_ONLINE():
                        print("User already online.")
                        self.notifications.append((datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), response_code ,"User already online."))
                    elif response_code == self.statusCode.USER_ALREADY_EXISTS():
                        print("User already exists.")
                        self.notifications.append((datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), response_code ,"User already exists."))
                    elif response_code == self.statusCode.UPLOAD_SUCCESS():
                        print("File uploaded successfully.")
                        self.notifications.append((datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), response_code ,"File uploaded successfully."))
                    elif response_code == self.statusCode.PING():
                        data = self.receive_message(self.client)
                        self.notifications.append((datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), response_code ,"Server has just pinged you."))
                        message = f"ping {data}"
                        length = len(message)
                        packed_length = struct.pack("!I", length)
                        print (f"Sending message: {message}")
                        self.client.sendall(packed_length)
                        self.client.sendall(message.encode())
                        self.notifications.append((datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), self.statusCode.PING() ,"You have just replied to the server."))
                    elif response_code == self.statusCode.FETCH_SUCCESS():
                        self.local_respiratory = Database()
                        peers = self.receive_message(self.client)
                        peers = ast.literal_eval(peers)
                        print("List of peers that have the file:")
                        for peer in peers:
                            print(f"Hostname: {peer[0]}, IP Address: {peer[1]}, Port: {peer[2]}, Online: {peer[3]}")
                        selected_peer = None
                        print(self.fetch_peer)
                        while self.fetch_peer == None:
                            selected_peer = int(input("Enter the index of the peer you want to download from (-1 to quit): "))
                            if (selected_peer < -1 or selected_peer >= len(peers) or selected_peer == None):
                                print("Invalid index.")
                                continue
                            if (selected_peer == -1):
                                break
                            if (peers[selected_peer][3] == 0):
                                print("Peer is offline.")
                            elif (peers[selected_peer][3] == 1):
                                break
                        if (selected_peer == -1):
                            self.fetch_peer = 0
                        else:
                            self.fetch_peer = peers[selected_peer]
                        self.notifications.append((datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), response_code ,"You have just received the list of peers that have the file."))
                    elif response_code == self.statusCode.FILE_NOT_FOUND():
                        self.fetch_peer = 0
                        print("File not found.")
                        self.notifications.append((datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), response_code ,"File not found."))
                    elif response_code == self.statusCode.BAD_REQUEST():
                        print("Bad request.")
                        self.notifications.append((datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), response_code ,"Bad request."))
                    elif response_code == self.statusCode.STOP():
                        self.success = False
                        print("Server has stopped. Please use the stop command to exit.")
        except ConnectionAbortedError:
            print("Connection to the server was aborted.")
            self.stop()
        except OSError:
            print("Connection to the server was forcibly closed.")
            self.stop()
        except Exception as e:
            print(f"Exception in client listener: {e}")

    def isSuccessful(self):
        return self.success
class PeerListener(Listener):
    def __init__(self, client):
        super().__init__(client)
        self.local_repository_dir = None
        self.subRunning = True
    def set_local_repository(self, local_repository_dir):
        self.local_repository_dir = local_repository_dir
    def start(self):
        self.client.listen(1)
        while self.running:
            try:
                conn, addr = self.client.accept()
                self.thread = Thread(target=self.listen, args=(conn, addr), daemon=True)
                self.thread.start()
            except Exception as e:
                if not self.running:
                    break
                else:
                    print(f"Error in Peer Server:  {e}")
    def listen(self, conn, addr):
        try:
            while self.subRunning:
                data = self.receive_message(conn)
                if data:
                    command = data.split(" ")[0]
                    parameter = data.split(" ")[1:]
                    if command == "download":
                        file_name = parameter[0]
                        # read the file
                        file_path = os.path.join(self.local_repository_dir, file_name)
                        file_size = os.path.getsize(file_path)
                        conn.sendall(file_size.to_bytes(4, byteorder='big'))
                        sleep(1)
                        with open(file_path, "rb") as file:
                            while True:
                                data = file.read(4096)  # Use a larger buffer size for optimization
                                if not data:
                                    break
                                conn.send(data)
                        print("File sent.")
                        self.notifications.append((datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), self.statusCode.DOWNLOAD_SUCCESS() ,f'File "{file_name}" sent to {addr[0]}:{addr[1]}.'));
                        conn.close()

        except ConnectionAbortedError:
            print("Error in Peer Server: Connection to the server was aborted.")
        except OSError:
            print("Peer Connection for download was forcibly closed.")
        except Exception as e:
            print(f"Exception in peer listener: {e}")
        
        