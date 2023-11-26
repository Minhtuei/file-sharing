from datetime import datetime
class File():
    def __init__(self, file_name, file_size, file_date, file_description):
        self.file_name = file_name
        self.file_size = file_size
        self.file_date = file_date
        self.file_description = file_description

    def __str__(self):
        return f"{self.file_name},{self.file_size},{self.file_date},{self.file_description}"

    @property
    def get_file_name(self):
        return self.file_name

    @property
    def get_file_size(self):
        return self.file_size

    @property
    def get_file_date(self):
        return self.file_date

    @property
    def get_file_description(self):
        return self.file_description

    @property
    def get_file_info(self):
        return (self.file_name, self.file_size, self.file_date, self.file_description)

    @property
    def format_size(self):
        # convert file size from bytes to KB, MB, GB, TB
        size_in_bytes = int(self.file_size)
        if size_in_bytes < 1024:
            return f"{size_in_bytes}B"
        elif size_in_bytes < pow(1024, 2):
            return f"{round(size_in_bytes/1024, 2)}KB"
        elif size_in_bytes < pow(1024, 3):
            return f"{round(size_in_bytes/pow(1024, 2), 2)}MB"
        elif size_in_bytes < pow(1024, 4):
            return f"{round(size_in_bytes/pow(1024, 3), 2)}GB"

    def print_file(self):
        print(f"File name: {self.file_name}")
        print(f"File size: {self.format_size}")
        print(f"File date: {self.file_date}")
        print(f"File description: {self.file_description}")
        print("-"*50)