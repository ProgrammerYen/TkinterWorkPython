from tkinter import *
import sqlite3

# Confinguring window and features
root = Tk()
root.title("Databases")
root.geometry("400x400")
root.resizable(False, False)

# Create or connect to a database
database_connect = sqlite3.connect("address-book.db")

# Creating cursor
cursor = database_connect.cursor()

# Make table in database
cursor.execute("""CREATE A TABLE addresses (
    first_name text
    last_name text
    address text
    city text
    age integer
    zipcode integer)""")

# Commit changes
database_connect.commit()

# Close database connection
database_connect.close()

# Creating main event loop
root.mainloop()