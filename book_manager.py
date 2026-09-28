from data import books
from data import save_books


def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    book = {
        "id": book_id,
        "name": book_name,
        "author": author,
        "status": "Available"
    }

    books.append(book)

    save_books(books)

    print("Book added successfully!")

def remove_book():
    book_id = input("Enter Book ID to remove: ")

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            print("Book removed successfully!")
            return

    print("Book not found.")
