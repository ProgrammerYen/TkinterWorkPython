from tkinter import *

# Creating window
root = Tk()
root.title("Sliders")
root.iconbitmap("logos/sliders_icon_128308.ico")
root.resizable(False, False)

# Size of window.
root.geometry("250x250")

frame = Frame(root)
frame.pack(expand=True)

def vertical_show(value, grid_values):
    """Shows vertical value and resizes the page to be the dimensions of the vertical and horizontal values"""
    global show_vertical
    show_vertical.grid_forget()
    show_vertical = Label(frame, text=value)
    show_vertical.grid(row=grid_values[0], column=grid_values[1])
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))
    
def horizontal_show(value, grid_values):
    """Shows horizontal value and resizes the page to be the dimensions of the vertical and horizontal values"""
    global show_horizontal
    show_horizontal.grid_forget()
    show_horizontal = Label(frame, text=value)
    show_horizontal.grid(row=grid_values[0], column=grid_values[1])
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))
    
show_vertical = Label(frame, text="")
show_horizontal = Label(frame, text="")

# Vertical Slider.
vertical = Scale(frame, from_=250, to=500)
vertical.grid(row=0, column=0)

# Button executes the code written in the function, vertical_show when pressed.
show_vertical_button = Button(frame, text="Y Dimension", command=lambda: vertical_show(vertical.get(), (2, 0)))
show_vertical_button.grid(row=1, column=0, pady=(5, 0))


# Horizontal Slider.
horizontal = Scale(frame, from_=250, to=500, orient=HORIZONTAL)
horizontal.grid(row=0, column=2, padx=(30, 0))

# Button executes the code written in the function horizontal_show when pressed.
show_horizontal_button = Button(frame, text="X Dimension", command=lambda: horizontal_show(horizontal.get(), (2, 2)))
show_horizontal_button.grid(row=1, column=2, padx=(35, 0))

# Creating event loop in order to run the program.
root.mainloop()