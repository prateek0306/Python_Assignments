from file_handler import read_data, write_data
from exceptions import UserNotFoundException

def authenticate_user():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user_data = read_data("users.txt")

    for user in user_data:
        saved_username, saved_password = user.split(",")
        if username == saved_username and password == saved_password:
            print("Authentication successful!")
            return

    raise UserNotFoundException("Invalid username or password.")

def register_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    user_data = f"{username},{password}"

    write_data("users.txt", user_data)

    print("User registered successfully!")
