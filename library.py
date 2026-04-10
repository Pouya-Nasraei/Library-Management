import sqlite3
from validation import validate_book, validate_user


class Library:

    def __init__(self, booklist, name, database_path="LibraryDataset.txt", db_file="borrowed_books.db"):

        self.bookList = booklist
        self.name = name
        self.database_path = database_path
        self.db_file = db_file

        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()
        
        self.book_lookup = {self._normalize(book): book for book in self.bookList}
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
        
    def _normalize(self, text):
        return text.strip().lower()

    def displayBooks(self):
        return self.bookList

    def lendBook(self, book, user):
        
        book = book.strip()
        user = user.strip()

        validate_book(book)
        validate_user(user)
        
        key = self._normalize(book)

        if key not in self.book_lookup:
            return f"Book '{book}' is not in the library."

        real_book = self.book_lookup[key]
        
        self.cursor.execute("SELECT user FROM borrowed_books WHERE LOWER(book)=?", (key,))
        result = self.cursor.fetchone()

        if result:
            return f"Book '{real_book}' is already borrowed by {result[0]}"

        self.cursor.execute(
            "INSERT INTO borrowed_books (book, user) VALUES (?, ?)",
            (real_book, user)
        )

        self.conn.commit()

        return f"Book '{real_book}' has been borrowed by {user}."

    def addBook(self, book):
        
        book = book.strip()

        validate_book(book)

        key = self._normalize(book)

        if key in self.book_lookup:
            return f"Book '{book}' already exists."

        self.bookList.append(book)
        self.book_lookup[key] = book

        with open(self.database_path, "a") as f:
            f.write(f"\n{book}")

        return f"Book '{book}' added successfully."

    def returnBook(self, book):
        
        book = book.strip()

        validate_book(book)

        key = self._normalize(book)

        self.cursor.execute("SELECT * FROM borrowed_books WHERE LOWER(book)=?", (key,))
        result = self.cursor.fetchone()

        if not result:
            return f"Book '{book}' is not borrowed."

        self.cursor.execute("DELETE FROM borrowed_books WHERE LOWER(book)=?", (key,))
        self.conn.commit()

        return f"Book '{book}' returned successfully."
