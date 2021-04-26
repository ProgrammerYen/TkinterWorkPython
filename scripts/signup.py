from tkinter import *
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
        self.root.title("Login SmartX")
        self.root.geometry("1000x667")

        # Backrgound Image
        self.bg = ImageTk.PhotoImage(Image.open("images/AdobeStock_162870060-e1531903647410.jpeg"))
        self.bg_label = Label(self.root, image=self.bg)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Create frame to allow the user to put in their details.
        self.frame = Frame(self.root, bg="#fff", padx=55, pady=30)
        self.frame.place(x=75, y=164, height=380, width=400)

        # Title for frame that says Join SmartX
        self.txt = "Login Here"
        self.count = 0
        self.text = '' 
        self.color = ["#00d5ff","#f29844", "red2", "#8B4513"]
        self.heading = Label(self.frame,text=self.txt, font=("Impact", 35),bg="#fff",fg="#00d5ff")
        self.heading.pack(anchor=W, pady=(0, 20))
        self.slider()
        self.heading_color()	

        self.email_lbl = Label(self.frame, text="Email", font=("Calibri", 20), bg="#fff", fg="orange")
        self.email_lbl.pack(anchor=W)

        # Creating entry box for email and password.
        self.entry = Entry(self.frame, width=25, font=("Calibri", 15), fg="orange", bg="#fff", highlightthickness=1, bd=0)
        self.entry.config(highlightcolor="orange", highlightbackground="orange")
        self.entry.pack(anchor=W, pady=(0,5))

        self.password_lbl = Label(self.frame, text="Create a Password", font=("Calibri", 20), bg="#fff", fg="orange")
        self.password_lbl.pack(anchor=W)

        self.entry_p = Entry(self.frame, width=25, font=("Calibri", 15), fg="orange", bg="#fff", highlightthickness=1, bd=0)
        self.entry_p.config(highlightcolor="orange", highlightbackground="orange")
        self.entry_p.pack(anchor=W)

        self.login_btn = Button(self.frame, text="Login", font=("yu gothic ui", 20), bg="#00d5ff", fg="#fff", bd=0, padx=40, pady=4)
        self.login_btn.pack(anchor=CENTER, pady=(40, 0))

    
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



# Create window
root = Tk()

# Instance of class
sign_up = Signup(root)

# Event loop
root.mainloop()