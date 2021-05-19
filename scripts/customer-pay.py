from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import re
import sqlite3

# Creating main window.
root = Tk()

# Title of app
root.title("SmartX - customer pay details")
root.resizable(False, False)

def close_window():
    """Verifies whether the user wants to close window."""
    if messagebox.askokcancel("Exit current window", "Are you sure you wish to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", close_window)

class CustomerPayCRM:
    def __init__(self):
        global entry_vars
        
        self.frame = Frame(root, bg="#fff", padx=35, pady=35)
        self.frame.pack()
        
        self.title = Label(self.frame, text="Customer Pay Details", fg="#00d5ff", bg="#fff",
                           font=("Impact", 30))
        self.title.grid(row=0, column=0)
        
        self.title_description = Label(self.frame, text=
                                       "Welcome to SmartX customer pay. Enter\ndetails below.",
                                       fg="#dedede", bg="#fff", font=("goudy old style", 15),
                                       justify="left")
        self.title_description.grid(row=1, column=0, sticky=W, pady=10)
        
        self.input_frame = Frame(self.frame, bg="#fff")
        self.input_frame.grid(row=2, column=0, sticky=W, pady=5)
        
        self.lbl_fname = Label(self.input_frame, text="First Name:", fg="orange", bg="#fff",
                           font=("Calibri", 15))
        self.lbl_fname.grid(row=0, column=0, sticky=W, padx=(0, 20), pady=3)
        
        self.entry_fname = Entry(self.input_frame, width=23, bd=0, highlightthickness=1,
                                 font=("Calibri", 12), fg="orange")
        self.entry_fname.grid(row=0, column=1, sticky=W, pady=3)
        
        self.lbl_lname = Label(self.input_frame, text="Last Name:", fg="orange", bg="#fff",
                           font=("Calibri", 15))
        self.lbl_lname.grid(row=1, column=0, sticky=W, padx=(0, 20), pady=3)
    
        self.entry_lname = Entry(self.input_frame, width=23, bd=0, highlightthickness=1
                                 , font=("Calibri", 12), fg="orange")
        self.entry_lname.grid(row=1, column=1, sticky=W, pady=3, columnspan=3)
        
        self.lbl_email = Label(self.input_frame, text="Email Address:", fg="orange", bg="#fff",
                           font=("Calibri", 15))
        self.lbl_email.grid(row=2, column=0, sticky=W, padx=(0, 20), pady=3)
    
        self.entry_email = Entry(self.input_frame, width=23, bd=0, highlightthickness=1
                                 , font=("Calibri", 12), fg="orange")
        self.entry_email.grid(row=2, column=1, sticky=W, pady=3)        
        
        self.payment_method = Label(self.input_frame, text="Payment Method:", fg="orange",
                                    bg="#fff", font=("Calibri", 15))
        self.payment_method.grid(row=3, column=0, sticky=W, padx=(0, 20), pady=3)
        
        self.cbx_frame = Frame(self.input_frame, bg="#fff")
        self.cbx_frame.grid(row=3, column=1, sticky=W)
        
        self.store_cbx_pay = StringVar()
        self.store_cbx_pay.set("Bank Transfer")
        
        self.cbx_payment = ttk.Combobox(self.cbx_frame, textvariable=self.store_cbx_pay,
                                        state="readonly", width=14, font=("Calibri", 12))
        
        self.cbx_payment["value"] = ("Bank Transfer", "Paypal")
        self.cbx_payment.grid(row=0, column=0, sticky=W, pady=3, ipady=2, padx=2)
        
        self.address_lbl = Label(self.input_frame, text="Residential Address:", fg="orange",
                                 bg="#fff", font=("Calibri", 15))
        self.address_lbl.grid(row=4, column=0, sticky=W, padx=(0, 20), pady=3)
        
        self.entry_address = Entry(self.input_frame, width=23, bd=0, highlightthickness=1
                                 , font=("Calibri", 12), fg="orange")
        self.entry_address.grid(row=4, column=1, sticky=W, pady=3)
        
        self.account_number = Label(self.input_frame, text="Account Number:", fg="orange",
                                 bg="#fff", font=("Calibri", 15))
        self.account_number.grid(row=5, column=0, sticky=W, padx=(0, 20), pady=3)

        self.entry_account_num = Entry(self.input_frame, width=23, bd=0, highlightthickness=1
                                 , font=("Calibri", 12), fg="orange")
        self.entry_account_num.grid(row=5, column=1, sticky=W, pady=3)
        
        self.neft_ifsc = Label(self.input_frame, text="NEFT IFSC code:", fg="orange",
                                 bg="#fff", font=("Calibri", 15))
        self.neft_ifsc.grid(row=6, column=0, sticky=W, padx=(0, 20), pady=3)

        self.entry_ifsc = Entry(self.input_frame, width=23, bd=0, highlightthickness=1
                                 , font=("Calibri", 12), fg="orange")
        self.entry_ifsc.grid(row=6, column=1, sticky=W, pady=3)
        
        self.submit_btn = Button(self.frame, text="Submit Details", bd=0, padx=20, pady=7,
                                 font=("Calibri", 15), activebackground="#fff",
                                 activeforeground="#00d5ff", fg="#fff", bg="#00d5ff",
                                 command=self.validate_input)
        self.submit_btn.configure(highlightbackground="#00d5ff", highlightcolor="#00d5ff")
        self.submit_btn.grid(row=3, column=0, sticky=W, padx=130, pady=(25,0))              
        
        self.submit_cbx = Button(self.cbx_frame, text="Save", fg="#fff", highlightthickness=1,
                                 bg="orange", font=("Calibri", 12), bd=0, padx=6,
                                 activebackground="#fff", activeforeground="orange",
                                 command=self.submit_payment)
        self.submit_cbx.configure(highlightbackground="orange", highlightcolor="orange")
        self.submit_cbx.grid(row=0, column=1, sticky=W, padx=2)
        
        entry_vars = [self.entry_ifsc, self.entry_account_num, self.entry_address,
                      self.entry_email, self.entry_lname, self.entry_fname]
        
        for i in entry_vars:
            i.config(highlightcolor="#00d5ff", highlightbackground="#00d5ff")
        
        self.account_word = "Account Number:"
        
        
    def submit_payment(self):
        global account_word
        
        self.account_number.grid_forget()
        self.entry_account_num.grid_forget()
        self.neft_ifsc.grid_forget()
        self.entry_ifsc.grid_forget()
        
        if self.store_cbx_pay.get() == "Paypal":
            self.account_number  = Label(self.input_frame, text="Paypal Email:",
                                           fg="orange", bg="#fff", font=("Calibri", 15))
            self.account_number.grid(row=5, column=0, sticky=W, padx=(0, 20), pady=3)
            
            self.entry_account_num = Entry(self.input_frame, width=23, bd=0, highlightthickness=1
                                     , font=("Calibri", 12), fg="orange")
            self.entry_account_num.grid(row=5, column=1, sticky=W, pady=3)
            
            self.neft_ifsc = Label(self.input_frame, text="Paypal Password:", fg="orange",
                                 bg="#fff", font=("Calibri", 15))
            self.neft_ifsc.grid(row=6, column=0, sticky=W, padx=(0, 20), pady=3)

            self.entry_ifsc = Entry(self.input_frame, width=23, bd=0, highlightthickness=1
                                     , font=("Calibri", 12), fg="orange", show="•")
            self.entry_ifsc.grid(row=6, column=1, sticky=W, pady=3)
            
            self.account_word = "Paypal Email:"
            
        else:
            self.account_number = Label(self.input_frame, text="Account Number:", fg="orange",
                                 bg="#fff", font=("Calibri", 15))
            self.account_number.grid(row=5, column=0, sticky=W, padx=(0, 20), pady=3)

            self.entry_account_num = Entry(self.input_frame, width=23, bd=0, highlightthickness=1
                                     , font=("Calibri", 12), fg="orange")
            self.entry_account_num.grid(row=5, column=1, sticky=W, pady=3)
            
            self.entry_account_num.config(highlightcolor="#00d5ff", highlightbackground="#00d5ff")
            
            self.neft_ifsc = Label(self.input_frame, text="NEFT IFSC code:", fg="orange",
                                     bg="#fff", font=("Calibri", 15))
            self.neft_ifsc.grid(row=6, column=0, sticky=W, padx=(0, 20), pady=3)

            self.entry_ifsc = Entry(self.input_frame, width=23, bd=0, highlightthickness=1
                                     , font=("Calibri", 12), fg="orange")
            self.entry_ifsc.grid(row=6, column=1, sticky=W, pady=3)
            
            self.account_word = "Account Number:"
            
        self.entry_ifsc.config(highlightcolor="#00d5ff", highlightbackground="#00d5ff")
        self.entry_account_num.config(highlightcolor="#00d5ff", highlightbackground="#00d5ff")

            
    def validate_input(self):
        global account_word
        global entry_vars
        
        # Creates connection to database
        connect_database = sqlite3.connect("customer-pay.db")
                
        # Cursor to addd data as tables in database.
        cursor = connect_database.cursor()
        
        if self.entry_fname == "" or self.entry_lname == "" or self.entry_address == "" or self.entry_account_num == "" or self.entry_ifsc == "":
            messagebox.showinfo("Empty Fields", "Please fill out all fields given.")
        
        self.email_re = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
        self.email_match = bool(re.search(self.email_re, self.entry_email.get()))
            
        if not self.email_match:
            messagebox.showinfo("Invalid Email", "Email is not valid and does not match " +
                                    "standard email address format.")
            self.entry_email.delete(0, END)
        
        if self.account_word == "Account Number:":
            self.ifsc_re = re.compile(r"^[A-Za-z]{4}0[A-Z0-9a-z]{6}$")
            self.ifsc_match = bool(re.search(self.ifsc_re, self.entry_ifsc.get()))
            
            if not self.ifsc_match:
                messagebox.showinfo("Invalids IFSC code", "The IFSC code you have entered is not " +
                                    "valid and does not follow standard IFSC code format.")
                self.entry_ifsc.delete(0, END)
                
            self.account_number_re = re.compile(r"^\w{1,17}$")
            self.account_num_match = bool(re.search(self.account_number_re,
                                                    self.entry_account_num.get()))
            
            if not self.account_num_match:
                messagebox.showinfo("Invalids account number", "The account number you have" +
                                    " entered is not valid and does not follow standard account" +
                                    " number format.")
                self.entry_account_num.delete(0, END)
                
            if self.email_match and self.ifsc_match:
                messagebox.showinfo("Data saved", "Database connection successful. Data stored away safely.")
                messagebox.showinfo("Saved to database", "Database:\customer-pay.db\nCreate without error.")
                messagebox.showinfo("Thank you", f"""Thank you for signing up at SmartX. Please keep sensitive
information to yourself and please do not share with others.""")                             

                # Add tables to database.
                cursor.execute("""INSERT INTO customer_pay VALUES
                               (:first_name,  :last_name, :email_address, :payment_method, :address, ifsc_code, account_number)""",
                               {
                                    "first_name": self.entry_fname.get(),
                                    "last_name": self.lname.get(),
                                    "email_address": self.entry_email.get(),
                                    "payment_method": self.store_cbx_pay.get(),
                                    "address": self.entry_address.get(),
                                    "ifsc_code": self.entry_ifsc.get(),
                                    "account_number": self.entry_account_num.get()
                                    
                                })
                
                # Commit changes.
                connect_database.commit()
                
                # Close connection.
                connect_database.close()
            

        if self.account_word == "Paypal Email:":
            self.paypal_email_match = bool(re.search(self.email_re, self.entry_account_num.get()))
            if not self.paypal_email_match:
                messagebox.showinfo("Invalid Paypal Email", "Paypal Email is not valid and does not match " +
                                    "standard email address format.")
                
            if self.paypal_email_match and self.email_match:
                messagebox.showinfo("Data saved", "Database connection successful. Data stored away safely.")
                messagebox.showinfo("Saved to database", "Database:\customer-pay.db\nCreate without error.")
                messagebox.showinfo("Thank you", f"""Thank you for signing up at SmartX. Please keep sensitive
information to yourself and please do not share with others.""")
                
                # Add tables to database.
                cursor.execute("""INSERT INTO customer_pay VALUES
                               (:first_name,  :last_name, :email_address, :payment_method, :address, ifsc_code, account_number)""",
                               {
                                    "first_name": self.entry_fname.get(),
                                    "last_name": self.lname.get(),
                                    "email_address": self.entry_email.get(),
                                    "payment_method": self.store_cbx_pay.get(),
                                    "address": self.entry_address.get(),
                                    "ifsc_code": self.entry_ifsc.get(),
                                    "account_number": self.entry_account_num.get()
                                    
                                })
    
    
crm_pay = CustomerPayCRM()

root.mainloop()