from tkinter import *

root = Tk()
root.title("Sliders")
root.iconbitmap("logos/sliders_icon_128308.ico")
root.resizable(False, False)

frame = Frame(root)
frame.pack()

vertical = Scale(frame, from_=0, to=200)
vertical.grid(row=0, column=0)

space = Label(frame, text="  ")
space.grid(row=0, column=1)

horizontal = Scale(frame, from_=10, to=200, orient=HORIZONTAL)
horizontal.grid(row=0, column=2)

root.mainloop()