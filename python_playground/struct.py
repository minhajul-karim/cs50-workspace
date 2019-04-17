from cs50 import get_string
from students import Book

# A list of all books
books = []

# Enter data for 3 books
for i in range(3):
    name = get_string("Name of book: ")
    author = get_string("Name of author: ")
    price = get_string("Price: ")

    # Declare a variable of class Book
    newBook = Book(name, author, price)
    books.append(newBook)

# Printing all info
for book in books:
    print(f"{book.nameOfbook} is written by {book.nameOfAuthor}, price = {book.priceOfBook}")