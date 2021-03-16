from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Anonymous Survey")
root.configure(bg="#000")
root.resizable(False, False)

ageLabel = Label(root, text="Enter your height:", fg="#fff", bg="#000", font=(None, 19))
ageLabel.pack()

age = Entry(root, fg="#fff", bg="#000", font=(None, 19), bd=0, highlightthickness=2)
age.config(highlightbackground="orange", highlightcolor="orange")
age.pack(ipadx=50, ipady=10)

spacePack = Label(root, text="", fg="#fff", bg="#000").pack()

nameLabel = Label(root, text="Enter your weight:", fg="#fff", bg="#000", font=(None, 19))
nameLabel.pack()

name = Entry(root, fg="#fff", bg="#000", font=(None, 19), bd=0, highlightthickness=2)
name.config(highlightbackground="orange", highlightcolor="orange")
name.pack(ipadx=50, ipady=10)    

def askSubmit():
    response = messagebox.askyesno("Verifying Submission", "Are you sure you wish to submit this form?")
    if response == 1:
        fileName = "nameAge.csv"
        APPEND = "a"
        with open(fileName, APPEND, encoding="utf-8") as fileObj:
            fileObj.write(name.get().strip() + ", " + age.get().strip() + "\n")
            
        win = Toplevel()
        win.title("Anonymous Survey")
        win.configure(bg="#000")
        win.resizable(False, False)
        
        thankSurveyPart = Label(win, text="Thank you to the following people for participating in this survey")
            
submitSurvey = Button(root, text="Submit Survey", fg="#fff", bg="#000", padx=20, pady=5, bd=0, font=(None, 17),
                      activebackground="#000", activeforeground="#fff", command=askSubmit)
submitSurvey.pack(padx=10)

root.mainloop() 

