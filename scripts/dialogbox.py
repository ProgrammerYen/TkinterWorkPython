from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("PizzaTop")
root.geometry("300x300")
root.iconbitmap("logos/food-pizza_115113.ico")

root.filename = filedialog.askopenfilename(
    initialdir="C:/Users/DeAlwis_Consulting/OneDrive/Family/Yenula",
    title = "Please select a file", filetypes=(("All Files", "*.*"), ("Plain Text", "*.txt"), ("png", "*.png"), ("jpg", "*.jpg"), ("ico", "*.ico"),
                                               ("html", "*.html"), ("python", "*.py"), ("CSS", "*.css")))   

root.mainloop()