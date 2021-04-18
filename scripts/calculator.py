from tkinter import *

# Creating root widget
root = Tk()
root.title("Calculator")
root.resizable(False, False)
root.iconbitmap("logos/Calculator_30001.ico")
root.configure(bg="#fff")


# Input field
e = Entry(root, width=10,justify=RIGHT, bg="#f2f2f0", bd=0, highlightthickness=0, font=("Calibri", 60))
e.config(highlightcolor="#f2f2f0", highlightbackground="#f2f2f0")
e.grid(row=0, column=0, columnspan=4, ipady=110)    

# Defining functions
def buttonClick(num):
  global fnum_dup
  
  fnum_dup = ""
  if num == "-":
    current = e.get()
    if current == "":
      e.delete(0, END)
      e.insert(0, "-" + str(current))
      fnum = "-" + str(current)
      fnum_dup = fnum   
      
    else:
      try:
        if float(current).is_integer():
          e.delete(0, END)
          e.insert(0, -1 * int(current))
          fnum = -1 * int(current)
          fnum_dup = fnum
            
        else:
          e.delete(0, END)
          e.insert(0, -1 * float(current))
          fnum = -1 * float(current)
          fnum_dup = fnum
          
      except:
        try:
          e.delete(0, END)
          e.insert(0, -1 * float(current))
          fnum = -1 * float(current)
          fnum_dup = fnum
          
        except:
          pass 
          
  else:  
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(num))
    fnum = str(current) + str(num)
    fnum_dup = fnum

def buttonClear():
  e.delete(0,END)


def buttonAdd():
  global fnum
  global math
  
  try:
    newNum = e.get()
    math = "a"
    fnum = float(newNum)
    e.delete(0,END)
    
  except:
    pass

def buttonSub():
  global fnum
  global math
  
  try:
    newNum = e.get()
    math = "s"
    fnum = float(newNum)
    e.delete(0,END)
    
  except:
    pass


def buttonMul():
  global fnum
  global math
  
  
  try:
    newNum = e.get()
    math = "m"
    fnum = float(newNum)
    e.delete(0,END)
    
  except:
    pass


def buttonDiv():
  global fnum
  global math
  
  try:
    newNum = e.get()
    math = "d"
    fnum = float(newNum)
    e.delete(0,END)
    
  except:
    pass


def buttonSqrt():
  global fnum
  global math
  
  try:
    newNum = e.get()
    math = "sqrt"
    fnum = newNum
    e.delete(0, END)

  except:
    pass
  
  
def buttonEqual():
  global snum
  global math
  global fnum_dup
  
  snum = e.get()
  e.delete(0,END)
  try:
      # Checking which operation to do
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
            res = round(float(fnum) - float(snum), 10)
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
            res = round(float(snum) ** (1/2), 10)
            if res.is_integer():
                e.insert(0, int(res))
            
            else:
                e.insert(0, res)
        except:
            e.insert(0, "Math Error")
        
  except:
      pass
        
# Defining buttons.
button_1 = Button(root, text="1", padx=36, pady=20, command=lambda: buttonClick(1), bg="#fff", bd=0, highlightthickness=2,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_2 = Button(root, text="2", padx=35, pady=20, command=lambda: buttonClick(2), bg="#fff", bd=0, highlightthickness=2,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_3 = Button(root, text="3", padx=41, pady=20, command=lambda: buttonClick(3), bg="#fff", bd=0, highlightthickness=2,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")

button_4 = Button(root, text="4", padx=36, pady=20, command=lambda: buttonClick(4), bg="#fff", bd=0, highlightthickness=2,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_5 = Button(root, text="5", padx=35, pady=20, command=lambda: buttonClick(5), bg="#fff", bd=0, highlightthickness=2,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_6 = Button(root, text="6", padx=41, pady=20, 
command=lambda: buttonClick(6), bg="#fff", bd=0, highlightthickness=2, font=("Calibri", 18), activebackground="orange", activeforeground="#fff")

button_7 = Button(root, text="7", padx=38, pady=25, command=lambda: buttonClick(7), bg="#fff", bd=0, highlightthickness=0,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_8 = Button(root, text="8", padx=35, pady=20, command=lambda: buttonClick(8), bg="#fff", bd=0, highlightthickness=2,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_9 = Button(root, text="9", padx=41, pady=20, command=lambda: buttonClick(9), bg="#fff", bd=0, highlightthickness=2,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
 
button_0 = Button(root, text="0", padx=87, pady=21, command=lambda: buttonClick(0), bg="#fff", bd=0, highlightthickness=2,
                  font=("Calibri", 18), activebackground="orange", activeforeground="#fff")
button_add = Button(root, text="+", padx=41, pady=21, command=lambda: buttonAdd(), bg="#fff", bd=0, highlightthickness=2,
                    font=("Calibri", 18), activebackground="#3bd1ff", activeforeground="#fff", fg="#3bd1ff")
button_sub = Button(root, text="-", padx=43.4, pady=21, command=lambda: buttonSub(), bg="#fff", bd=0, highlightthickness=2,
                    font=("Calibri", 18), activebackground="#3bd1ff", activeforeground="#fff", fg="#3bd1ff")

button_mul = Button(root, text="x", padx=41.5, pady=20, command=lambda: buttonMul(), bg="#fff", bd=0, highlightthickness=2,
                    font=("Calibri", 18), activebackground="#3bd1ff", activeforeground="#fff", fg="#3bd1ff")
button_div = Button(root, text="÷", padx=41, pady=20, command=lambda: buttonDiv(), bg="#fff", bd=0, highlightthickness=2,
                    font=("Calibri", 18), activebackground="#3bd1ff", activeforeground="#fff", fg="#3bd1ff")
button_equal = Button(root, text="=", padx=43, pady=23, command=lambda: buttonEqual(), bg="#3bd1ff", bd=0, highlightthickness=0,
                      font=("Calibri", 18), activebackground="#00ffbf", activeforeground="#fff", fg="#fff")

button_clear = Button(root, text="AC", padx=30, pady=23, command=lambda: buttonClear(), bg="#fcd7d7", bd=0, highlightthickness=0,
                      font=("Calibri", 18), activebackground="#fff", activeforeground="#ff5c5c", fg="#ff5c5c")
button_sqrt = Button(root, text="√", padx=40, pady=22, command=lambda: buttonSqrt(), bg="#fff", bd=0, highlightthickness=0,
                     font=("Calibri", 18), activebackground="orange", activeforeground="#fff", fg="orange")

decimal_point = Button(root, text=".", padx=40, pady=13, command=lambda: buttonClick("."), bg="#fff", bd=0, highlightthickness=2,
                       font=("Calibri", 23), activebackground="orange", activeforeground="#fff")

button_minus = Button(root, text="+/-", padx=26, pady=13, command=lambda: buttonClick("-"), bg="#fff", bd=0, highlightthickness=2,
                       font=("Calibri", 23), activebackground="orange", activeforeground="#fff", fg="orange")

var_list = [button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9, button_0, button_add, button_sub,
            button_mul, button_div, button_equal, button_clear, button_sqrt]
for i in var_list:
    i.config(highlightbackground="#fff", highlightcolor="#fff")

button_7.grid(row=2, column=0)
button_8.grid(row=2, column=1)
button_9.grid(row=2, column=2)

button_4.grid(row=3, column=0)
button_5.grid(row=3, column=1)
button_6.grid(row=3, column=2)

button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_0.grid(row=5, column=0, columnspan=2)

button_minus.grid(row=1, column=2)

button_add.grid(row=1, column=3)
button_sub.grid(row=2, column=3)
button_mul.grid(row=3, column=3)
button_div.grid(row=4, column=3)
button_sqrt.grid(row=1, column=1)

button_clear.grid(row=1, column=0)
button_equal.grid(row=5, column=3)                   
decimal_point.grid(row=5, column=2)

# Event loop
root.mainloop()