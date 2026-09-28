from data import books
from data import save_books


def issue_book():
    book_id = input("Enter Book ID to issue: ")

    for book in books:
        if book["id"] == book_id:

            if book["status"] == "Available":
                book["status"] = "Issued"
                print("Book issued successfully!")
            else:
                print("Book is already issued.")

            return

    print("Book not found.")


def return_book():
    book_id = input("Enter Book ID to return: ")

    for book in books:
        if book["id"] == book_id:

            if book["status"] == "Issued":
                book["status"] = "Available"

                save_books(books)
                
                print("Book returned successfully!")
            else:
                print("Book is already available.")

            return

    print("Book not found.")
