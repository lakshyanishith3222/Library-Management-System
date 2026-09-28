# Library Management System

## 1. Project Overview

The Library Management System is a Python-based project designed to manage books in a library.

The system allows the user to add, display, search, issue, return, and remove books. The project uses multiple Python files to keep the program organized and easy to understand.

Book information is stored permanently in a JSON file, so the data is not lost when the program is closed.

---

## 2. Objectives

The main objectives of this project are:

- To create a simple library management system using Python.
- To manage book records efficiently.
- To provide options for adding and removing books.
- To search for books using Book ID or Book Name.
- To manage book issue and return operations.
- To store book information permanently using JSON.
- To demonstrate the use of Python functions, lists, dictionaries, modules, and file handling.

---

## 3. Features

The system provides the following features:

### Add Book
Allows the user to add a new book by entering:
- Book ID
- Book Name
- Author Name

### Display All Books
Displays all books currently stored in the library.

### Search Book
Allows the user to search for a book using:
- Book ID
- Book Name

### Issue Book
Allows the user to issue an available book.

### Return Book
Allows the user to return an issued book.

### Remove Book
Allows the user to remove a book from the library using its Book ID.

### Permanent Storage
Book records are stored in `books.json` using JSON file handling.

---

## 4. Technologies Used

- Python
- JSON
- File Handling
- Functions
- Lists
- Dictionaries
- Modules

---

## 5. Project Structure

```text
Library_Management_System/
│
├── main.py
├── book_manager.py
├── search.py
├── transactions.py
├── display.py
├── data.py
│
└── data/
    └── books.json