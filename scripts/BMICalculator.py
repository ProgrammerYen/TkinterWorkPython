from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("BMI Calculator")
root.configure(bg="#000")
root.iconbitmap("logos/scale_weight_3065.ico")
root.resizable(False, False)

title = Label(root, text="BMI Calculator", fg="#fff", bg="#000", font=("Calibri", 33, "bold")).pack(pady=(3, 13))

nameLabelAct = Label(root, text="Enter your name:", fg="#fff", bg="#000", font=(None, 19))
nameLabelAct.pack()

nameact = Entry(root, fg="#fff", bg="#000", font=(None, 19), bd=0, highlightthickness=2, justify=CENTER)
nameact.config(highlightbackground="orange", highlightcolor="orange")
nameact.pack(ipadx=50, ipady=10, anchor=CENTER)    

ageLabelAct = Label(root, text="Enter your age:", fg="#fff", bg="#000", font=(None, 19))
ageLabelAct.pack()

ageact = Entry(root, fg="#fff", bg="#000", font=(None, 19), bd=0, highlightthickness=2, justify=CENTER)
ageact.config(highlightbackground="orange", highlightcolor="orange")
ageact.pack(ipadx=50, ipady=10, anchor=CENTER)    

ageLabel = Label(root, text="Enter your height (m):", fg="#fff", bg="#000", font=(None, 19))
ageLabel.pack()

age = Entry(root, fg="#fff", bg="#000", font=(None, 19), bd=0, highlightthickness=2, justify=CENTER)
age.config(highlightbackground="orange", highlightcolor="orange")
age.pack(ipadx=50, ipady=10, padx=10, anchor=CENTER)

nameLabel = Label(root, text="Enter your weight (kg):", fg="#fff", bg="#000", font=(None, 19))
nameLabel.pack()

name = Entry(root, fg="#fff", bg="#000", font=(None, 19), bd=0, highlightthickness=2, justify=CENTER)
name.config(highlightbackground="orange", highlightcolor="orange")
name.pack(ipadx=50, ipady=10, anchor=CENTER)    

def askSubmit():
    global bmi
    global showBmi
    
    response = messagebox.askyesno("Verifying Submission", "Are you sure you wish to submit this form?")
    if response == 1:
        try:
            showBmi.pack_forget()
            bmi.pack_forget()
            bmiActual = round(float(name.get())/(float(age.get()))**2, 3)
            bmi = Label(root, fg="#fff", bg="#000", font=("Calibri", 19), bd=0, text=
                        f"Body mass index (3 d.p): {str(bmiActual)}")
            bmi.pack(ipadx=21)
            

            if bmiActual < 18.5:
                weightStatus = "underweight"
                showBmi = Label(root, fg="#fff", bg="#000", font=("Calibri", 19), bd=0, text="Weight Status: " + str(weightStatus))           
                showBmi.pack()

            elif bmiActual < 25:
                weightStatus = "healthy"
                showBmi = Label(root, fg="#fff", bg="#000", font=("Calibri", 19), bd=0, text="Weight status: " + str(weightStatus))    
                showBmi.pack()

            elif bmiActual < 30:
                weightStatus = "overweight"
                showBmi = Label(root, fg="#fff", bg="#000", font=("Calibri", 19), bd=0, text="Weight status: " + str(weightStatus))
                showBmi.pack()

            else:
                weightStatus = "obese"
                showBmi = Label(root, fg="#fff", bg="#000", font=("Calibri", 19), bd=0, text="Weight status: " + weightStatus)
                showBmi.pack()
                
            fileName = "nameAge.csv"
            APPEND = "a"    
            
            with open(fileName, APPEND, encoding="utf-8") as fileObj:
                fileObj.write(str(nameact.get()) + ", " + str(ageact.get()) + ", " + str(bmiActual) + ", " + weightStatus + "\n")
                
            name.delete(0, END)
            age.delete(0, END)
            nameact.delete(0, END)
            ageact.delete(0, END)

        except:
            messagebox.showerror("Invalid input", "The inputs that you have entered are not valid numbers or it is unable to divide by.")
       
spacePack = Label(root, text="", fg="#fff", bg="#000").pack() 
frame = Frame(root, background="orange")
            
bmi = Label(root, text="", fg="#fff", bg="#000")
showBmi = Label(root, text="", fg="#fff", bg="#000")

submitSurvey = Button(frame, text="Submit Survey", fg="#fff", bg="#000", padx=10, pady=10, bd=0, font=(None, 17),
                      activebackground="#000", activeforeground="#fff", command=askSubmit)

submitSurvey.pack(padx=2, pady=2)
frame.pack(pady=(0, 18))

root.mainloop() 