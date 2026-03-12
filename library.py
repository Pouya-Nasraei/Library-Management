import json
import os
from validation import validate_book, validate_user


class Library:
    def __init__(self, booklist, name, database_path="LibraryDataset.txt", borrow_path="borrowed_books.json"):
        self.bookList = booklist
        self.name = name
        self.database_path = database_path
        self.borrow_path = borrow_path
        self.lendDict = self.load_borrow_data()

    def load_borrow_data(self):
        if os.path.exists(self.borrow_path):
            with open(self.borrow_path, "r") as f:
                return json.load(f)
        return {}

    def save_borrow_data(self):
        with open(self.borrow_path, "w") as f:
            json.dump(self.lendDict, f, indent=4)

    def displayBooks(self):
        return self.bookList

    def lendBook(self, book, user):

        validate_book(book)
        validate_user(user)

        if book not in self.bookList:
            return f"'{book}' is not in the library."

        if book in self.lendDict:
            return f"'{book}' is already borrowed by {self.lendDict[book]}"

        self.lendDict[book] = user
        self.save_borrow_data()

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

        if book not in self.lendDict:
            return "Book is not borrowed."

        self.lendDict.pop(book)
        self.save_borrow_data()

        return "Book returned successfully."