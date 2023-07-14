class FileOperation:
    def __init__(self, file_name):
        self.file_name = file_name

    def write_file(self, data):
        with open(self.file_name, '+a') as file:
            file.write(data)

    def read_file(self):
        try:
            with open(self.file_name, '+r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            raise FileException(f"File '{self.file_name}' not found.")

class FileException(Exception):
    pass
