from tkinter import *
import re
from PIL import Image, ImageTk

# Created class to make signup form in tkinter
class Signup:
    def __init__(self, root):
        # Instance attributes
        # Root widget
        self.root = root
        self.root.resizable(False, False)
        self.root.title("Sign up SmartX")
        self.root.geometry("1000x667")

        self.bg = ImageTk.PhotoImage(Image.open("images/AdobeStock_162870060-e1531903647410.jpeg"))
        self.bg_label = Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create frame to allow the user to put in their details.
        self.frame = Frame(self.root, bg="#fff", padx=40, pady=30)
        self.frame.place(x=75, y=164, height=340, width=400)

        self.signup_title = Label(self.frame, text="Join SmartX", font=("Impact", 35), bg="#fff", fg="#00d5ff")
        self.signup_title.pack(pady=(0, 10))
        
        self.email_lbl = Label(self.frame, text="Email", font=("Calibri", 20), bg="#fff", fg="orange")
        self.email_lbl.pack(anchor=W)

        self.email_ent = Entry(self.frame, width=20, font=("Calibri", 20), fg="orange", bg="#fff")
        self.email_ent.pack()

# Create window
root = Tk()

# Instance of class
sign_up = Signup(root)

# Event loop
root.mainloop()
