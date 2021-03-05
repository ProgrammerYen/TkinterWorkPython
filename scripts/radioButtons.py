from tkinter import *

root = Tk()
root.title("Pizza Top")
root.resizable(False, False)

label = Label(root, text="Choose your topping")
label.pack()

frame = LabelFrame(root, text="", padx=10, pady=10)
frame.pack(ipadx=53, padx=5)

option = StringVar()
option.set(None)

options = [
    ("Pepperoni", "Pepperoni"),
    ("Cheese", "Cheese"),
    ("Onions", "Onions"),
    ("Mushrooms", "Mushrooms"),
    ("Tomatoes", "Tomatoes"),
]

for name, value in options:
    r = Radiobutton(frame, text=name, variable=option, value=value, command=lambda: optionGet(option.get()))   
    r.pack(anchor=W)

def optionGet(val): 
    global label
    label.pack_forget()
    label = Label(root, text=val)
    label2.pack()
    label.pack()

label2 = Label(root, text="Current Option chosen:")
label = Label(root, text=option.get())

label2.pack(padx=10)

root.mainloop()