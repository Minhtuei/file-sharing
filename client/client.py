import os
import shutil
import socket
import struct
from datetime import datetime
from threading import Thread
from time import sleep

from Modules.FileData import File
from Modules.ClientListener import ClientListener, PeerListener
from Modules.ClientSender import ClientSender
from Modules.Database import Database


class Client:
    def __init__(self):
        self.server_host = None
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

    def set_server_host(self, server_host):
        self.server_host = server_host
    def set_peerServer_host(self, peerServer_host):
        self.local_host = peerServer_host
    def set_server_port(self, server_port):
        self.local_port = server_port

    def start(self):
        server_host_ = input("Enter server host (auto for automatic): ")
        ip_address = input ("Enter your ip address (auto for automatic): ")
        local_port = input ("Enter your port (auto for automatic): ")
        try:
            if local_port != "auto" and not int(local_port) in range(0, 65536):
                print("Invalid port. Please try again.")
                return
        except ValueError:
            print("Invalid port. Please try again.")
            return
        if len(server_host_.split(".")) != 4 and server_host_ != "auto":
            print("Invalid ip address. Please try again.")
            return
        if len(ip_address.split(".")) != 4 and ip_address != "auto":
            print("Invalid ip address. Please try again.")
            return
        self.server_host = server_host_ if server_host_ != "auto" else socket.gethostbyname_ex(socket.gethostname())[2][-1]
        self.local_host = ip_address if ip_address != "auto" else socket.gethostbyname_ex(socket.gethostname())[2][-1]
        self.local_port = local_port if local_port != "auto" else 5001
        try:
            self.client.connect((self.server_host, self.server_port))
            print(self.client)
            self.listen_Server = Thread(target=self.client_listener.listen)
            self.listen_Server.start()
            print(f"Client connected to {self.server_host}:{self.server_port}")
            self.create_repository()
            self.create_file_system()
            self.login()
        except ConnectionRefusedError:
            print ("Server is not running. Please start the server first.")
            return
        except OSError:
            print ("Server is not running. Please start the server first.")
            return

    def stop(self):
        try:
            self.peer_listener.stop()
            self.client_listener.stop()
            sleep(1)
            print("Client stopped.")
        except Exception as e:
            self.client_listener.stop()
    def login(self):
        print("Please login or register to start using the system.")
        while not self.client_listener.isSuccessful():
            msg = input("Enter 'login' or 'register' to continue: ")
            if msg == "login":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                self.client_sender.login(username, password, self.local_host, self.local_port )
            elif msg == "register":
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                self.client_sender.register(username, password, self.local_host, self.local_port )
            else:
                print("Invalid command. Please try again.")
            sleep(1)
    
        self.local_server.bind((self.local_host, int(self.local_port)))
        self.listen_Peer = Thread(target=self.peer_listener.start)
        self.listen_Peer.start()
        self.peer_listener.set_local_repository(self.local_respiratory_dir)
        print(f"Peer Server listening on {self.local_host}:{self.local_port}")

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
                file = File(file[1], file[2], file[3], file[4].replace("_", " "))
                file.print_file()
    def notify(self):
        notifications = self.client_listener.get_notifications()
        if len(notifications) == 0:
            print("No notifications.")
        else:
            print("List of notifications:")
            for notification in notifications:
                print(f"{notification[0]}: {notification[2]}")
    def publish(self, local_file_name, file_name):
        try:
            file_path = os.path.join(self.local_file_system_dir, local_file_name)
            if not os.path.exists(file_path):
                print("File does not exist.")
            else:
                # Create the full destination path
                destination_path = os.path.join(self.local_respiratory_dir, file_name)
                if os.path.exists(destination_path):
                    print("File already exists in local repository.")
                    return
                # Move the file to the destination directory
                shutil.move(file_path, destination_path)
                # Update local_respiratory
                file_size = os.path.getsize(destination_path)
                file_date = datetime.now().strftime("%H:%M:%S-%d/%m/%Y")
                file_description = input("Enter file description: ").replace(" ", "_")      
                new_file = File(file_name, file_size,file_date, file_description)
                self.local_respiratory.add_file(new_file)
                self.client_sender.publish(new_file)
                sleep(1)
                self.client_listener.notifications[-1] = (datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), self.client_listener.statusCode.UPLOAD_SUCCESS() ,f'File "{file_name}" published.')
        except OSError as e:
            print("The server is not running. Please try again later.")
            self.stop()
    def fetch(self, file_name):
        try:
            self.client_sender.fetch(file_name)
            self.client_listener.notifications.append((datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), None ,f'Fetching file "{file_name}" from the server.'))
            while self.client_listener.get_fetch_peers() == None:
                sleep(1)
            selected_peer = self.client_listener.get_fetch_peers()
            if selected_peer == 0:
                return
            if selected_peer[1] == self.local_host and selected_peer[2] == self.local_port:
                print("You already have the file. So we will duplicate it for you.")
            self.peer_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.peer_client.connect((selected_peer[1], int(selected_peer[2])))
            mgs = f"download {file_name}"
            length = len(mgs)
            packed_length = struct.pack("!I", length)
            self.peer_client.sendall(packed_length)
            self.peer_client.sendall(mgs.encode())
            sleep(1)
            for file in self.local_respiratory.get_all_files():
                if file[1] == file_name:
                    file_name = file_name.split(".")
                    handle_file_name = file_name[0].split("(")
                    if len(handle_file_name) == 1:
                        file_name = f"{handle_file_name[0]}(1).{file_name[1]}"
                    else:
                        file_name = f"{handle_file_name[0]}({int(handle_file_name[1][:-1])+1}).{file_name[1]}"
            with open(os.path.join(self.local_respiratory_dir, file_name), "wb") as file:
                while True:
                    data = self.peer_client.recv(4096)
                    if b"EOF" in data:
                        data = data.replace(b"EOF", b"")
                        file.write(data)
                        break
                    file.write(data)
            print("File downloaded successfully.") 
            self.client_listener.notifications.append((datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), self.client_listener.statusCode.DOWNLOAD_SUCCESS() ,f'File "{file_name}" downloaded from {selected_peer[0]}/{selected_peer[1]}.'))
            file_size = os.path.getsize(os.path.join(self.local_respiratory_dir, file_name))
            file_date = datetime.now().strftime("%H:%M:%S-%d/%m/%Y")
            file_description = f"Downloaded from {selected_peer[0]}".replace(" ", "_")
            new_file = File(file_name, file_size,file_date, file_description)
            self.local_respiratory.add_file(new_file)
            self.client_sender.publish(new_file) 
            self.client_listener.fetch_peer = None
        except OSError as e:
            print("The server is not running. Please try again later.")
            self.stop()
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
                        > notify: list all notifications from the server
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
                case "notify":
                    self.notify();
                case "fetch":
                    if len(input_command) < 2:
                        print("Invalid command. Type 'help' for more information.")
                    else:
                        self.fetch(input_command[1]);
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
    client.controller()