from tkinter import *

# Creating root widget
root = Tk()
root.title("Calculator")
root.resizable(False, False)
root.configure(bg="#fff")


# Input field
e = Entry(root, width=11, justify=RIGHT, bg="#f2f2f0", bd=0, highlightthickness=0, font=("Calibri", 50))
e.config(highlightcolor="#f2f2f0", highlightbackground="#f2f2f0")
e.grid(row=0, column=0, columnspan=4, ipady=110)

# Defining functions
def buttonClick(num):
  current = e.get()
  e.delete(0, END)
  e.insert(0, str(current)+str(num))
  fnum = str(current) + str(num)

def buttonClear():
  e.delete(0,END)

def buttonAdd():
  global fnum
  global math
  newNum = e.get()
  math = "a"
  fnum = float(newNum)
  e.delete(0,END)

def buttonSub():
  global fnum
  global math
  newNum = e.get()
  math = "s"
  fnum = float(newNum)
  e.delete(0,END)

def buttonMul():
  global fnum
  global math
  newNum = e.get()
  math = "m"
  fnum = float(newNum)
  e.delete(0,END)

def buttonDiv():
  global fnum
  global math
  newNum = e.get()
  math = "d"
  fnum = float(newNum)
  e.delete(0,END)

def buttonSqrt():
  global fnum
  global math
  newNum = e.get()
  math = "sqrt"
  fnum = float(newNum)
  e.delete(0,END)


def buttonPerc():
  global fnum
  global math
  newNum = e.get()
  math = "p"
  fnum = float(newNum)
  e.delete(0,END)

def buttonEqual():
  global snum
  global math
  snum = e.get()
  e.delete(0,END)

  # Cheching which operation to do
  if math == "a":
    try:
        res = round(float(snum) + float(fnum), 10)
        if res.is_integer():
            e.insert(0, int(res))
            
        else:
            e.insert(0, res)
        
    except:
        e.insert(0, "Math Error")

  if math == "s":
    try:
        res = round(float(fnum) - float(snum), 0)
        if res.is_integer():
            e.insert(0, int(res))
            
        else:
            e.insert(0, res)
        
    except:
        e.insert(0, "Math Error")

  if math == "m":
    try:
        res = round(float(snum) * float(fnum), 10)
        if res.is_integer():
            e.insert(0, int(res))
        
        else:
            e.insert(0, res)
        
    except:
        e.insert(0, "Math Error")

  if math == "d":
    try:
        res = round(float(fnum)/float(snum), 10)
        if res.is_integer():
            e.insert(0, int(res))
            
        else:
            e.insert(0, res)
        
    except:
        e.insert(0, "Math Error")        

  if math == "sqrt":
    try:
        res = round(float(fnum) ** (1/2), 10)
        if res.is_integer():
            e.insert(0, int(res))
        
        else:
            e.insert(0, res)
    except:
        e.insert(0, "Math Error")

  if math == "p":
    try:
        res = round((float(fnum) / 100) * float(snum), 10)
        if res.is_integer():
            e.insert(0, str(int(res)))

        else:
            e.insert(0, str(res))
            
    except:
        e.insert(0, "Math Error")

# Defining buttons.
button_1 = Button(root, text="1", padx=30, pady=17, command=lambda: buttonClick(1), bg="#fff", bd=0, highlightthickness=2,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_2 = Button(root, text="2", padx=30, pady=17, command=lambda: buttonClick(2), bg="#fff", bd=0, highlightthickness=2,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_3 = Button(root, text="3", padx=30, pady=17, command=lambda: buttonClick(3), bg="#fff", bd=0, highlightthickness=2,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")

button_4 = Button(root, text="4", padx=30, pady=17, command=lambda: buttonClick(4), bg="#fff", bd=0, highlightthickness=2,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_5 = Button(root, text="5", padx=30, pady=17, command=lambda: buttonClick(5), bg="#fff", bd=0, highlightthickness=2,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_6 = Button(root, text="6", padx=30, pady=17, 
command=lambda: buttonClick(6), bg="#fff", bd=0, highlightthickness=2, font=("Calibri", 18), activebackground="orange", activeforeground="#fff")

button_7 = Button(root, text="7", padx=30, pady=17, command=lambda: buttonClick(7), bg="#fff", bd=0, highlightthickness=2,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_8 = Button(root, text="8", padx=30, pady=17, command=lambda: buttonClick(8), bg="#fff", bd=0, highlightthickness=2,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_9 = Button(root, text="9", padx=30, pady=17, command=lambda: buttonClick(9), bg="#fff", bd=0, highlightthickness=2,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
 
button_0 = Button(root, text="0", padx=30, pady=17, command=lambda: buttonClick(0), bg="#fff", bd=0, highlightthickness=2,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_add = Button(root, text="+", padx=31, pady=17, command=lambda: buttonAdd(), bg="#fff", bd=0, highlightthickness=2,
                    font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_sub = Button(root, text="-", padx=34, pady=17, command=lambda: buttonSub(), bg="#fff", bd=0, highlightthickness=2,
                    font=("Calibri", 18), activebackground="orange", activeforeground="#fff")

button_mul = Button(root, text="x", padx=33, pady=17, command=lambda: buttonMul(), bg="#fff", bd=0, highlightthickness=2,
                    font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_div = Button(root, text="÷", padx=30, pady=17, command=lambda: buttonDiv(), bg="#fff", bd=0, highlightthickness=2,
                    font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_equal = Button(root, text="=", padx=80, pady=17, command=lambda: buttonEqual(), bg="orange", bd=0, highlightthickness=0,
                      font=("Calibri", 18), activebackground="#fff", activeforeground="orange", fg="#fff")

button_clear = Button(root, text="AC", padx=71, pady=14.5, command=lambda: buttonClear(), bg="#fff", bd=0, highlightthickness=2,
                      font=("Calibri", 18), activebackground="orange", activeforeground="#fff", fg="orange")
button_sqrt = Button(root, text="√", padx=33, pady=17, command=lambda: buttonSqrt(), bg="#fff", bd=0, highlightthickness=2,
                     font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_perc = Button(root, text="%", padx=34, pady=17, command=lambda: buttonPerc(), bg="#fff", bd=0, highlightthickness=2,
                     font=("Calibri", 18), activebackground="orange", activeforeground="#fff")

var_list = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_0, button_add, button_sub,
            button_mul, button_div, button_equal, button_clear, button_sqrt, button_perc]
for i in var_list:
    i.config(highlightbackground="#fff", highlightcolor="#fff")

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_0.grid(row=4, column=0)

button_perc.grid(row=4, column=1)

button_sub.grid(row=2, column=3)
button_add.grid(row=1, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_sqrt.grid(row=4, column=2)

button_clear.grid(row=5, column=0, columnspan=2)
button_equal.grid(row=5, column=2, columnspan=2)                   

# Event loop
root.mainloop()