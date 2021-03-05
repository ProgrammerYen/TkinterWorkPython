from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("PizzaTop")
root.iconbitmap("logos/food-pizza_115113.ico")

win = Toplevel()
win.iconbitmap("logos/food-pizza_115113.ico")
win.resizable(False, False)
win.title("PizzaTop")

label_topping = Label(root, text="Choose your topping")
label_topping.pack()

frame = LabelFrame(root, text="", padx=5)
frame.pack(ipadx=53, padx=5, pady=5)

label_show = Label(win, text="Current topping chosen for pizza:")

label_show.pack(padx=10, pady=(10, 3))

radio_var = StringVar()
radio_var.set(None)

radio_buttons = {"Pepperoni": "Pepperoni", "Cheese": "Cheese", "Mushrooms": "Mushrooms", "Chicken": "Chicken"}

for key, value in radio_buttons.items():
    Radiobutton(frame, text=key, variable=radio_var, value=value, command=lambda: show_radio_button(radio_var.get())).pack(anchor=W)

def show_radio_button(value):
    global label_radio
    label_radio.pack_forget()
    label_radio = Label(win, text=value)
    label_radio.pack()

label_radio = Label(root, text=radio_var.get())

mainloop()