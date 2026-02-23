# Library Management System

# BOOKS
class Book:
    def __init__(self, book_id, book_name, author_name):
        self.book_id = book_id
        self.book_name = book_name
        self.author_name = author_name
    def display_info(self):
        print(self.book_id, self.book_name, self.author_name)    

# BOOK UNITS
class BookUnit:
    def __init__(self, book, total_unit, available_unit):
        self.book = book
        self.total_unit = total_unit
        self.available_unit = available_unit

# ISSUE TABLE
class IssueRecord:
    def __init__(self, user_id, book_id, issue_date, return_date):
        self.user_id = user_id
        self.book_id = book_id
        self.issue_date = issue_date
        self.return_date = return_date

# USER INFO
class User:
    def __init__(self, user_id, name, year, email, mobile, is_admin):
        self.user_id = user_id
        self.name = name
        self.year = year
        self.email = email
        self.mobile = mobile
        self.is_admin = is_admin

# HISTROY TABLE
class History:
    def __init__(self, user_id, book_name, issue_date, return_date):
        self.user_id = user_id
        self.book_name = book_name
        self.issue_date = issue_date
        self.return_date = return_date

# ADMIN 
class Admin(User):
    def __init__(self, user_id, name, year, email, mobile):
        super().__init__(user_id, name, year, email, mobile, True)

   

        