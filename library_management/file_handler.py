def read_data(file_path):
    file=open(file_path, "r+") 
    data = file.read().splitlines()
    return data

def write_data(file_path, data):
    file=open(file_path, "a+") 
    file.write(data + "\n")
