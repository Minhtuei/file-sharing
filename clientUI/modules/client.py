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
    def publish(self, local_file_name, file_name,file_path, file_description):
        try:
            if not os.path.exists(file_path):
                print("File does not exist.")
            else:
                # Create the full destination path
                destination_path = os.path.join(self.local_respiratory_dir, file_name)
                if os.path.exists(destination_path):
                    print("File already exists in local repository. Please use ")
                    return
                # Move the file to the destination directory
                shutil.move(file_path, destination_path)
                # Update local_respiratory
                file_size = os.path.getsize(destination_path)
                file_date = datetime.now().strftime("%H:%M:%S-%d/%m/%Y")
                new_file = File(file_name, file_size,file_date, file_description)
                self.local_respiratory.add_file(new_file)
                self.client_sender.publish(new_file)
        except OSError as e:
            print("The server is not running. Please try again later.")
            self.stop()
    def fetch(self, file_name):
        self.client_sender.fetch(file_name)
        self.client_listener.notifications.append((datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), None ,f'Fetching file "{file_name}" from the server.'))
        while self.client_listener.get_fetch_peers() == None:
            sleep(1)
        return self.client_listener.get_fetch_peers()
    def download(self, selected_host, file_name):
        try:
            self.peer_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.peer_client.connect((selected_host[1], int(selected_host[2])))
            mgs = f"download {file_name}"
            length = len(mgs)
            packed_length = struct.pack("!I", length)
            self.peer_client.sendall(packed_length)
            self.peer_client.sendall(mgs.encode())
            sleep(1)
            duplicate_files = self.local_respiratory.count_duplicate_files(file_name)
            if duplicate_files > 0:
                file_name = file_name.split(".")
                file_name = f"{file_name[0]}({duplicate_files}).{file_name[1]}"
            with open(os.path.join(self.local_respiratory_dir, file_name), "wb") as file:
                while True:
                    data = self.peer_client.recv(4096)
                    if b"EOF" in data:
                        data = data.replace(b"EOF", b"")
                        file.write(data)
                        break
                    file.write(data)
            
            self.client_listener.notifications.append((datetime.now().strftime("%H:%M:%S-%d/%m/%Y"), self.client_listener.statusCode.DOWNLOAD_SUCCESS() ,f'File "{file_name}" downloaded from {selected_host[0]}/{selected_host[1]}.'))
            file_size = os.path.getsize(os.path.join(self.local_respiratory_dir, file_name))
            file_date = datetime.now().strftime("%H:%M:%S-%d/%m/%Y")
            file_description = f"Downloaded from {selected_host[0]}".replace(" ", "_")
            new_file = File(file_name, file_size,file_date, file_description)
            self.local_respiratory.add_file(new_file)
            self.client_sender.publish(new_file) 

        except Exception as e:
            print(f"Exception in download: {e}")