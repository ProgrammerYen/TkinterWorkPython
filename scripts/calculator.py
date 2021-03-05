from tkinter import *

# Creating Root Widget.
root = Tk()

# Main body of the code.
root.title("Calculator")
root.geometry("440x540")
root.configure(bg="#4ddbff")
root.iconbitmap("logos/Calculator_30001.ico")
root.resizable(False, False)

expression = ""
def Press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def EqualPress():
    global expression
    try:
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:
        equation.set("Math Error")
        expression = ""
def ClearButton():
    global expression
    expression = ""
    equation.set("0")

buttonFrame = Frame(root, bg="#4ddbff")
buttonFrame.pack()
equation = StringVar()
inputField = Entry(buttonFrame, textvariable=equation, justify="right", font=("arial", 25, "bold"))

button1 = Button(buttonFrame, text="1", font=("times new roman", 15), relief="ridge", bd=1, bg="#4ddbff",
                 width=8, height=3, command=lambda: Press(1))
button2 = Button(buttonFrame, text="2", font=("times new roman", 15), relief="ridge", bd=1, bg="#4ddbff",
                 width=8, height=3, command=lambda: Press(2))
button3 = Button(buttonFrame, text="3", font=("times new roman", 15), relief="ridge", bd=1, bg="#4ddbff",
                 width=8, height=3, command=lambda: Press(3))
addition = Button(buttonFrame, text="+", font=("times new roman", 15), relief="ridge", bd=1, bg="#4ddbff",
                 width=8, height=3, command=lambda: Press("+"))
button4 = Button(buttonFrame, text="4", font=("times new roman", 15), relief="ridge", bd=1, bg="#4ddbff",
                 width=8, height=3, command=lambda: Press(4))
button5 = Button(buttonFrame, text="5", font=("times new roman", 15), relief="ridge", bd=1, bg="#4ddbff",
                 width=8, height=3, command=lambda: Press(5))
button6 = Button(buttonFrame, text="6", font=("times new roman", 15), relief="ridge", bd=1, bg="#4ddbff",
                 width=8, height=3, command=lambda: Press(6))
subtraction = Button(buttonFrame, text="-", font=("times new roman", 15), relief="ridge", bd=1, bg="#4ddbff",
                 width=8, height=3, command=lambda: Press("-"))
button7 = Button(buttonFrame, text="7", font=("times new roman", 15), relief="ridge", bd=1, bg="#4ddbff",
                 width=8, height=3, command=lambda: Press(7))
button8 = Button(buttonFrame, text="8", font=("times new roman", 15), relief="ridge", bd=1, bg="#4ddbff",
                 width=8, height=3, command=lambda: Press(8))
button9 = Button(buttonFrame, text="9", font=("times new roman", 15), relief="ridge", bd=1, bg="#4ddbff",
                 width=8, height=3, command=lambda: Press(9))
multiply = Button(buttonFrame, text="*", font=("times new roman", 15), relief="ridge", bd=1, bg="#4ddbff",
                 width=8, height=3, command=lambda: Press("*"))
button0 = Button(buttonFrame, text="0", font=("times new roman", 15), relief="ridge", bd=1, bg="#4ddbff",
                 width=8, height=3, command=lambda: Press(0))
decimalPoint = Button(buttonFrame, text=".", font=("times new roman", 15), relief="ridge", bd=1, bg="#4ddbff",
                 width=8, height=3, command=lambda: Press("."))
clear = Button(buttonFrame, text="C", font=("times new roman", 15), relief="ridge", bd=1, bg="#4ddbff",
                 width=8, height=3, command=ClearButton)
divide = Button(buttonFrame, text="/", font=("times new roman", 15), relief="ridge", bd=1, bg="#4ddbff",
                 width=8, height=3, command=lambda: Press("/"))
equals = Button(buttonFrame, text="=", font=("times new roman", 15), relief="ridge", bd=1, bg="#4ddbff",
                 width=8, height=3, command=EqualPress)

inputField.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=15)

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
addition.grid(row=1, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
subtraction.grid(row=2, column=3)

button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
multiply.grid(row=3, column=3)

button0.grid(row=4, column=0)
decimalPoint.grid(row=4, column=1)
clear.grid(row=4, column=2)
divide.grid(row=4, column=3)

equals.grid(row=5, column=0)

# Creating an event loop.
root.mainloop()