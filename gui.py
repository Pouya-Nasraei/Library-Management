import tkinter as tk
from tkinter import messagebox
from library import Library
from PIL import Image, ImageTk


def load_books():

    with open("LibraryDataset.txt", "r") as f:
        return [line.strip() for line in f.readlines()]


def start_gui():

    books = load_books()
    lib = Library(books, "Pouya's Library")

    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("500x450")
    
    bg_image = Image.open("Images\\bg.jfif")
    bg_image = bg_image.resize((500, 450))
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = tk.Canvas(root, width=500, height=450)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    canvas.bg_photo = bg_photo

    title_lbl = tk.Label(canvas, text="Pouya's Library", font=("Arial", 16, "bold"), bg=None)
    canvas.create_window(250, 30, window=title_lbl)

    frame_inputs = tk.Frame(root)

    tk.Label(frame_inputs, text="Book:", font=("Arial", 12)).grid(row=0, column=0, padx=5)
    entry_book = tk.Entry(frame_inputs, width=30)
    entry_book.grid(row=0, column=1, padx=5)

    tk.Label(frame_inputs, text="Username:", font=("Arial", 12)).grid(row=1, column=0, padx=5)
    entry_user = tk.Entry(frame_inputs, width=30)
    entry_user.grid(row=1, column=1, padx=5)
    canvas.create_window(250, 85, window=frame_inputs)

    display_lst = tk.Listbox(root, width=50, height=10, font=("Sans", 10), bg="white", fg="Black", border=2, relief="groove")

    def display_books():

        display_lst.delete(0, tk.END)

        for book in lib.displayBooks():
            display_lst.insert(tk.END, " " + book)

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

    frame_buttons = tk.Frame(root)

    tk.Button(frame_buttons, text="Display Books", width=15, command=display_books).grid(row=0, column=0, padx=5)
    tk.Button(frame_buttons, text="Borrow Book", width=15, command=lend_book).grid(row=0, column=1, padx=5)
    tk.Button(frame_buttons, text="Add Book", width=15, command=add_book).grid(row=1, column=0, padx=5, pady=5)
    tk.Button(frame_buttons, text="Return Book", width=15, command=return_book).grid(row=1, column=1, padx=5, pady=5)
    canvas.create_window(250, 160, window=frame_buttons)
    
    collection_lbl = tk.Label(root, text="Library Collection:", font=("Arial", 12, "bold"), bg="LightGray")
    canvas.create_window(250, 225, window=collection_lbl)

    
    canvas.create_window(250, 340, window=display_lst)

    display_books()

    root.mainloop()
