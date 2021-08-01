from tkinter import *
from tkinter import ttk

# Creating window for gui
root = Tk()
root.title("Tic Tac Toe")
root.resizable(False, False)

player_frame = Frame(root, bg="#fff")
player_frame.pack()

focusBorderImageData = '''
    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
    Ry/99NIz//oGrZpUUEAAOw==
'''

borderImageData = '''
    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
'''

style = ttk.Style()
borderImage = PhotoImage("borderImage", data=borderImageData)
focusBorderImage = PhotoImage("focusBorderImage", data=focusBorderImageData)

style.element_create("RoundedFrame",
                     "image", borderImage,
                     ("focus", focusBorderImage),
                     border=16, sticky="nsew")
style.layout("RoundedFrame",
             [("RoundedFrame", {"sticky": "nsew"})])

frame1 = ttk.Frame(player_frame, style="RoundedFrame", padding=10)
text1 = Label(frame1, borderwidth=0, highlightthickness=0,
                width=13, height=1, bg="#fff", text="O     -",
              font=("Calibri", 15), fg="#00d5ff", pady=4)
text1.pack(fill="both", expand=True)

text1.bind("<FocusIn>", lambda event: frame1.state(["focus"]))
text1.bind("<FocusOut>", lambda event: frame1.state(["!focus"]))

frame2 = ttk.Frame(player_frame, style="RoundedFrame", padding=10)
text2 = Label(frame2, borderwidth=0, highlightthickness=0,
            width=9, height=1, text="×     -", font=("Calibri", 20),
              bg="#fff", fg="#00d5ff")
text2.pack(fill="both", expand=True)

text2.bind("<FocusIn>", lambda event: frame2.state(["focus"]))
text2.bind("<FocusOut>", lambda event: frame2.state(["!focus"]))

root.configure(background="white")
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)

frame1.focus_set()

count = 1
grid_positions = []
grid_pos_val = []

def count_nums(l):
    for i in range(len(l)):
        if l.count(l[i]) == 3:
            return i

def count_diagonal(l):
     return ((0,0) in l and (1,1) in l and (2,2) in l) or ((2,0) in l and (1,1) in l and (0,2) in l)
       
       
def btn_press(btn, grid_pos):
    """Check to see if a player has won"""
    
    global  grid_pos_vals
    global count
    global grid_positions
    
    if btn["text"] == "":
        if count % 2 == 0:
            btn["text"] = "❌"
            grid_positions.append((grid_pos, "×"))
            
            
        else:
            btn["text"], btn["font"] = "O", ("Calibri", 15, "bold")
            grid_positions.append((grid_pos, "O"))
        
        # Grid Pos
        grid_pos_val.append(grid_pos)
        
        # Symbols of player
        grid_pos_symx = [i for i in grid_positions if i[-1] == "×"]
        grid_pos_symo = [i for i in grid_positions if i[-1] == "O"]
        
        # Row and column vals of x
        grid_row_vals_x = [i[0][0] for i in grid_positions if i[-1] == "×"]
        grid_col_vals_x = [i[0][1] for i in grid_positions if i[-1] == "×"]
        
        # Row and column vals of o
        grid_row_vals_o = [i[0][0] for i in grid_positions if i[-1] == "O"]
        grid_col_vals_o = [i[0][1] for i in grid_positions if i[-1] == "O"]
        
        # Grid pos of x
        grid_pos_x = [i[0] for i in grid_positions if i[-1] == "×"]
        
        # Grid pos of o
        grid_pos_o = [i[0] for i in grid_positions if i[-1] == "O"]
      
        x_vals = [] 
        
        vals_len = []
        if len(grid_positions) > 4:
            if len(grid_pos_symo) > 2 or len(grid_pos_symx) > 2:
                if len(grid_pos_symo) > 2:
                    vals_len.append(grid_pos_symo)
                    
                if len(grid_pos_symx) > 2:
                    vals_len.append(grid_pos_symx)
              
                win_frame = Frame(root, bg="#fff")
                win_frame.pack()
                    
                player_win = Label(win_frame, text="Player one won!!".upper(), font=("Impact", 20),
                                   bg="#00d5ff", fg="#fff", width=17, pady=10, padx=35)
                var_buttons = [(btn1, (0,0)), (btn2, (0,1)), (btn3, (0,2)), (btn4, (1,0)),
                               (btn5, (1,1)), (btn6, (1,2)), (btn7, (2,0)), (btn8, (2,1)),
                               (btn9, (2,2))]
                
                if count_nums(grid_row_vals_o) != None or count_nums(grid_col_vals_o) != None:
                    player_win.grid(row=0, column=0, ipadx=35)
                    for i in var_buttons:
                        if i[-1] not in grid_pos_val:
                            i[0]["state"] = DISABLED
                            
                elif count_diagonal(grid_pos_x):
                    player_win["text"] = "Player two won!!".upper()
                    player_win.pack()
                    for i in var_buttons:
                        if i[-1] not in grid_pos_val:
                            i[0]["state"] = DISABLED

                elif count_diagonal(grid_pos_o):
                    player_win.pack()
                    for i in var_buttons:
                        if i[-1] not in grid_pos_val:
                            i[0]["state"] = DISABLED
                    
                elif count_nums(grid_row_vals_x) != None or count_nums(grid_col_vals_x) != None:
                    player_win["text"] = "Player two won!!".upper()
                    player_win.pack()
                    for i in var_buttons:
                        if i[-1] not in grid_pos_val:
                            i[0]["state"] = DISABLED
                            
                

        count += 1


btn_frame = Frame(root, bg="#fff")
btn_frame.pack()

# Buttons for tic tac toe.
btn1 = Button(btn_frame, text="", bg="orange", activebackground="#fff",
              activeforeground="#ffbb00", fg="#fff", highlightthickness=3,
              command=lambda: btn_press(btn1, (0,0)))
btn1.grid(row=0, column=0, padx=2, pady=2, ipadx=3)

btn2 = Button(btn_frame, text="", bg="orange", activebackground="#fff",
              activeforeground="#ffbb00", fg="#fff", highlightthickness=3,
              command=lambda: btn_press(btn2, (0, 1)))
btn2.grid(row=0, column=1, padx=2, pady=2, ipadx=3)

btn3 = Button(btn_frame, text="", bg="orange", activebackground="#fff",
              activeforeground="#ffbb00", fg="#fff", highlightthickness=3,
              command=lambda: btn_press(btn3, (0, 2)))
btn3.grid(row=0, column=2, padx=2, pady=2, ipadx=3)

btn4 = Button(btn_frame, text="", bg="orange", activebackground="#fff",
              activeforeground="#ffbb00", fg="#fff", highlightthickness=3,
              command=lambda: btn_press(btn4, (1, 0)))
btn4.grid(row=1, column=0, padx=2, pady=2, ipadx=3)

btn5 = Button(btn_frame, text="", bg="orange", activebackground="#fff",
              activeforeground="#ffbb00", fg="#fff", highlightthickness=3,
              command=lambda: btn_press(btn5, (1, 1)))
btn5.grid(row=1, column=1, padx=2, pady=2, ipadx=3)

btn6 = Button(btn_frame, text="", bg="orange", activebackground="#fff",
              activeforeground="#ffbb00", fg="#fff", highlightthickness=3,
              command=lambda: btn_press(btn6, (1, 2)))
btn6.grid(row=1, column=2, padx=2, pady=2, ipadx=3)

btn7 = Button(btn_frame, text="", bg="orange", activebackground="#fff",
              activeforeground="#ffbb00", fg="#fff", highlightthickness=3,
              command=lambda: btn_press(btn7, (2, 0)))
btn7.grid(row=2, column=0, padx=2, pady=2, ipadx=3)

btn8 = Button(btn_frame, text="", bg="orange", activebackground="#fff",
              activeforeground="#ffbb00", fg="#fff", highlightthickness=3,
              command=lambda: btn_press(btn8, (2, 1)))
btn8.grid(row=2, column=1, padx=2, pady=2, ipadx=3)

btn9 = Button(btn_frame, text="", bg="orange", activebackground="#fff",
              activeforeground="#ffbb00", fg="#fff", highlightthickness=3,
              command=lambda: btn_press(btn9, (2, 2)))
btn9.grid(row=2, column=2, padx=2, pady=2, ipadx=3)

var_buttons = [btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9]

for i in range(1, len(var_buttons)+1):
    var_buttons[i-1]["bg"], var_buttons[i-1]["width"], var_buttons[i-1]["bd"], var_buttons[i-1]["font"], var_buttons[i-1]["height"] = "#ffbb00", 8, 0, ("Calibri", 15), 3
    var_buttons[i-1].config(highlightcolor="#fff", highlightbackground="#fff")


# Event loop
root.mainloop()
