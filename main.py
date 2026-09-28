from book_manager import add_book
from book_manager import remove_book
from display import display_books
from search import search_book
from transactions import issue_book
from transactions import return_book


while True:
    print("\n========================================")
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("========================================")

    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Remove Book")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_book()
        
    elif choice == "2":
        display_books()

    elif choice=="3":
        search_book()

    elif choice=="4":
        issue_book()

    elif choice=="5":
        return_book()

    elif choice==("6"):
        remove_book()
        
    elif choice == "7":
        print("Thank you for using the Library Management System!")
        break

    else:
        print("This option is not available yet.")
