from Py.library_management.books import add_book, search_book, delete_book
from Py.library_management.users import authenticate_user, register_user
from Py.library_management.borrow import borrow_book, list_borrowed_books
from Py.library_management.returnn import return_book
from Py.library_management.file_handler import read_data, write_data

def show_menu():
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Delete Book")
    print("4. Authenticate User")
    print("5. Register User")
    print("6. Borrow Book")
    print("7. List Borrowed Books")
    print("8. Return Book")
    print("0. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            search_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            authenticate_user()
        elif choice == '5':
            register_user()
        elif choice == '6':
            borrow_book()
        elif choice == '7':
            list_borrowed_books()
        elif choice == '8':
            return_book()
        elif choice == '0':
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
