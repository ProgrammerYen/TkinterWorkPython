from tkinter import *
from encrypt_data import encrypt_data

# Confinguring window and features
root = Tk()
root.title("Databases")
root.configure(bg="#2C3E50")
root.resizable(False, False)
root.iconbitmap("logos/down_diagram_dropdown_diagram_chart_decrease_icon_153073.ico")

def submit():
    """Submit data into database"""
    file_name = "address-book.db"
    APPEND = "a"
    
    shift_numbers = []
    
    f_name_enc = encrypt_data(f_name.get().strip().lower())
    shift_numbers.append(f_name_enc.split()[-1])
    
    l_name_enc = encrypt_data(l_name.get().strip().lower())
    shift_numbers.append(l_name_enc.split()[-1])
    
    address_enc = encrypt_data(address.get().strip().lower())
    shift_numbers.append(address_enc.split()[-1])
    
    city_enc = encrypt_data(city.get().strip().lower())
    shift_numbers.append(city_enc.split()[-1])
    
    age_enc = encrypt_data(age.get().strip().lower())
    shift_numbers.append(age_enc.split()[-1])
    
    postcode_enc = encrypt_data(postcode.get().strip().lower())
    shift_numbers.append(postcode_enc.split()[-1])
    
    with open(file_name, APPEND, encoding="utf-8") as file_object:
        file_object.write(
            "".join(f_name_enc.split()[:-1]) + ", " + "".join(l_name_enc.split()[:-1])  + ", " + "".join(address_enc.split()[:-1])
            + ", " + "".join(city_enc.split()[:-1]) + ", " + "".join(age_enc.split()[:-1]) + ", " + "".join(postcode_enc.split()[:-1]) + 
            "\n")
        
    file_name2 = "encrypt-data-nums.csv"
    
    with open(file_name2, APPEND, encoding="utf-8") as file_object:             
        file_object.write(shift_numbers[0] + ", " + shift_numbers[1] + ", " + shift_numbers[2] + ", " + shift_numbers[3] + ", " +
                          shift_numbers[4] + ", " + shift_numbers[5] + "\n")
        
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    age.delete(0, END)
    postcode.delete(0, END)

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

add_data = Button(root, text="Add to database", font=("Calibri", 40), padx=106, pady=10, bg="#F89403", fg="white", activebackground="#F89403",
                   activeforeground="white", bd=0, command=submit)
add_data.grid(row=7 , column=0, columnspan=2)

# Creating main event loop
root.mainloop()