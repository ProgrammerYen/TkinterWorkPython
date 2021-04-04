from tkinter import *

# Window for app
root = Tk()
root.title("Dropdown")

root.resizable(False, False)

choose_topping = Label(root, text="Choose a topping")
choose_topping.pack(anchor=CENTER)

# Making the frame for dropdown boxes.
frame = Frame(root)
frame.pack(anchor=W, padx=8, pady=8)

# List of values for dropdown box

toppings = ["Cheese", "Pepperoni", "Chillis", "Chicken", "BBQ"]

# Dropdown boxes

store_topping = StringVar()
store_topping.set(toppings[0])

dropdown_toppings = OptionMenu(frame, store_topping, *toppings)
dropdown_toppings.pack()

def topping_choice():
	"""Displays the topping that the user has chosen."""
	global topping
	topping.pack_forget()

	topping = Label(frame, text=store_topping.get())
	topping.pack()

# Button allows user to see topping that has been chosen.

show_topping = Button(frame, text="Show selection", command=topping_choice)
show_topping.pack()

topping = Label(frame, text="")

# Creating event loop
root.mainloop()