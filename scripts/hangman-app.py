from tkinter import *
import random
from PIL import ImageTk, Image

root = Tk()
root.title("Hangman")
root.configure(bg="#fff")
root.resizable(False, False)
root.geometry("1350x620")

stages = ["C:/Users/DeAlwis_Consulting/OneDrive/Family/Yenula/python_work/Project/tkinterThings/scripts/s12.png", 
          "C:/Users/DeAlwis_Consulting/OneDrive/Family/Yenula/python_work/Project/tkinterThings/scripts/s22.png",
          "C:/Users/DeAlwis_Consulting/OneDrive/Family/Yenula/python_work/Project/tkinterThings/scripts/s32.png",
          "C:/Users/DeAlwis_Consulting/OneDrive/Family/Yenula/python_work/Project/tkinterThings/scripts/s42.png",
          "C:/Users/DeAlwis_Consulting/OneDrive/Family/Yenula/python_work/Project/tkinterThings/scripts/s52.png",
          "C:/Users/DeAlwis_Consulting/OneDrive/Family/Yenula/python_work/Project/tkinterThings/scripts/s62.png",
          "C:/Users/DeAlwis_Consulting/OneDrive/Family/Yenula/python_work/Project/tkinterThings/scripts/s72.png"]

READ = "r"
file_name = "C:/Users/DeAlwis_Consulting/OneDrive/Family/Yenula/python_work/Project/tkinterThings/scripts/dictionary.txt"
with open(file_name, READ, encoding="utf-8") as f_obj:
    lines = f_obj.readlines()
    lines = [i for i in lines if len(i) > 6]
    word = random.choice(lines) 

underscore_letters = ("_ "*(len(word)-1)).strip()
stage = 1
count = 0
num_letters = 1


def hang_letter():
    global entry_letter
    global underscore_letters
    global word
    global stage
    global count
    global num_letters
    global mission
    global image_lbl
    global image
    global underscore_word
    global letter_guess
    
    guess_letter = entry_letter.get()
    
    if guess_letter in word:
        index_in_word = [i*2 for i in range(len(word)) if word[i] == guess_letter]
        underscore_letters = list(underscore_letters)
            
        for i in index_in_word:
            del underscore_letters[i]
            underscore_letters.insert(i, guess_letter)
            
        underscore_letters = "".join(underscore_letters)
        underscore_word["text"] = underscore_letters
        num_letters += 1
        
    if guess_letter not in word:
        count += 1
        image_lbl.place_forget()
        image = ImageTk.PhotoImage(
            Image.open(stages[count]))
        image_lbl = Label(image=image, bd=0)
        image_lbl.place(x=5, y=10)
        if count == 6:
            mission["text"] = f"You murderer! You killed him!!\nThe word was {word}"
            letter_guess = Label(frame_hang, text="Guess a letter. Save Mr Hang", bg="#bb00ff", 
                      fg="#fff", activebackground="#bb00ff", activeforeground="#fff", padx=30, pady=10, bd=0,
                      font=("Monaco", 20), highlightthickness=1)
            image_lbl.place_forget()
            image = ImageTk.PhotoImage(
                Image.open("C:/Users/DeAlwis_Consulting/OneDrive/Family/Yenula/python_work/Project/tkinterThings/scripts/s82.png"))
            image_lbl = Label(image=image, bd=0)
            image_lbl.place(x=5, y=10)
    
    if num_letters == len(word):
        mission["text"] = "Well done you won! :)"
        
    
image = ImageTk.PhotoImage(
    Image.open("C:/Users/DeAlwis_Consulting/OneDrive/Family/Yenula/python_work/Project/tkinterThings/scripts/s12.png"))
image_lbl = Label(image=image, bd=0)
image_lbl.place(x=30, y=10)
                   
frame_hang = Frame(bg="#fff")
frame_hang.place(x=630, y=20)                   
                   
lbl_hangman = Label(frame_hang, text="Stop hangin' man", bg="#fff", font=("Stencil", 55), fg="#1e90ff")
lbl_hangman.grid(row=0, column=0)

mission = Label(frame_hang, text="Save Mr Hang from being hung to death! :O", bg="#fff", font=("Goudy Old Style", 20), fg="#ff00fb")
mission.grid(row=1, column=0, pady=(20, 0))

underscore_word = Label(frame_hang, text=underscore_letters, bg="#fff", font=("times new roman", 30), fg="#00db0f")
underscore_word.grid(row=2, column=0)

lbl_letter = Label(frame_hang, text="Guess a letter", bg="#fff", font=("Impact", 60), fg="red2")
lbl_letter.grid(row=3, column=0, pady=(0, 30))

entry_letter = Entry(frame_hang, bg="#fff", bd=0, highlightthickness=2, font=("Calibri", 30), width=30, fg="#1e90ff")
entry_letter.config(highlightbackground="orange", highlightcolor="orange")
entry_letter.grid(row=4, column=0)

letter_guess = Button(frame_hang, text="Guess a letter. Save Mr Hang", bg="#bb00ff", 
                      fg="#fff", activebackground="#bb00ff", activeforeground="#fff", padx=30, pady=10, bd=0,
                      font=("Monaco", 20), highlightthickness=1, command=hang_letter)
letter_guess.config(highlightbackground="#bb00ff", highlightcolor="#bb00ff")
letter_guess.grid(row=5, column=0, pady=(40, 0))


mainloop()