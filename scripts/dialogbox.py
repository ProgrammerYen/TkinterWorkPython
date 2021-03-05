from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("PizzaTop")
root.geometry("300x300")
root.iconbitmap("logos/food-pizza_115113.ico")

root.filename = filedialog.askopenfilename(
    initialdir="C:/Users/DeAlwis_Consulting/OneDrive/Family/Yenula",
    title = "Please select a file", filetypes=(("PNG Files", "*.png"), ("JPG Files", "*.jpg"), ("ICO Files", "*.ico")))

fileLabel = Label(root, text=root.filename)
fileLabel.grid(row=0, column=0)
imageChosen = ImageTk.PhotoImage(Image.open(root.filename))

imageLabel = Label(root, image=imageChosen)
imageLabel.grid(row=1, column=0)

def messageExit():
    response = messagebox.askquestion("Verify the you wish to exit program", "Are you sure you wish to exit the program?")
    if response == "yes":
        root.destroy()

buttonExit = Button(root, text="Exit Program", command=messageExit)
buttonExit.grid(row=2, column=0)
root.mainloop()