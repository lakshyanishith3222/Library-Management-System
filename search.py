from data import books


def search_book():
    search = input("Enter Book ID or Book Name: ")

    for book in books:
        if book["id"] == search or book["name"].lower() == search.lower():
            print("\n========== BOOK FOUND ==========")
            print("Book ID:", book["id"])
            print("Book Name:", book["name"])
            print("Author:", book["author"])
            print("Status:", book["status"])
            return

    print("\nBook not found.")
