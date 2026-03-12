import sqlite3
import os
from validation import validate_book, validate_user


class Library:

    def __init__(self, booklist, name, database_path="LibraryDataset.txt", db_file="borrowed_books.db"):

        self.bookList = booklist
        self.name = name
        self.database_path = database_path
        self.db_file = db_file

        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS borrowed_books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book TEXT UNIQUE,
            user TEXT
        )
        """)

        self.conn.commit()

    def displayBooks(self):
        return self.bookList

    def lendBook(self, book, user):

        validate_book(book)
        validate_user(user)

        if book not in self.bookList:
            return f"'{book}' is not in the library."

        self.cursor.execute("SELECT user FROM borrowed_books WHERE book=?", (book,))
        result = self.cursor.fetchone()

        if result:
            return f"'{book}' is already borrowed by {result[0]}"

        self.cursor.execute(
            "INSERT INTO borrowed_books (book, user) VALUES (?, ?)",
            (book, user)
        )

        self.conn.commit()

        return f"'{book}' has been borrowed by {user}."

    def addBook(self, book):

        validate_book(book)

        if book in self.bookList:
            return "Book already exists."

        self.bookList.append(book)

        with open(self.database_path, "a") as f:
            f.write(f"\n{book}")

        return "Book added successfully."

    def returnBook(self, book):

        validate_book(book)

        self.cursor.execute("SELECT * FROM borrowed_books WHERE book=?", (book,))
        result = self.cursor.fetchone()

        if not result:
            return "Book is not borrowed."

        self.cursor.execute("DELETE FROM borrowed_books WHERE book=?", (book,))
        self.conn.commit()

        return "Book returned successfully."

