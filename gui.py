import tkinter as tk
from tkinter import messagebox
from library import Library
from PIL import Image, ImageTk


def load_books():

    with open("LibraryDataset.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

def start_gui():

    books = load_books()
    lib = Library("Pouya's Library")

    root = tk.Tk()
    root.title("Library Management System")
    root.geometry("450x500")
    root.resizable(False, False)
    
    bg_image = Image.open("Images\\library.jpg")
    bg_image = bg_image.resize((450, 500))
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = tk.Canvas(root, width=450, height=500)
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
    canvas.bg_photo = bg_photo

    canvas.create_text(
    220, 35,
    text="Pouya's Library",
    font=("Arial", 18, "bold"),
    justify= "center",
    fill="white"
    )
    
    canvas.create_text(
    110, 80,
    text="Book:",
    font=("Arial", 14, "bold"),
    justify= "left",
    fill="white"
    )
    
    entry_book = tk.Entry(root, width=25)
    canvas.create_window(270, 80, window=entry_book)
    
    canvas.create_text(
    130, 110,
    text="Username:",
    font=("Arial", 14, "bold"),
    justify= "left",
    fill="white"
    )
    
    entry_user = tk.Entry(root, width=25)
    canvas.create_window(270, 110, window=entry_user)

    display_lst = tk.Listbox(root, width=45, height=12, font=("Sans", 10), bg="white", fg="Black", border=2, relief="groove", justify="left")

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
    
    frame_add_button = tk.Frame(root)
    canvas.create_window(225, 165, window=frame_add_button)
    tk.Button(frame_add_button, text="Add Book", font=("Arial", 10, "bold"), width=15, command=add_book, bg="lightblue", fg="black").pack()
    
    frame_borrow_button = tk.Frame(root)
    canvas.create_window(145, 210, window=frame_borrow_button)
    tk.Button(frame_borrow_button, text="Borrow Book", font=("Arial", 10, "bold"), width=15, command=lend_book, bg="yellow", fg="black").pack()
    
    frame_return_button = tk.Frame(root)
    canvas.create_window(310, 210, window=frame_return_button)
    tk.Button(frame_return_button, text="Return Book", font=("Arial", 10, "bold"), width=15, command=return_book, bg="lightgreen", fg="black").pack()

    canvas.create_text(
    220, 255,
    text="Library Collection:",
    font=("Arial", 16, "bold"),
    justify= "center",
    fill="white"
    )
    
    canvas.create_window(220, 380, window=display_lst)

    display_books()

    root.mainloop()
