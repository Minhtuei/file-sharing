import sqlite3
import os

class Database:
    def __init__(self):
        directory = os.path.dirname(__file__)
        self.conn = sqlite3.connect(os.path.join(directory, "database.db"))
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS repo (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            file_name TEXT NOT NULL UNIQUE,
            file_size INTEGER NOT NULL,
            file_date TEXT NOT NULL,
            file_description TEXT
        )""")
        self.conn.commit()
    def add_file(self, file):
        self.cursor.execute("INSERT INTO repo VALUES (NULL, ?, ?, ?, ?)", file.get_file_info)
        self.conn.commit()
    def get_all_files(self):
        self.cursor.execute("SELECT * FROM repo")
        return self.cursor.fetchall()
    def close(self):
        self.cursor.execute("UPDATE users SET isOnline=0")
        self.conn.close()
    def get_file(self, file_name):
        self.cursor.execute("SELECT * FROM repo WHERE file_name=?", (file_name,))
        return self.cursor.fetchone()
    def count_duplicate_files(self,file_name):
        self.cursor.execute("SELECT COUNT(*) FROM repo WHERE file_name=?", (file_name,))
        return self.cursor.fetchone()[0]