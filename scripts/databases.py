from tkinter import *
import sqlite3

# Confinguring window and features
root = Tk()
root.title("Databases")
root.geometry("400x400")
root.resizable(False, False)

# Databases
database_connect = sqlite3.connect("databases/address-book.db")


# Creating main event loop
root.mainloop()