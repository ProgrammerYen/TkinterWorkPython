from tkinter import *

root = Tk()
root.title("Pizza Top")
root.resizable(False, False)
root.iconbitmap("logos/sliders_icon_128308.ico")


# Creating class to create sliders.
class Slider:
    # Constructor __init__
    def __init__(self, verticalFrom, verticalTo, horizontalFrom, horizontalTo):
        # Declaring instance attributes
        self.verticalFrom = int(verticalFrom)
        self.verticalTo = int(verticalTo)
        self.horizontalFrom = int(horizontalFrom)
        self.horizontalTo = int(horizontalTo)
    
    # Instance method creating vertical slider.
    def verticalSlider(self):
        global frame   
        frame = Frame(root, padx=20, pady=20)
        frame.grid(row=0, column=0)
        
        labelVertSlider = Label(frame, text="Hello")
        labelVertSlider.grid(row=0, column=0)
        vertical = Scale(frame, from_=self.verticalFrom, to=self.verticalTo) 
        vertical.grid(row=1, column=0)
     
    # Instance method creating horizontal slider.
    def horizontalSlider(self):
        labelSpace = Label(frame, text="      ")
        labelSpace.grid(row=0, column=1)
        horizontal = Scale(frame, from_=self.horizontalFrom, to=self.horizontalTo, orient=HORIZONTAL)
        horizontal.grid(row=0, column=2)


# Instance of class Slider
slider = Slider("0", "100", "10", "200")
slider.verticalSlider()
slider.horizontalSlider()   

root.mainloop()