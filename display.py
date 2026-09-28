from data import books


def display_books():
    if len(books) == 0:
        print("\nNo books available in the library.")
        return

    print("\n========== ALL BOOKS ==========")

    for book in books:
        print("Book ID:", book["id"])
        print("Book Name:", book["name"])
        print("Author:", book["author"])
        print("Status:", book["status"])
        print("------------------------------")
