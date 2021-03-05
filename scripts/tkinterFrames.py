from tkinter import *

root = Tk()
root.title("Learn to code at Codemy.com")
root.iconbitmap("logos/codecademy_logo_icon_145396.ico")

frame = Frame(root, padx=20, pady=20, relief=RAISED, bd=3)
frame.pack(padx=30, pady=30)

button = Button(frame, text="Dont click here", padx=20, pady=20, relief=SUNKEN, bd=1.5, state=DISABLED, width=20)
button2 = Button(frame, text="...or here", padx=20, pady=20, relief=SUNKEN, bd=1.5, state=DISABLED, width=20)
button3 = Button(frame, text="Click Here", padx=20, pady=20, relief=SUNKEN, bd=1.5, width=20)
button4 = Button(frame, text="...or here", padx=20, pady=20, relief=SUNKEN, bd=1.5, width=20)

button.grid(row=0, column=0)
button2.grid(row=0, column=1)
button3.grid(row=1, column=0)
button4.grid(row=1, column=1)

root.mainloop()