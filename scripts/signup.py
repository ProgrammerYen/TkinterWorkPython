from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import re

# Created class to make signup form in tkinter
class Signup:
    def __init__(self, root):
        # Instance attributes
        # Root widget
        self.root = root
        self.root.resizable(False, False)
        self.root.title("Sign up SmartX")
        self.root.geometry("1000x667")

        # Backrgound Image
        self.bg = ImageTk.PhotoImage(Image.open("images/AdobeStock_162870060-e1531903647410.jpeg"))
        self.bg_label = Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create frame to allow the user to put in their details.
        self.frame = Frame(self.root, bg="#fff", padx=55, pady=30)
        self.frame.place(x=75, y=164, height=440, width=400)

        # Title for frame that says Join SmartX
        self.txt = "Join SmartX"

        self.count = 0
        self.text = '' 
        self.color = ["#00d5ff","#f29844", "red2", "#8B4513"]														 
        self.heading = Label(self.frame,text=self.txt, font=("Impact", 35),bg="#fff",fg="#00d5ff")
        self.heading.pack(anchor=W, pady=(0, 20))
        self.slider()
        self.heading_color()	

        self.email_lbl = Label(self.frame, text="Email", font=("Calibri", 20), bg="#fff", fg="orange")
        self.email_lbl.pack(anchor=W)

        # Creating entry box for email.
        self.entry = Entry(self.frame, width=25, font=("Calibri", 15), fg="orange", bg="#fff", highlightthickness=1, bd=0)
        self.entry.config(highlightcolor="orange", highlightbackground="orange")
        self.entry.pack(anchor=W, pady=(0,5))

        self.password_lbl = Label(self.frame, text="Create a Password", font=("Calibri", 20), bg="#fff", fg="orange")
        self.password_lbl.pack(anchor=W)

        # Creating variable that holds the value of the password.
        self.password = StringVar()

        # Entry box for password.
        self.entry_pass = Entry(self.frame, width=25, font=("Calibri", 15), fg="orange", bg="#fff", highlightthickness=1, bd=0, textvariable=self.password, show="*")
        self.entry_pass.config(highlightcolor="orange", highlightbackground="orange")
        self.entry_pass.pack(anchor=W, pady=(0, 5))

        self.conf_pas_lbl = Label(self.frame, text="Confirm Password", font=("Calibri", 20), bg="#fff", fg="orange")
        self.conf_pas_lbl.pack(anchor=W)

        # Variable that holds the values of the confirmation password.
        self.confirm_password = StringVar()

        # Confirm password entry box.
        self.confirm_ent = Entry(self.frame, width=25, font=("Calibri", 15), fg="orange", bg="#fff", highlightthickness=1, bd=0, textvariable=self.confirm_password, show="*")
        self.confirm_ent.config(highlightcolor="orange", highlightbackground="orange")
        self.confirm_ent.pack(anchor=W)

        # Button that allows you to login.
        self.login_btn = Button(self.frame, text="Sign up", font=("yu gothic ui", 20), bg="#00d5ff", fg="#fff", bd=0, padx=40, pady=4, command=self.validate_input,
                                activebackground="#00d5ff", activeforeground="#fff")
        self.login_btn.pack(anchor=CENTER, pady=(30, 0))

    def slider(self):
        if self.count>=len(self.txt):
            self.count = -1
            self.text = ''
            self.heading.config(text=self.text)

        else:
            self.text = self.text+self.txt[self.count]
            self.heading.config(text=self.text)

        self.count+=1

        self.heading.after(100,self.slider)

    
    def heading_color(self):
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)

    def validate_input(self):
        email_re = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
        match_email = bool(re.search(email_re, self.entry.get()))

        password_re = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
        match_password = bool(re.search(password_re, self.entry_pass.get()))

        if not match_email:
            messagebox.showinfo("Invalid Email", "Invalid input for email address. Does not follow the standard email format.")

        if not match_password:
            messagebox.showinfo("Weak Password", "Password is too weak.\nConditions for a valid password are:\n1. Should have at least one number.\n2. Should have at least one uppercase and one lowercase character.\n3. Should have at least one special symbol (@$!%*#?&).\n4. Should be between 6 to 20 characters long.")

        if self.confirm_password.get() != self.password.get():
            messagebox.showinfo("Incorrect Password", "Incorrect confirmation password entered.")

        if match_email and match_password and self.confirm_password.get() == self.password.get():
            messagebox.showinfo("Thank you", f"Thank you for signing up at SmartX. We really hope that you will be a great help to us and be a loyal employee.\n\nPassword: {self.password.get()}\n\nPlease keep sensitive information private to yourself and do not share with anybody else")


# Create window
root = Tk()

# Instance of class
sign_up = Signup(root)

# Event loop
root.mainloop()