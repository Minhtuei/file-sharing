import os
import shutil
import socket
from datetime import datetime
from threading import Thread
from time import sleep
import struct
import FileData as fd
from ClientListener import ClientListener, PeerListener
from ClientSender import ClientSender
from Database import Database


class Client:
    def __init__(self):
        self.server_host = '192.168.1.9'
        self.server_port = 5000
        self.local_host = None
        self.local_port = None
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.local_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.peer_listener = PeerListener(self.local_server)
        self.client_listener = ClientListener(self.client)
        self.client_sender = ClientSender(self.client)
        self.listen_Server = None
        self.listen_Peer = None
        self.local_respiratory = Database()
        self.controller()

    def start(self):
        try:
            self.client.connect((self.server_host, self.server_port))
            self.listen_Server = Thread(target=self.client_listener.start)
            self.listen_Server.start()
            print(f"Client connected to {self.server_host}:{self.server_port}")
            self.local_host = socket.gethostbyname_ex(socket.gethostname())[2][1]
            self.local_port = 5001
            print(f"Peer Server listening on {self.local_host}:{self.local_port}")
            self.local_server.bind((self.local_host, self.local_port))
            self.listen_Peer = Thread(target=self.peer_listener.start)
            self.listen_Peer.start()
            self.create_repository()
            self.create_file_system()
            self.peer_listener.set_local_repository(self.local_respiratory_dir)
        except ConnectionRefusedError:
            print ("Server is not running. Please start the server first.")
            return
        except OSError:
            print ("Server is not running. Please start the server first.")
            return
        print("Please login or register to start using the system.")
        while not self.client_listener.isSuccessful():
            msg = input("Enter 'login' or 'register' to continue: ")
            if msg == "login":
                self.client_sender.login()
            elif msg == "register":
                self.client_sender.register()
            else:
                print("Invalid command. Please try again.")
            sleep(1)
    def stop(self):
        self.client_sender.stop()
        # self.peer_listener.stop()
        self.client_listener.stop()
        print("Client stopped.")
    def create_repository(self):
        self.app_folder = os.path.dirname(os.path.abspath(__file__))
        self.local_respiratory_dir = os.path.join(
            self.app_folder, "local_respiratory")
        if not os.path.exists(self.local_respiratory_dir):
            os.mkdir(self.local_respiratory_dir)

    def create_file_system(self):
        self.app_folder = os.path.dirname(os.path.abspath(__file__))
        self.local_file_system_dir = os.path.join(
            self.app_folder, "local_file_system")
        if not os.path.exists(self.local_file_system_dir):
            os.mkdir(self.local_file_system_dir)
    def list_files(self):
        print("List of files in local repository:")
        local_repo = self.local_respiratory.get_all_files()
        if len(local_repo) == 0:
            print("No files in local repository.")
        else:
            for file in local_repo:
                file = fd.File(file[1], file[2], file[3], file[4].replace("_", " "))
                file.print_file()
    def publish(self, local_file_name, file_name):
        file_path = os.path.join(self.local_file_system_dir, local_file_name)
        if not os.path.exists(file_path):
            print("File does not exist.")
        else:
            # Create the full destination path
            destination_path = os.path.join(self.local_respiratory_dir, file_name)

            # Move the file to the destination directory
            shutil.move(file_path, destination_path)

            # Update local_respiratory
            file_size = os.path.getsize(destination_path)
            file_date = datetime.now().strftime("%H:%M:%S-%d/%m/%Y")
            file_description = input("Enter file description: ").replace(" ", "_")      
            new_file = fd.File(file_name, file_size,file_date, file_description)
            self.local_respiratory.add_file(new_file)
            self.client_sender.publish(new_file)
            
    def controller(self):
        while True:
            input_command = input("Enter a command: ").split()
            if len(input_command) == 0:
                print("Invalid command. Type 'help' for more information.")
                continue
            match input_command[0]:
                case "help":
                    print("""
                        Command format: command "parameter1" "parameter2" ...
                        List of command:
                        > start: start the client
                        > stop: stop the client
                        > list: list all files in the local repository
                        > publish "lname" "fname": a local file (which is stored in the client's file system at "lname") is added to the 
                            client's repository as a file named "fname" and this information is conveyed to the server
                        > describe "fname" "description": add a description to the file "fname" in the local repository
                        > fetch "file name": fetch some copy of the target file and add it to the local repository
                        > download "index": download the file with the index <index> return from the fetch command to local repository on your computer""");
                case "start":
                    self.start();
                case "stop":
                    self.stop();
                    break;
                case "list":
                    self.list_files();
                case "fetch":
                    if len(input_command) < 2:
                        print("Invalid command. Type 'help' for more information.")
                    else:
                        self.client_sender.fetch(input_command[1])
                        while self.client_listener.get_fetch_peers() == None:
                            sleep(1)
                        selected_peer = self.client_listener.get_fetch_peers()
                        self.peer_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        self.peer_client.connect((selected_peer[1], 5002))
                        mgs = f"download {input_command[1]}"
                        length = len(mgs)
                        packed_length = struct.pack("!I", length)
                        self.peer_client.sendall(packed_length)
                        self.peer_client.sendall(mgs.encode())
                        file = open(os.path.join(self.local_respiratory_dir, input_command[1]), "wb")
                        while True:
                            current_pos = file.tell()
                            data = self.peer_client.recv(1024)
                            if data.decode() == "EOF":
                                break
                            file.write(data)
                            file.seek(current_pos + len(data))
                            
                        file.close()
                        print("File downloaded successfully.") 
                        self.peer_client.close()             
                case "publish":
                    if len(input_command) < 3:
                        print("Invalid command. Type 'help' for more information.")
                    else:
                        self.publish(input_command[1], input_command[2]);
                case default:
                    print("Invalid command. Type 'help' for more information.")
            sleep(1)
if __name__ == "__main__":
    client = Client()
