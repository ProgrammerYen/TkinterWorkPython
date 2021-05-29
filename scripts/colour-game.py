from tkinter import *
from tkinter import messagebox
import random
import time

class ColourGame:
    def __init__(self, sign):
        """Create main window for GUI"""
        # Instance attributes.
        # Defining root.
        self.sign = sign
        self.sign.resizable(False, False)
        self.sign.title("Colour Game")
        self.sign.geometry("510x530")
        self.sign.configure(bg="#fff")
        self.sign.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Timer colour game.
        self.timer_frame = Frame(self.sign, bg="#fff", padx=10, pady=10)
        self.timer_frame.pack(anchor=W)
        
        self.timer = Label(self.timer_frame, text="Timer: 30 seconds", fg="#29e000",
                           bg="#fff", font=("Arial", 15))
        self.timer.pack()
        
        # Title and other features.
        self.txt = "Guess the Colour"
        
        self.count = 0
        self.text = '' 
        self.color = ["#00d5ff","#f29844", "red2", "#8B4513"]                                                        
        self.heading = Label(self.sign,text=self.txt, font=("Impact", 35),bg="#fff",fg="#00d5ff")
        self.heading.pack(pady=(15, 30))
        self.slider()
        
        self.heading_color()
        
        self.heading_description = Label(self.sign,
                                         text=
                                         "Welcome to Guess the Colour. Enter the colour \nof the word displayed below. How many points\n can you win under thirty seconds!",
                                         bg="#fff", fg="#af00e0", font=("yu gothic ui", 12))
        self.heading_description.pack(pady=(0,8))
        
        # Frame for points label and colour word
        self.points_frame = Frame(self.sign, bg="#fff")
        self.points_frame.pack()
        
        self.points = 0
        self.point_lbl = Label(self.points_frame, text="Your Points: "
                               + str(self.points), fg="#29e000", bg="#fff", font=("Arial", 25))
        self.point_lbl.grid(row=0, column=0, pady=10)
        
        
        self.colour_word = Label(self.points_frame, text="Purple", font=("Calibri", 30), fg="#00d5ff",
                                 bg="#fff")
        self.colour_word.grid(row=1, column=0, pady=10)
        
        self.entry_colour = Entry(self.sign, font=("gouldy old style", 16), fg="#ff59e3", bd=0,
                                  highlightthickness=1, width=27)
        self.entry_colour.config(highlightcolor="#00d5ff", highlightbackground="#00d5ff")
        self.entry_colour.pack(pady=(10, 0))
        
        self.frame_submit = Frame(bg="#fff")
        self.frame_submit.pack(pady=(40, 20))
        
        # Colours to choose from
        self.colours_hex = {"#00d5ff": "blue", "#f29844": "orange", "red2": "red",
                            "#8B4513": "brown", "#fffc47": "yellow", "#29e000": "green",
                            "#00e5ff": "cyan", "#ff59e3": "pink", "#af00e0": "purple",
                            }
        
        # Name of colour hex.
        self.hex_colours = ["#00d5ff", "#f29844", "red2", "#8B4513", "#fffc47",
                            "#af00e0", "#ff59e3", "#00e5ff", "#29e000"]
        
        self.colours_string = """Amber
Apricot
Aqua
Auburn
Azure
Beige
Black
Blue
Bronze
Brown
Burgundy
Charcoal
Cherry
Blossom
Pink
Chocolate
Cobalt
Copper
Cream
Crimson
Cyan
Dandelion
Denim
Ecru
Emerald green
Forest green
Fuchsia 
Green
Grey  
Indigo
Ivory
Jade    
Khaki   
Lavender
Lemon
Lilac
Lime green
Magenta
Maroon
Mauve
Mint green
Moss green
Mustard
Olive
Orange  
Peach
Pink
Powder
Blue
Puce
Prussian blue
Purple
Quartz
Grey 
Red
Rose
Royal blue
Ruby
Salmon pink
Sandy brown
Sapphire
Scarlet Shocking pink
Silver
Sky blue
Tan
Tangerine
Turquoise
Violet
White        
Yellow""".title()
        
        # Name of colour word.
        self.colour_words = self.colours_string.split("\n")
        
        self.submit_colour = Button(self.frame_submit, text="Guess Colour", fg="#fff",
                                    bg="#00d5ff", bd=0, activebackground="#fff",
                                    activeforeground="#00d5ff", highlightthickness=1,
                                    font=("Lato", 15), padx=8, command=self.submit_guess_colour)
        self.submit_colour.config(highlightcolor="#00d5ff", highlightbackground="#00d5ff")
        self.submit_colour.grid(row=0, column=0, ipady=5)
        
        self.reset_points = Button(self.frame_submit, text="Reset Points", fg="#fff",
                                    bg="#ff59e3", bd=0, activebackground="#fff",
                                    activeforeground="#ff59e3", highlightthickness=1,
                                    font=("Lato", 15), padx=8, command=self.reset_score)
        self.reset_points.config(highlightcolor="#ff59e3", highlightbackground="#ff59e3")
        self.reset_points.grid(row=0, column=1, ipady=5)
        
        self.start_timer = Button(self.frame_submit, text="Start Timer", fg="#fff",
                                    bg="orange", bd=0, activebackground="#fff",
                                    activeforeground="orange", highlightthickness=1,
                                    font=("Lato", 15), padx=9, command=self.start_colour_timer)
        self.start_timer.config(highlightcolor="orange", highlightbackground="orange")
        self.start_timer.grid(row=0, column=2, ipady=5)
        
        if self.entry_colour.get().lower() == "blue":
            self.point_lbl.pack_forget()
            self.points += 1
            self.point_lbl.pack(pady=10)
            
        self.colour_right = Label(self.frame_submit)
        self.random_right_comments = ["That's right, well done!", "Correct!", "Good Choice!",
                                      "Wow, your right!", "Well Done!"]
        self.random_wrong_comments = ["Almost there!", "Wrong but good try!", "Nearly!",
                                      "Don't give up!", "That was close!",
                                      "Come on, work harder!"]

        # Setting the value of the timer second number.
        self.i = 30


    def start_colour_timer(self):
        "Begin the 30 second timer for colour game."

        if self.i == 0:
            self.sign.geometry("510x590")
            self.colour_right = Label(self.frame_submit,
                                      text="Game Over! Final Score: {}".format(str(self.points)), bg="#8B4513",
                                      fg="#fff", font=("Calibri", 25), pady=7, width=24)
            self.colour_right.grid(row=1, column=0, columnspan=3)

        self.timer.pack_forget()

        self.timer = Label(self.timer_frame, text=f"Time left: {str(self.i)}", fg="#29e000", bg="#fff",
                            font=("Arial", 15))

        self.timer.pack()

        self.i -= 1

        if self.i >= 0:
            self.timer.after(1000, self.start_colour_timer)

 
    def submit_guess_colour(self):
        "Submit guess and checks whether the user's colour guess is correct or incorrect."
        
        self.sign.geometry("510x590")
        
        if self.entry_colour.get().lower() == self.colours_hex[self.colour_word["fg"]]:
            self.point_lbl.grid_forget()
            self.points += 1
        
            self.point_lbl = Label(self.points_frame, text="Your Points: " + str(self.points),
                                   fg="#29e000", bg="#fff", font=("Arial", 25))
            self.point_lbl.grid(row=0, column=0, pady=10)
            
            self.colour_right = Label(self.frame_submit,
                                      text=random.choice(self.random_right_comments), bg="#29e000",
                                      fg="#fff", font=("Calibri", 25), pady=7, width=24)
            
        else:
            self.colour_right = Label(self.frame_submit,
                                      text=random.choice(self.random_wrong_comments), bg="#ff5252",
                                      fg="#fff", font=("Calibri", 25), pady=7, width=24)

        self.colour_right.grid(row=1, column=0, columnspan=3)
            
        
        self.colour_word.grid_forget()
        
        self.word_choice = random.choice(self.colour_words)
        self.colour_word_choice = random.choice(self.hex_colours)
        
        while self.colours_hex[self.colour_word_choice] == self.word_choice:
            self.colour_word_choice = random.choice(self.hex_colours)
        
        self.colour_word = Label(self.points_frame, text=self.word_choice, font=("Calibri", 30),
                                 fg=self.colour_word_choice, bg="#fff")
        self.colour_word.grid(row=1, column=0, pady=10)
        
        self.entry_colour.delete(0, END)
         
    def slider(self):
        """Makes letters in the title begin to appear each time and repeats process"""

        if self.count>=len(self.txt):
            self.count = -1
            self.text = ''
            self.heading.config(text=self.text)

        else:
            self.text = self.text+self.txt[self.count]
            self.heading.config(text=self.text)

        self.count+=1

        self.heading.after(100,self.slider)

    
    def heading_color(self):
        """Changes colour of title"""

        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)
     
     
    def on_closing(self):
        """Message shown before exiting colour game"""

        if messagebox.askokcancel("Leave colour game", "Are you sure you wanna quit?"):
            self.sign.destroy()
    
    
    def reset_score(self):
        """Changes the point score back to the default value - 0"""

        global points
        self.point_lbl.grid_forget()
        self.points = 0
        
        self.point_lbl = Label(self.points_frame, text="Your Points: " + str(self.points), fg="#29e000",
                               bg="#fff", font=("Arial", 25))
        self.point_lbl.grid(row=0, column=0, pady=10)
        
        
# Create window
colour_gui = Tk()

# Instance of class
colour_game = ColourGame(colour_gui)

# Event loop
mainloop()