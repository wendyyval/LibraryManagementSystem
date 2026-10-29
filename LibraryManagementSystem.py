class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def __str__(self):
        return(f"Title: {self.title}, "
               f"Author: {self.author}, "
               f"ISBN: {self.isbn}, "
               f"Borrowed: {'Yes' if self.is_borrowed else 'No'}")


class Library:
    def __init__(self):
        self.books = []
        self.user = {}

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def list_books(self):
        if not self.books: # if list is empty
            print('No books in the library.')
        for book in self.books: # print books in library if populated
            print(book)

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have borrowed '{book.title}'.")
                return
        print('Book is not available. Or has been borrowed.')

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and book.is_borrowed:
                book.is_borrowed = False
                print(f"You have returned '{book.title}'.")
                return
        print('Book is not available. Or has not been borrowed.')

class Users:
    def __init__(self, user_id, email):
        self.user_id = user_id
        self.email = email

book1 = Book("Python Crash Course", "Eric Matthes", "9781718502703")
book2 = Book("Automate the Boring Stuff with Python", "Al Sweigart", "9781718503403")
book3 = Book("Effective Java", "Joshua Bloch", "9780134685991")
book4 = Book("The Pragmatic Programmer", "Andy Hunt and Dave Thomas", "9780201616224")
print(book1)

print()

library = Library() # instance of class library w/ no parameters bc constructor takes no parameters
library.list_books()

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

library.add_book(Book("Learn Java", "Jane Doe", "9876543210"))

print()

library.list_books()

print()

library.borrow_book("9781718502703")
library.borrow_book("9780134685991")
library.borrow_book("8493828477203")
library.borrow_book("9781718502703")

print(book3)
print()

library.return_book("9781718502703")
library.return_book("9780134685991")
library.return_book("8493828477203")
library.return_book("9781718502703")
print(book3)