import tkinter as tk
from tkinter import messagebox
import json
import os


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
        if book not in self.bookList:
            return f"❌ '{book}' is not in the library."

        if book in self.lendDict:
            return f"❌ '{book}' is already borrowed by {self.lendDict[book]}"

        self.lendDict[book] = user
        self.save_borrow_data()
        return f"📚 '{book}' has been borrowed by {user}."

    def addBook(self, book):
        if book in self.bookList:
            return "⚠️ Book already exists."

        self.bookList.append(book)

        with open(self.database_path, "a") as f:
            f.write(f"\n{book}")

        return "✅ Book added successfully."

    def returnBook(self, book):
        if book not in self.lendDict:
            return "⚠️ Book is not borrowed."

        self.lendDict.pop(book)
        self.save_borrow_data()
        return "✅ Book returned successfully."


with open("LibraryDataset.txt", "r") as f:
    books = [line.strip() for line in f.readlines()]

lib = Library(books, "Pouya's Library")



def display_books():
    display.delete(0, tk.END)
    for book in lib.displayBooks():
        display.insert(tk.END, book)

def lend_book():
    book = entry_book.get()
    user = entry_user.get()

    result = lib.lendBook(book, user)
    messagebox.showinfo("Lend Book", result)
    display_books()

def add_book():
    book = entry_book.get()
    result = lib.addBook(book)
    messagebox.showinfo("Add Book", result)
    display_books()

def return_book():
    book = entry_book.get()
    result = lib.returnBook(book)
    messagebox.showinfo("Return Book", result)
    display_books()



root = tk.Tk()
root.title("Library Management System")
root.geometry("500x450")
root.configure(bg="white")

tk.Label(root, text="Pouya's Library", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

frame_inputs = tk.Frame(root, bg="white")
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Book:", font=("Arial", 12), bg="white").grid(row=0, column=0, padx=5)
entry_book = tk.Entry(frame_inputs, width=30)
entry_book.grid(row=0, column=1, padx=5)

tk.Label(frame_inputs, text="Username:", font=("Arial", 12), bg="white").grid(row=1, column=0, padx=5)
entry_user = tk.Entry(frame_inputs, width=30)
entry_user.grid(row=1, column=1, padx=5)

frame_buttons = tk.Frame(root, bg="white")
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Display Books", width=15, command=display_books).grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Borrow Book", width=15, command=lend_book).grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Add Book", width=15, command=add_book).grid(row=1, column=0, padx=5, pady=5)
tk.Button(frame_buttons, text="Return Book", width=15, command=return_book).grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Library Collection:", font=("Arial", 12, "bold"), bg="white").pack(pady=10)

display = tk.Listbox(root, width=50, height=10)
display.pack()

display_books()

root.mainloop()
