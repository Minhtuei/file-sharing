from threading import Thread
import struct

class ClientSender:
    def __init__(self, client):
        self.client = client
    def send_message(self, message):
        # Calculate the length of the message
        print (f"Sending message: {message}")
        length = len(message)
        # Pack the length as a 4-byte integer (assuming messages are less than 4 GB)
        packed_length = struct.pack("!I", length)
        # Send the packed length
        self.client.sendall(packed_length)
        # Send the actual message
        self.client.sendall(message.encode())

    def stop(self):
        # Add any cleanup or additional shutdown logic here
        self.send_message("exit")
    def login(self,username,password ,ipAddr, peerPort):
        msg = f"login {username} {password} {ipAddr} {peerPort}"
        self.send_message(msg)

    def register(self,username,password ,ipAddr, peerPort):
        msg = f"register {username} {password} {ipAddr} {peerPort}"
        print(msg)
        self.send_message(msg)

    def publish(self, new_file):
        new_file_data = new_file.get_file_info
        msg = f"publish {new_file_data[0]} {new_file_data[1]} {new_file_data[2]} {new_file_data[3]}"
        self.send_message(msg)
    def fetch(self, file_name):
        msg = f"fetch {file_name}"
        self.send_message(msg)