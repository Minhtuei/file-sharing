import sqlite3
import os
# Define your connection parameters

class Database:
    def __init__(self):
        directory = os.path.dirname(__file__)
        self.conn = sqlite3.connect(os.path.join(directory, "database.db"))
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        # Create the 'users' table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hostname TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            ipAddress TEXT NOT NULL,
            peerPort INTEGER ,
            isOnline INTEGER NOT NULL
        )""")

        self.cursor.execute("""CREATE TABLE IF NOT EXISTS file (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            owner_id INTEGER NOT NULL,
            file_name TEXT NOT NULL ,
            file_size INTEGER NOT NULL,
            file_date TEXT NOT NULL,
            file_description TEXT,
            FOREIGN KEY(owner_id) REFERENCES users(id)
        )""")
        self.conn.commit()
    def update_user(self, hostname, ipAddress, peerPort):
        #update user's ip peerPort and isOnline base on hostname and ipAddress
        self.cursor.execute("UPDATE users SET peerPort=?, isOnline=1 WHERE hostname=? AND ipAddress=?", (peerPort, hostname, ipAddress))
        self.conn.commit()
    def add_user(self, hostname, password, ipAddress, peerPort):
        self.cursor.execute("INSERT INTO users VALUES (NULL, ?, ?, ?, ?, ?)", (hostname, password, ipAddress, peerPort, 1))
        self.conn.commit()
    def insert_file(self, owner_id, file_name, file_size, file_date, file_description):
        self.cursor.execute("INSERT INTO file VALUES (NULL, ?, ?, ?, ?, ?)", (owner_id, file_name, file_size, file_date, file_description))
        self.conn.commit()
    def get_user(self, hostname):
        self.cursor.execute("SELECT * FROM users WHERE hostname=?", (hostname,))
        return self.cursor.fetchone()
    def get_files(self, owner_id):
        self.cursor.execute("SELECT * FROM file WHERE owner_id=?", (owner_id,))
        return self.cursor.fetchall()
    def fetch(self, file_name):
        self.cursor.execute("SELECT hostname,ipAddress FROM users WHERE id IN (SELECT owner_id FROM file WHERE file_name=?)", (file_name,))
        return self.cursor.fetchall()
    def close(self):
        self.cursor.execute("UPDATE users SET isOnline=0")
        self.conn.close()
