from file_handler import read_data, write_data
from exceptions import BookNotFoundException

def borrow_book():
    book_title = input("Enter the title of the book to borrow: ")

    book_data = read_data("books.txt")

    found = False
    updated_data = []
    for book in book_data:
        title, author = book.split(",")
        if book_title.lower() in title.lower():
            updated_data.append(f"{title},{author},Borrowed")
            found = True
        else:
            updated_data.append(book)

    if found:
        write_data("books.txt", updated_data)
        print("Book borrowed successfully!")
    else:
        raise BookNotFoundException(f"Book with title '{book_title}' not found.")

def list_borrowed_books():
    book_data = read_data("books.txt")

    borrowed_books = [book for book in book_data if "Borrowed" in book]

    if borrowed_books:
        print("Borrowed Books:")
        for book in borrowed_books:
            title, author, _ = book.split(",")
            print(f"Title: {title}\nAuthor: {author}")
    else:
        print("No books are currently borrowed.")
