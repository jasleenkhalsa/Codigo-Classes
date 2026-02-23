# Library Management System

# BOOKS
class Books:
    def __init__(self, book_id, book_name, author_name):
        self.book_id = book_id
        self.book_name = book_name
        self.author_name = author_name

# BOOK UNITS
class BookUnit:
    def __init__(self, book_name, total_unit, available_unit):
        self.book_name = book_name
        self.total_unit = total_unit
        self.available_unit = available_unit