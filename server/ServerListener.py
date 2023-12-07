from threading import Thread
from AuthController import AuthController
from StatusCode import StatusCode
import struct
from time import sleep
class ServerListener:
    def __init__(self, server):
        self.server = server
        self.thread = None
        self.running = True
        self.status = StatusCode()
        self.clients = []
        self.ping_data = None
    def start(self):
        self.server.listen(1)
        print(f"Server listening on {self.server.getsockname()}")
        while self.running:
            sleep(1)
            try:
                conn, addr = self.server.accept()
                print(f"Connection from {addr}")
                self.thread = Thread(target=self.listen, args=(conn, addr,))
                self.thread.start()
            except Exception as e:
                if not self.running:
                    break
                print(f"Exception in server listener start: {e}")
    def get_clients(self):
        return self.clients
    def get_ping_data(self):
        return self.ping_data
    def stop(self):
        self.running = False
        for client in self.clients:
            client[0].sendall(self.status.STOP().encode('utf-8'))
            client[0].close()
        # Add any cleanup or additional shutdown logic here

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

    def listen(self, conn, addr):
        self.clients.append((conn,addr))
        auth = AuthController()
        try:
            while self.running:
                data = self.receive_message(conn)
                if data is None:
                    break  # Connection closed
                if data:
                    command = data.split()[0]
                    parameters = data.split()[1:]
                    if command == "login":
                        username = parameters[0]
                        password = parameters[1]
                        ipAddress = parameters[2]
                        peerPort = parameters[3]
                        try:
                            response = auth.login(username, password, ipAddress, peerPort)
                            conn.sendall(response.encode())
                        except Exception as e:
                            print(e)
                    elif command == "register":
                        username = parameters[0]
                        password = parameters[1]
                        ipAddress = parameters[2]
                        peerPort = parameters[3]
                        try:
                            response = auth.register(username, password, ipAddress, peerPort)
                            conn.sendall(response.encode())
                        except Exception as e:
                            print(e)
                    elif command == "publish":
                        try:
                            file = parameters
                            conn.sendall(auth.publish(file).encode())
                        except Exception as e:
                            print(e)
                    elif command == "ping":
                        self.ping_data = parameters[0]
                    elif command == "fetch":
                        try:
                            file_name = parameters[0]
                            response = auth.fetch(file_name)
                            conn.sendall(response[0].encode())
                            if response[0] == self.status.FETCH_SUCCESS():
                                message = str(response[1])
                                length = len(message)
                                packed_length = struct.pack("!I", length)
                                conn.sendall(packed_length)
                                conn.sendall(message.encode())
                        except Exception as e:
                            print(e)
                    elif command == "exit":
                        print(f"Connection closed: {addr}")
                        self.clients.remove((conn,addr))
                        auth.setStatus(0)
                        conn.close()
                        break
        except OSError:
            print(f"Connection closed: {addr}")
        except Exception as e:
            print(f"Exception in server listener listen: {e}")
            auth.close() 
