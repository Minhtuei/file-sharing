from AuthController import AuthController
from StatusCode import StatusCode
import struct
import secrets
from FileData import File
class ServerSender:
    def __init__(self, server):
        self.server = server
        self.auth = None
        self.ping_data = None
    def send_message(self,conn ,message):
        # Calculate the length of the message
        length = len(message)
        # Pack the length as a 4-byte integer (assuming messages are less than 4 GB)
        packed_length = struct.pack("!I", length)
        # Send the packed length
        conn.sendall(packed_length)
        # Send the actual message
        conn.sendall(message.encode())
    def ping (self, hostname, clients):
        self.auth = AuthController()
        self.ping_data = None
        try:
            user = self.auth.get_user(hostname)
            if user:
                for client in clients:
                    if client[1][0] == user[3]:
                        client[0].sendall(StatusCode().PING().encode('utf-8'))
                        self.ping_data = secrets.token_hex(16)
                        self.send_message(client[0], self.ping_data)
                        return self.ping_data
            return None
        except Exception as e:
            print(e)
    def discover(self,hostname,clients):
        self.auth = AuthController()
        try:
            user = self.auth.get_user(hostname)
            if user:
                repo = self.auth.get_files(user[0])
                if len(repo) == 0:
                    print("This hostname's repo is empty")
                else:
                    print("This hostname's repository:")
                    for file in repo:
                        file_data = File(file[2],file[3],file[4],file[5])
                        file_data.print_file()
            else:
                print("User not found")
        except Exception as e:
            print(e)
    def stop(self,clients):
        for client in clients:
            client[0].sendall(StatusCode().STOP().encode('utf-8'))