from tkinter import *
from tkinter import messagebox
import random

# Creating window in root.
root = Tk()
# Title of GUI window.
root.title("Codemy | Learn to code now!")
# Configuring the background color for the window.
root.configure(bg="#000")
# Disabling user from resizing the window.
root.resizable(False, False)

# Creating messagebox window in function.
def message():
    website = "codemy.com"
    # List of domain names.
    domains = [".com", ".gov", ".org", ".co.uk", ".edu", ".net", ".io"]
    
    # Checking whether the variable website has a domain name.
    if "." in website:
        response = messagebox.askyesno(f"Learn to code at {website.capitalize()}", "Are you sure you wish to exit Codemy.com?")
        if response == 1:    
            root.destroy()
        
    else:
        response = messagebox.askyesno(f"Learn to code at {website.capitalize()}" + random.choice(domains),
                                          "Are you sure you wish to exit Codemy.com?")
        if response == 1:    
            root.destroy()         

button = Button(root, text="Exit Program", font=(None, 25), bg="#000", fg="#fff", command=message, activebackground="#000",
                activeforeground="#fff", width=19)
button.grid(row=0, column=0)


mainloop()
