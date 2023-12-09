import os
import shutil
import socket
import struct
from datetime import datetime
from threading import Thread
from time import sleep

from . FileData import File
from . ClientListener import ClientListener, PeerListener
from . ClientSender import ClientSender
from . Database import Database


class Client:
    def __init__(self):
        self.server_host = socket.gethostbyname_ex(socket.gethostname())[2][-1]
        self.server_port = 5000
        self.local_host = socket.gethostbyname_ex(socket.gethostname())[2][-1]
        self.local_port = 5001
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
        try:
            self.client.connect((self.server_host, self.server_port))
            self.listen_Server = Thread(target=self.client_listener.start)
            self.listen_Server.start()
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

    def stop(self):
        try:
            self.client_sender.stop()
            self.peer_listener.stop()
            self.client_listener.stop()
            print("Client stopped.")
        except Exception as e:
            self.client_listener.stop()
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
        try:
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
        except OSError as e:
            print("The server is not running. Please try again later.")
            self.stop()
    def fetch(self, file_name):
        try:
            self.client_sender.fetch(file_name)
            while self.client_listener.get_fetch_peers() == None:
                sleep(1)
            selected_peer = self.client_listener.get_fetch_peers()
            self.peer_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.peer_client.connect((selected_peer[1], self.local_port+1))
            mgs = f"download {file_name}"
            length = len(mgs)
            packed_length = struct.pack("!I", length)
            self.peer_client.sendall(packed_length)
            self.peer_client.sendall(mgs.encode())
            with open(os.path.join(self.local_respiratory_dir, file_name), "wb") as file:
                while True:
                    data = self.peer_client.recv(4096)
                    if b"EOF" in data:
                        data = data.replace(b"EOF", b"")
                        file.write(data)
                        break
                    file.write(data)
            print("File downloaded successfully.") 
            self.peer_client.close()
            file_size = os.path.getsize(os.path.join(self.local_respiratory_dir, file_name))
            file_date = datetime.now().strftime("%H:%M:%S-%d/%m/%Y")
            file_description = f"Downloaded from {selected_peer[0]}".replace(" ", "_")
            new_file = fd.File(file_name, file_size,file_date, file_description)
            self.local_respiratory.add_file(new_file)
            self.client_sender.publish(new_file) 
        except OSError as e:
            print("The server is not running. Please try again later.")
            self.stop()