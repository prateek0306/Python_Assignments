from file_handler import read_data, write_data
from exceptions import BookNotFoundException

def add_book():
    book_title = input("Enter the title of the book: ")
    book_author = input("Enter the author of the book: ")
    book_data = f"{book_title},{book_author}"

    write_data('books.txt',book_data)

    print("Book added successfully!")

def search_book():
    book_title = input("Enter the title of the book to search: ")

    book_data = read_data("books.txt")

    for book in book_data:
        title, author = book.split(",")
        if book_title.lower() in title.lower():
            print(f"Book Found!\nTitle: {title}\nAuthor: {author}")
            return

    raise BookNotFoundException(f"Book with title '{book_title}' not found.")

def delete_book():
    book_title = input("Enter the title of the book to delete: ")

    book_data = read_data("data/books.txt")

    found = False
    updated_data = []
    for book in book_data:
        title, author = book.split(",")
        if book_title.lower() not in title.lower():
            updated_data.append(book)
        else:
            found = True

    if found:
        write_data("books.txt", updated_data)
        print("Book deleted successfully!")
    else:
        raise BookNotFoundException(f"Book with title '{book_title}' not found.")
