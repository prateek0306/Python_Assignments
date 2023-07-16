from file_handler import read_data, write_data
from exceptions import BookNotFoundException

def return_book():
    book_title = input("Enter the title of the book to return: ")

    book_data = read_data("books.txt")

    found = False
    updated_data = []
    for book in book_data:
        title, author, status = book.split(",")
        if book_title.lower() in title.lower() and status.strip().lower() == "borrowed":
            updated_data.append(f"{title},{author},Available")
            found = True
        else:
            updated_data.append(book)

    if found:
        write_data("books.txt", updated_data)
        print("Book returned successfully!")
    else:
        raise BookNotFoundException(f"Book with title '{book_title}' not found.")
