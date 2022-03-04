from tkinter import *
from tkinter import ttk
from DAO_Module.CustomerDAO import CustomerDAO
from Data_functions import display_customers_data
from Models import Customer

class CustomersFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, master=root, width=780, height=450, background="red", highlightbackground="black", highlightthickness=3)
        # SECTION STYLE OF TREEVIEW DEVICES
        ## Creation of the style
        self.style = ttk.Style()
        ## Definition of the style to be used
        self.style.theme_use("default")
        ## Configuration of the style
        self.style.configure("Treeview",
            background="red",
            foreground="white",
            fieldbackground="red",
            font="Sans-Serif 13 bold"
        )
        ## Configuring the style at the selection level
        self.style.map("Treeview",
            background=[("selected", "lightpink")],
            foreground=[("selected", "black")]
        )
        # END SECTION STYLE TREEVIEW DEVICES

        ## Creation of the treeview frame
        self.treeFrame = Frame(self)
        self.treeFrame.grid(row=0, column=0, columnspan=9, padx=5, pady=5)

        # SECTION SCROLLBAR
        self.scroll = Scrollbar(self.treeFrame)
        self.scroll.pack(side=RIGHT, fill=Y)
        # END SECTION SCROLLBAR

        # SECTION TREEVIEW DEVICES
        ## Creation of the Treeview and configuration of the scrollbar
        self.treeView = ttk.Treeview(self.treeFrame, yscrollcommand=self.scroll.set)
        self.treeView.pack()
        self.scroll.config(command=self.treeView.yview)
        ## Definition of columns
        self.treeView["columns"] = ("ID", "Company", "Street", "Location", "Postal Code", "Phone", "Email", "Name", "Surname")
        columns = ["ID", "Company", "Street", "Location", "Postal Code", "Phone", "Email", "Name", "Surname"]
        ## Formatting columns
        self.treeView.column("#0", width=0,stretch=NO)
        self.treeView.column(columns[0], anchor=CENTER, minwidth=20, width=20)
        for i in range(1, len(columns)):
            self.treeView.column(columns[i], anchor=W, minwidth=100, width=100)
        ## Creation of headings
        self.treeView.heading("#0", text="")
        self.treeView.heading(columns[0], text=columns[0], anchor=CENTER)
        for i in range(1, len(columns)):
            self.treeView.heading(columns[i], text=columns[i], anchor=W)
        ## Adding data
        display_customers_data(self.treeView)
        # END SECTION TREEVIEW DEVICES

        # BUTTON SECTION DEVICES
        self.registerCustomerButton = Button(self, text="Register", command=self.registerCustomer, background="green", foreground="white", font="Sans-Serif 15 bold")
        self.registerCustomerButton.grid(row=1, column=1, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)
        self.registerDeviceButton = Button(self, text="Register Device", command=None, background="green", foreground="white", font="Sans-Serif 15 bold")
        self.registerDeviceButton.grid(row=1, column=4, columnspan=3, padx=10, pady=10, ipadx=5, ipady=5)
        self.reloadButton = Button(self, text="Reload", command=self.reload, background="yellow", foreground="black", font="Sans-Serif 15 bold")
        self.reloadButton.grid(row=1, column=3, padx=10, pady=10, ipadx=5, ipady=5)
        self.deleteCustomerButton = Button(self, text="Delete", command=self.deleteCustomer, background="darkred", foreground="white", font="Sans-Serif 15 bold")
        self.deleteCustomerButton.grid(row=1, column=7, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)
        # END BUTTON SECTION DEVICES


    def __saveCustomerInformation(self):
        company = self.companyEntry.get()
        street = self.streetEntry.get()
        location = self.locationEntry.get()
        postal_code = self.postalEntry.get()
        phone = self.phoneEntry.get()
        email = self.emailEntry.get()
        name = self.nameEntry.get()
        surname =  self.surnameEntry.get()
        customer = Customer(
            name.capitalize(), 
            surname.capitalize(), 
            email.lower(), 
            phone, 
            company, 
            street.capitalize(), 
            location.capitalize(), 
            postal_code)
        if (phone != "" and name != "" and surname != "" and email != "" and postal_code != "" and company != "" and street != "" and location != ""):
            try:
                phone = int(phone)
            except:
                err = 1
            else:
                err = 0
            if (err == 1 or len(str(phone)) < 9):
                self.message.configure(text="The phone number is invalid: It must be a set of at least 9 digits !")
            else:
                customerDAO = CustomerDAO()
                customerDAO.register_customer(customer)
                print("Saved !")
                self.companyEntry.config(bg="green")
                self.streetEntry.config(bg="green")
                self.locationEntry.config(bg="green")
                self.postalEntry.config(bg="green")
                self.phoneEntry.config(bg="green")
                self.emailEntry.config(bg="green")
                self.nameEntry.config(bg="green")
                self.surnameEntry.config(bg="green")
                self.window.after(1000, self.window.destroy)
        else:
            self.message.configure(text="All information must be provided !")
    
    
    def registerCustomer(self):
        self.window = Tk()
        self.window.title("Customer Registration")
        frame = Frame(self.window, background="lightpink", height=800, width=700, highlightbackground="black", highlightthickness=3)
        frame.pack(ipadx=5, ipady=20)
        Label(frame, text="Customer Registration", background="red", foreground="white", highlightbackground="black", highlightthickness=3,
                         width=40, height=3, font="sans-serif 18 bold").grid(row=0, column=0, padx=20, pady=20)
        formFrame = Frame(frame,  width=600, height=600, background="red", highlightbackground="black", highlightthickness=3)
        formFrame.grid(row=1, column=0, padx=10, pady=10)
        Label(formFrame, text="Company*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=0, padx=20, pady=10, sticky=W)
        self.companyEntry = Entry(formFrame, width=50)
        self.companyEntry.grid(row=0, column=1, padx=20)
        Label(formFrame, text="Street*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=1, padx=20, pady=10, sticky=W)
        self.streetEntry = Entry(formFrame, width=50)
        self.streetEntry.grid(row=1, column=1, padx=20)
        Label(formFrame, text="Location*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=2, padx=20, pady=10, sticky=W)
        self.locationEntry = Entry(formFrame, width=50)
        self.locationEntry.grid(row=2, column=1, padx=20)
        Label(formFrame, text="Postal Code*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=3, padx=20, pady=10, sticky=W)
        self.postalEntry = Entry(formFrame, width=50)
        self.postalEntry.grid(row=3, column=1, padx=20)
        Label(formFrame, text="Phone*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=4, padx=20, pady=10, sticky=W)
        self.phoneEntry = Entry(formFrame, width=50)
        self.phoneEntry.grid(row=4, column=1, padx=20)
        Label(formFrame, text="Email*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=5, padx=20, pady=10, sticky=W)
        self.emailEntry = Entry(formFrame, width=50)
        self.emailEntry.grid(row=5, column=1, padx=20)
        Label(formFrame, text="Name*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=6, padx=20, pady=10, sticky=W)
        self.nameEntry = Entry(formFrame, width=50)
        self.nameEntry.grid(row=6, column=1, padx=20)
        Label(formFrame, text="Surname*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=7, padx=20, pady=10, sticky=W)
        self.surnameEntry = Entry(formFrame, width=50)
        self.surnameEntry.grid(row=7, column=1, padx=20)

        self.message = Label(formFrame, text="", font="sans-serif 10", foreground="black", background="red")
        self.message.grid(row=8, column=1, padx=5, pady=5)
        Button(formFrame, text="Save", command=self.__saveCustomerInformation, width=10, background="green", foreground="white", font="Sans-Serif 15 bold").grid(row=9, column=0, padx=30, pady=20)
        Button(formFrame, text="Cancel", command=self.window.destroy, width=10, background="darkred", foreground="white", font="Sans-Serif 15 bold").grid(row=9, column=1, padx=10, pady=20)
        self.window.mainloop()


    def deleteCustomer(self):
        selected = self.treeView.focus()
        values = self.treeView.item(selected, "values")
        customerDAO = CustomerDAO()
        customerDAO.delete_customer(int(values[0]))
        self.reload()


    def reload(self):
        self.treeFrame.destroy()
        self.treeFrame = Frame(self)
        self.treeFrame.grid(row=0, column=0, columnspan=9, padx=5, pady=5)
        self.scroll = Scrollbar(self.treeFrame)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.treeView = ttk.Treeview(self.treeFrame, yscrollcommand=self.scroll.set)
        self.treeView.pack()
        self.scroll.config(command=self.treeView.yview)
        self.treeView["columns"] = ("ID", "Company", "Street", "Location", "Postal Code", "Phone", "Email", "Name", "Surname")
        columns = ["ID", "Company", "Street", "Location", "Postal Code", "Phone", "Email", "Name", "Surname"]
        self.treeView.column("#0", width=0,stretch=NO)
        self.treeView.column(columns[0], anchor=CENTER, minwidth=20, width=20)
        for i in range(1, len(columns)):
            self.treeView.column(columns[i], anchor=W, minwidth=100, width=100)
        
        self.treeView.heading("#0", text="")
        self.treeView.heading(columns[0], text=columns[0], anchor=CENTER)
        for i in range(1, len(columns)):
            self.treeView.heading(columns[i], text=columns[i], anchor=W)
            
        display_customers_data(self.treeView)

