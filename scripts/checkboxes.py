from tkinter import *

root = Tk()
root.title("PizzaTop")
root.resizable(False, False)
root.iconbitmap("logos/food-pizza_115113.ico")

win = Toplevel()
win.title("PizzaTop")
win.resizable(False, False)
win.iconbitmap("logos/food-pizza_115113.ico")

label_show = Label(win, text="         Current option chosen:         ")
label_show.pack()

string_var = StringVar()

ask_topping = Label(root, text="Choose your toppings")
ask_topping.pack()

frame = Frame(root, padx=10)
frame.pack(ipadx=53, anchor=W)

def show_button_check():
    global label_checkbox
    label_checkbox.pack_forget()
    label_checkbox = Label(win, text=string_var.get())
    label_checkbox.pack()

toppings = [("Cheese", "Cheese"), ("Pepperoni", "Pepperoni"), ("Chicken", "Chicken"), ("BBQ Sauce", "BBQ Sauce"), ("Chillis", "Chillis")]

for key, value in toppings:
    checkbox = Checkbutton(frame, text=key, onvalue=value, variable=string_var, command=show_button_check)
    checkbox.deselect()
    checkbox.pack(anchor=W)

label_checkbox = Label(frame, text="")

root.mainloop()