from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import random
import string

# 63 883 Cybersecurity lock stock photos

# Creating main window.
root = Tk()
root.title("PyPassword Generator")
root.resizable(False, False)
root.geometry("1224x768")

# Background image.
password_image = ImageTk.PhotoImage(Image.open("C:/Users/DeAlwis_Consulting/OneDrive/Family/Yenula/python_work/Project/tkinterThings/scripts/lock.jpg").resize((1224, 768)))
password_lbl = Label(image=password_image)
password_lbl.place(x=0, y=0)

# Frame with all the main parts of the password generator.
frame = Frame(root, bg="#fff", padx=50, pady=50)
frame.place(x=120, y=150)

letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

# Title
title = Label(frame, text="PyPassword", fg="#ff0000", bg="#fff",
              font=("Impact", 40))
title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

# Choice of number of letters.
letters_lbl = Label(frame, text="No. letters", font=("Calibri", 20), fg="#00d5ff",
                    bg="#fff")
letters_lbl.grid(row=1, column=0, pady=20, padx=(0, 20))

# Variable stores the combobox value chosen of letters.
store_letters = StringVar()
store_letters.set(6)

letters_cbx = ttk.Combobox(frame, textvariable=store_letters, state="readonly", width=12)
letters_cbx["value"] = list(range(6, 16))
letters_cbx.grid(row=1, column=1, ipady=2)

# Choice of number of digits.
digits_lbl = Label(frame, text="No. digits", font=("Calibri", 20), fg="#00d5ff",
                    bg="#fff")
digits_lbl.grid(row=2, column=0, pady=20, padx=(0, 30))

# Variable stores the combobox value chosen of digits.
store_digits = StringVar()
store_digits.set(3)

digits_cbx = ttk.Combobox(frame, textvariable=store_digits, state="readonly", width=12)
digits_cbx["value"] = list(range(3, 8))
digits_cbx.grid(row=2, column=1, ipady=2)

# Choice of number of symbols.
symbols_lbl = Label(frame, text="No. symbols", font=("Calibri", 20), fg="#00d5ff",
                    bg="#fff")
symbols_lbl.grid(row=3, column=0, pady=20)

# Variable stores the combobox value chosen of symbols.
store_symbols = StringVar()
store_symbols.set(3)

symbols_cbx = ttk.Combobox(frame, textvariable=store_symbols, state="readonly", width=12)
symbols_cbx["value"] = list(range(3, 8))
symbols_cbx.grid(row=3, column=1, ipady=2)

count = -1

show_choice = Label()
def display_password():
	global count
	global password_name
	global gen_pass


	count += 1

	password_name.grid_forget()

	password_name["text"] = gen_pass[:count]
	password_name.grid(row=4, column=0, columnspan=2, pady=(20, 0))

	password_name.after(100, display_password)


def generate_password():
    global password_name
    global store_letters
    global store_digits
    global store_symbols
    global gen_pass
    
    try:
        password_name.grid_forget()
    
    except:
        pass

    generate_btn.grid_forget()
    
    num_letters = store_letters.get()
    num_digits = store_digits.get()
    num_symbols = store_symbols.get()
    
    letters_choice = [random.choice(letters) for i in range(int(num_letters))]
    numbers_choice = [random.choice(numbers) for i in range(int(num_digits))]
    symbols_choice = [random.choice(symbols) for i in range(int(num_symbols))]

    letters_choice.extend(numbers_choice)
    letters_choice.extend(symbols_choice)
    random.shuffle(letters_choice)
    
    password = "".join(letters_choice)
    gen_pass = f"Your password is: {password}."
    password_name = Label(frame, text=gen_pass, fg="orange",
                      font=("Stencil", 10), bg="#fff")
    
    frame.place(x=120, y=100)
    
    display_password()
    
    generate_btn.grid(row=5, column=0, columnspan=2, pady=(35, 0))
    
# Button to generate random password.
generate_btn = Button(frame, text="Generate Password", bg="#ff36da", fg="#fff",
                      activebackground="#fff", activeforeground="#ff36da", font=("Calibri", 20),
                      padx=10, pady=5, bd=0,  command=generate_password)
generate_btn.config(highlightcolor="#ff36da", highlightbackground="#ff36da")

generate_btn.grid(row=4, column=0, columnspan=2, pady=(35, 0))

# Event loop running program.
mainloop()
