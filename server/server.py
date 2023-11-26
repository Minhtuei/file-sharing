import socket
from threading import Thread
from ServerListener import ServerListener
from ServerSender import ServerSender
import time
from time import sleep
class Server:
    def __init__(self):
        self.host = socket.gethostbyname_ex(socket.gethostname())[2][1]
        self.port = 5000
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Listener = ServerListener(self.server)
        self.Sender = ServerSender(self.server)
        self.listen_thread = Thread(target=self.Listener.start)
        self.controller = Thread(target=self.command)
        self.controller.start()
    def start(self):
        try:
            self.server.bind((self.host, self.port))
            print("Server started.")
            self.listen_thread.start()
        except WindowsError:
            print("Server is already running.")
        except Exception as e:
            print(f"Exception in server: {e}")
    def stop(self):
        try:
            self.Sender.stop(self.Listener.get_clients())
            self.Listener.stop()
            sleep(1)
            self.server.close()

            print("Server stopped.")
        except Exception as e:
            print(f"Exception in server: {e}")
    def ping(self, hostname):
        print(f"Pinging {hostname} with 32 bytes of data:")
        round_time_trips = []
        total_receive = 0
        for i in range(4):
            send_time = time.time()
            send_data = self.Sender.ping(hostname, self.Listener.get_clients())
            sleep(1)
            receive_data = self.Listener.get_ping_data()
            receive_time = time.time()
            round_time_trips.append((receive_time - send_time - 1) * 1000)
            if send_data == receive_data and receive_data != None:
                total_receive += 1
                print(f"Reply from {hostname}: time={round_time_trips[i]:.2f}ms")
            else:
                print(f"Request timed out.")
            sleep(1)
        print(f"Ping statistics for {hostname}:")
        print(f"Packets: Sent = 4, Received = {total_receive}, Lost = {4-total_receive} ({(1-total_receive/4)*100}% loss)")
           
        if total_receive == 4:
            print(f"Approximate round trip times in milli-seconds:")
            print(f"Minimum = {min(round_time_trips):.2f}ms, Maximum = {max(round_time_trips):.2f}ms, Average = {sum(round_time_trips)/len(round_time_trips):.2f}ms")
            print(f"Host {hostname} is online.")
        elif total_receive == 0:
            print(f"Host {hostname} is offline.")
        else:
            print(f"Host {hostname} is partially online.")
    def command(self):
        while True:
            input_command = input("Enter a command: ").split()
            match input_command[0]:
                case "help":
                    print("""
                        Command format: command "parameter1" "parameter2" ...
                        List of command:
                        > start: start the server
                        > stop: stop the server
                        > clear: clear the command-line output
                        > ping "hostname": check if the host with hostname is online
                        > discover "hostname": check the local files of host hostname""");
                case "start":
                    self.start();
                case "ping":
                    if len(input_command) == 2:
                        self.ping(input_command[1])
                    else:
                        print("Invalid Argument. Type 'help' for more information.")
                case "discover":
                    if len(input_command) == 2:
                        self.Sender.discover(input_command[1], self.Listener.get_clients())
                    else:
                        print("Invalid Argument. Type 'help' for more information.")
                case "stop":
                    self.stop();
                    break;
                case default:
                    print("Invalid command. Type 'help' for more information.")
            sleep(1)
if __name__ == "__main__":
    server = Server()