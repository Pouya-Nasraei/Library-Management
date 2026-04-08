import tkinter as tk
from tkinter import messagebox
from library import Library


def load_books():

    with open("LibraryDataset.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def start_gui():

    books = load_books()
    lib = Library(books, "Pouya's Library")

    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("500x450")
    root.configure(bg="LightGray")

    tk.Label(root, text="Pouya's Library", font=("Arial", 16, "bold"), bg="LightGray").pack(pady=10)

    frame_inputs = tk.Frame(root, bg="LightGray")
    frame_inputs.pack(pady=10)

    tk.Label(frame_inputs, text="Book:", font=("Arial", 12), bg="LightGray").grid(row=0, column=0, padx=5)
    entry_book = tk.Entry(frame_inputs, width=30)
    entry_book.grid(row=0, column=1, padx=5)

    tk.Label(frame_inputs, text="Username:", font=("Arial", 12), bg="LightGray").grid(row=1, column=0, padx=5)
    entry_user = tk.Entry(frame_inputs, width=30)
    entry_user.grid(row=1, column=1, padx=5)

    display = tk.Listbox(root, width=50, height=10, font=("Sans", 10), bg="white", fg="Black", border=2, relief="groove", )

    def display_books():

        display.delete(0, tk.END)

        for book in lib.displayBooks():
            display.insert(tk.END, " " + book)

    def lend_book():

        try:

            result = lib.lendBook(entry_book.get(), entry_user.get())
            messagebox.showinfo("Borrow Book", result)
            display_books()

        except ValueError as e:

            messagebox.showerror("Validation Error", str(e))

    def add_book():

        try:

            result = lib.addBook(entry_book.get())
            messagebox.showinfo("Add Book", result)
            display_books()

        except ValueError as e:

            messagebox.showerror("Validation Error", str(e))

    def return_book():

        try:

            result = lib.returnBook(entry_book.get())
            messagebox.showinfo("Return Book", result)
            display_books()

        except ValueError as e:

            messagebox.showerror("Validation Error", str(e))

    frame_buttons = tk.Frame(root, bg="LightGray")
    frame_buttons.pack(pady=10)

    tk.Button(frame_buttons, text="Display Books", width=15, command=display_books).grid(row=0, column=0, padx=5)
    tk.Button(frame_buttons, text="Borrow Book", width=15, command=lend_book).grid(row=0, column=1, padx=5)
    tk.Button(frame_buttons, text="Add Book", width=15, command=add_book).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(frame_buttons, text="Return Book", width=15, command=return_book).grid(row=1, column=1, padx=5, pady=5)

    tk.Label(root, text="Library Collection:", font=("Arial", 12, "bold"), bg="LightGray").pack(pady=10)

    display.pack()

    display_books()

    root.mainloop()
