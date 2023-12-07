
class File():
    def __init__(self, file_name, file_size,file_date, file_description):
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
        if self.file_size < 1024:
            return self.file_size.__str__()+"B"
        elif self.file_size < pow(1024, 2):
            return round(self.file_size/1024, 2).__str__()+"KB"
        elif self.file_size < pow(1024, 3):
            return round(self.file_size/pow(1024, 2), 2).__str__()+"MB"
        elif self.file_size < pow(1024, 4):
            return round(self.file_size/pow(1024, 3), 2).__str__()+"GB"
    def print_file(self):
        print(f"File name: {self.file_name}")
        print(f"File size: {self.format_size}")
        print(f"File date: {self.file_date}")
        print(f"File description: {self.file_description}")
        print("-"*50)