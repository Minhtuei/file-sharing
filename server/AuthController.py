from Database import Database
from StatusCode import StatusCode
from threading import Thread
class AuthController():
    def  __init__(self):
        self.database = Database()
        self.response_code = StatusCode()
        self.user = None

    def login(self, hostname, password, ipAddress, peerPort):
        print(f"Login request: {hostname} {password} {ipAddress} {peerPort}")
        self.user = self.database.get_user(hostname)
        print(self.user)
        if (not self.user):
            return self.response_code.USER_NOT_FOUND()
        elif (self.user[2] != password):
            return self.response_code.WRONG_PASSWORD()
        elif (self.user[5] == 1):
            return self.response_code.USER_ALREADY_ONLINE()
        else:
            self.database.update_user(hostname, ipAddress, peerPort)
            return self.response_code.LOGIN_SUCCESS()

    def register(self, hostname, password, ipAddress, peerPort):
        print(f"Register request: {hostname} {password} {ipAddress} {peerPort}")
        if (self.database.get_user(hostname) != None):
            return self.response_code.USER_ALREADY_EXISTS()
        else:
            self.database.add_user(hostname, password, ipAddress, peerPort)
            self.user = self.database.get_user(hostname)
            return self.response_code.REGISTER_SUCCESS()
    def publish(self,file):
        if self.user:
            print(file)
            self.database.insert_file(self.user[0],file[0],file[1],file[2],file[3].replace("_"," "))
            return self.response_code.UPLOAD_SUCCESS()
        else:
            return self.response_code.BAD_REQUEST()         
    def fetch(self,file_name):
        data= self.database.fetch(file_name)
        print(data)
        if len(data) == 0:
            return self.response_code.FILE_NOT_FOUND(),None
        else:
            return self.response_code.FETCH_SUCCESS(),data                             
    def get_files(self,owner_id):
        file = self.database.get_files(owner_id)
        return file
    def get_user(self,hostname):
        return self.database.get_user(hostname)
    def setStatus(self,status):
        self.database.update_status(self.user[1],status)
    def close(self):
        self.database.close()
        