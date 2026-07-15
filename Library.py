import string
import random
import numpy
# list
# todolist
# 1.Make a menu
# 2.List of books
# 3.add a book
# 4.borrow book
# 5.return book
# 6.status of library
# 7.users
# 8.admin

class book:
    def __init__(self, book_id, name, author):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.is_available = True
    
    def list_of_books(self):
        books = []
        append_book = {
            "book_id": self.book_id,
            "name": self.name,
            "author": self.author,
            "is_available": self.is_available
        }
        books.append(append_book)
        return books
    
class patron:
    def __init__(self, patron_id, name):
        self.patron_id = patron_id
        self.name = name
        self.borrowed_books = []
    
    def borrow_book(self, book):
        if book.is_available:
            book.is_available = False
            self.borrowed_books.append(book)
            return True
        else:
            return False
    
    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_available = True
            self.borrowed_books.remove(book)
            return True
        else:
            return False

class library:
    def __init__(self):
        self.books = []
        self.patrons = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def add_patron(self, patron):
        self.patrons.append(patron)
    
    def list_books(self):
        return [book.list_of_books() for book in self.books]
    
    def list_patrons(self):
        return [{"patron_id": patron.patron_id, "name": patron.name, "borrowed_books": [book.name for book in patron.borrowed_books]} for patron in self.patrons]
    
library_instance = library()


while True:
    print("Welcome to the Library Management System")
    print("1. Add a book")
    print("2. List all books")
    print("3. Add a patron")
    print("4. List all patrons")
    print("5. Borrow a book")
    print("6. Return a book")
    print("7. Exit")
    input_choice = input("Enter your choice:")
    if input_choice == "1":
        book_id = input("Enter book ID: ")
        name = input("Enter book name: ")
        author = input("Enter book author: ")
        new_book = book(book_id, name, author)
        library_instance.add_book(new_book)
        print(f"Book '{name}' added successfully.")
    elif input_choice == "2":
        books = library_instance.list_books()
        for book in books:
            print(book)
    elif input_choice == "3":
        patron_id = input("Enter patron ID: ")
        name = input("Enter patron name: ")
        new_patron = patron(patron_id, name)
        library_instance.add_patron(new_patron)
        print(f"Patron '{name}' added successfully.")
    elif input_choice == "4":
        patrons = library_instance.list_patrons()
        for patron in patrons:
            print(patron)
    elif input_choice == "5":
        patron_id = input("Enter patron ID: ")
        book_id = input("Enter book ID:")
        patron = next((p for p in library_instance.patrons if p.patron_id == patron_id), None)
        book = next((b for b in library_instance.books if b.book_id == book_id), None)
        if patron and book:
            if patron.borrow_book(book):
                print(f"Book '{book.name}' borrowed successfully.")
            else:
                print(f"Book '{book.name}' is not available.")
        else:
            print("Patron or book not found.")
    elif input_choice == "6":
        patron_id = input("Enter patron ID: ")
        book_id = input("Enter book ID:")
        patron = next((p for p in library_instance.patrons if p.patron_id == patron_id), None)
        book = next((b for b in library_instance.books if b.book_id == book_id), None)
        if patron and book:
            if patron.return_book(book):
                print(f"Book '{book.name}' returned successfully.")
            else:
                print(f"Book '{book.name}' was not borrowed by this patron.")
        else:
            print("Patron or book not found.")
    elif input_choice == "7":
        print("Exiting the Library Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
        
