from datetime import datetime, date
from tkinter import *
from PIL import Image, ImageTk
import calendar
from tkinter import messagebox

root = Tk()
root.title("Age calculator")
root.configure(bg="#101a36")
root.resizable(False, False)


def calculate_age():
    try:
        if name_entry.get().strip() == "":
            messagebox.showinfo("Invalid Name", "Please enter a valid name of length greater than zero.")
        
        else:
            isleap = calendar.isleap(int(datetime.now().year))
            if isleap:
                age_years = int((date.today() - date(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()))).days) // 366
                
            else:
                age_years = int((date.today() - date(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()))).days) // 365
            
            if age_years < 0:
                pass
            
            else:
                submit_info.pack_forget()
                label_age = Label(root, text=name_entry.get().title().strip() + " is " + str(age_years) + " years old.", font=("Calibri", 25),
                                fg="#fff", bg="#101a36").pack(anchor=W, padx=13)
                submit_info.pack(pady=(20, 10))
            
    except:
        messagebox.showerror("Invalid Input", "Please enter inputs that are valid integers.")

photo = ImageTk.PhotoImage(Image.open("images/old-age.webp").resize((620, 340)))
label_photo = Label(root, image=photo)
label_photo.pack(pady=(10, 0), padx=10)

frame = Frame(root, padx=10, pady=10, bg="#101a36")
frame.pack(anchor=W)

name_label = Label(frame, text="                        Name", font=("Calibri", 20), fg="#fff", bg="#101a36")
name_label.grid(row=0, column=0, pady=20)

name_entry = Entry(frame, font=("Calibri", 20), width=26, bg="#101a36", highlightthickness=1, fg="#fff")
name_entry.config(highlightbackground="#fff", highlightcolor="#fff")
name_entry.grid(row=0, column=1, pady=20)

year_label = Label(frame, text=" Year (in form yyyy)", font=("Calibri", 20), fg="#fff", bg="#101a36")
year_label.grid(row=1, column=0)

year_entry = Entry(frame, font=("Calibri", 20), width=26, bg="#101a36", highlightthickness=1, fg="#fff")
year_entry.config(highlightbackground="#fff", highlightcolor="#fff")
year_entry.grid(row=1, column=1)

month_label = Label(frame, text="Month (in form mm)   ", font=("Calibri", 20), fg="#fff", bg="#101a36")
month_label.grid(row=2, column=0, pady=(20, 0))

month_entry = Entry(frame, font=("Calibri", 20), width=26, bg="#101a36", highlightthickness=1, fg="#fff")
month_entry.config(highlightbackground="#fff", highlightcolor="#fff")
month_entry.grid(row=2, column=1, pady=(20, 0))

day_label = Label(frame, text="      Day (in form dd)", font=("Calibri", 20), fg="#fff", bg="#101a36")
day_label.grid(row=3, column=0, pady=(20, 10))

day_entry = Entry(frame, font=("Calibri", 20), width=26, bg="#101a36", highlightthickness=1, fg="#fff")
day_entry.config(highlightbackground="#fff", highlightcolor="#fff")
day_entry.grid(row=3, column=1, pady=(20, 10))

submit_info = Button(root, text="Calculate age", bg="orange", fg="#fff", font=("Calibri", 25), padx=210, bd=0,
                     command=calculate_age, activebackground="orange", activeforeground="#fff")
submit_info.pack(pady=10)

root.mainloop()
