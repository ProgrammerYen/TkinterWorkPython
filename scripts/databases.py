from tkinter import *
import sqlite3

# Confinguring window and features
root = Tk()
root.title("Databases")
root.configure(bg="#2C3E50")
root.resizable(False, False)

# Create or connect to a database
database_connect = sqlite3.connect("address-book.db")

# Creating cursor
cursor = database_connect.cursor()

# Entry requests
# first_name
# last_namet
# address
# city
# age
# postal_code

label_top = Label(root, text="Sign up", font=("Calibri", 40), padx=220, pady=10, bg="#F89403", fg="white")
label_top.grid(row=0, column=0, columnspan=2)

label_fname = Label(root, text="    First name", font=("Calibri", 25), fg="white", bg="#2C3E50")
label_fname.grid(row=1, column=0, pady=(30, 0))

f_name = Entry(root, bg="#6C7A89", font=("Calibri", 25), highlightthickness=1, fg="white")
f_name.config(highlightbackground="#6C7A89", highlightcolor="#6C7A89")
f_name.grid(row=1, column=1, pady=(30, 0))

label_lname = Label(root, text="   Last name", font=("Calibri", 25), fg="white", bg="#2C3E50")
label_lname.grid(row=2, column=0, pady=(30, 0))

l_name = Entry(root, bg="#6C7A89", font=("Calibri", 25), highlightthickness=1, fg="white")
l_name.config(highlightbackground="#6C7A89", highlightcolor="#6C7A89")
l_name.grid(row=2, column=1, pady=(30, 0))

label_address = Label(root, text="     Address", font=("Calibri", 25), fg="white", bg="#2C3E50")
label_address.grid(row=3, column=0, pady=(30, 0))

address = Entry(root, bg="#6C7A89", font=("Calibri", 25), highlightthickness=1, fg="white")
address.config(highlightbackground="#6C7A89", highlightcolor="#6C7A89")
address.grid(row=3, column=1, pady=(30, 0))

label_city = Label(root, text="City/Town", font=("Calibri", 25), fg="white", bg="#2C3E50")
label_city.grid(row=4, column=0, pady=(30, 0))

city = Entry(root, bg="#6C7A89", font=("Calibri", 25), highlightthickness=1, fg="white")
city.config(highlightbackground="#6C7A89", highlightcolor="#6C7A89")
city.grid(row=4, column=1, pady=(30, 0))

label_age = Label(root, text="           Age", font=("Calibri", 25), fg="white", bg="#2C3E50")
label_age.grid(row=5, column=0, pady=(30, 0))

age = Entry(root, bg="#6C7A89", font=("Calibri", 25), highlightthickness=1, fg="white")
age.config(highlightbackground="#6C7A89", highlightcolor="#6C7A89")
age.grid(row=5, column=1, pady=(30, 0))

label_postcode = Label(root, text="Postal code", font=("Calibri", 25), fg="white", bg="#2C3E50")
label_postcode.grid(row=6, column=0, pady=30)

postcode = Entry(root, bg="#6C7A89", font=("Calibri", 25), highlightthickness=1, fg="white")
postcode.config(highlightbackground="#6C7A89", highlightcolor="#6C7A89")
postcode.grid(row=6, column=1, pady=30)

add_data = Button(root, text="Add to database", font=("Calibri", 30), padx=139, pady=10, bg="#0096FF", fg="white", activebackground="#0096FF",
                   activeforeground="white")
add_data.grid(row=7 , column=0, columnspan=2)

selection = Button(root, text="Show selection", font=("Calibri", 30), padx=150, pady=10, bg="#0096FF", fg="white", activebackground="#0096FF",
                   activeforeground="white")
selection.grid(row=8, column=0, columnspan=2, pady=10)

# Commit changes    
database_connect.commit()

# Close database connection
database_connect.close()

# Creating main event loop
root.mainloop()