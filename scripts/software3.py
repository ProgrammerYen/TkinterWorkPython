from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Codemy.com | Learn to code now!")
root.configure(bg="#000")
root.resizable(False, False)

def message():
    website = "codemy.com"
    domains = [".com", ".gov", ".org", ".co.uk"]
    if "." in website:
        response = messagebox.askyesno(f"Learn to code at {website.capitalize()}.", "Are you sure you wish to exit this Codemy.com?")
        if response == 1:    
            root.destroy()
        
    else:
        response = messagebox.askyesno(f"Learn to code at {website.capitalize()}" + random.choice(domains),
                                          "Are you sure you wish to exit this Codemy.com?")
        if response == 1:    
            root.destroy()         

button = Button(root, text="Exit Program", font=(None, 20), bg="#000", fg="#fff", command=message, activebackground="#000",
                activeforeground="#fff", width=24)
button.grid(row=0, column=0)


mainloop()
        
    
