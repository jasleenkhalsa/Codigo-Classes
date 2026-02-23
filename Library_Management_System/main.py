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

    def display_info(self):
        print(f"ID: {self.user_id}, Name: {self.name}, Admin: {self.is_admin}")

# HISTORY TABLE
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

# Store Data

books = {}
users = {}
history_record = {}

# Functions

def add_book():
    num = int(input("Enter Number of Book entries you want to ADD :"))
    for i in range (num):
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        author_name = input("Enter Author Name: ")

        books[book_id] = Book(book_id, book_name, author_name)

        print("Book Added Successfully!\n")

def add_user():
    num = int(input("Enter Number of Users you want to ADD: "))

    for i in range(num):
        user_id = input("Enter User ID: ")
        name = input("Enter Name: ")
        year = input("Enter Year: ")
        email = input("Enter Email: ")
        mobile = input("Enter Mobile: ")

        is_admin = input("Is Admin (True/False): ").lower() == "true"

        users[user_id] = User(user_id, name, year, email, mobile, is_admin)

        print("User Added Successfully!\n")

def view_books():
    if not books:
        print("No Books Available.")
        return

    print("\n Book List ")
    for book in books.values():
        book.display_info()


def view_users():
    if not users:
        print("No Users Available.")
        return

    print("\n User List ")
    for user in users.values():
        user.display_info()

# Library    
while True:
    print("\n Library Menu ")
    print("1. Add Book")
    print("2. Add User")
    print("3. View Books")
    print("4. View Users")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        add_user()
    elif choice == "3":
        view_books()
    elif choice == "4":
        view_users()
    elif choice == "5":
        print("Exiting System...")
        break
    else:
        print("Invalid Choice!")

