from tkinter import *
from tkinter import ttk
from DAO_Module.CustomerDAO import CustomerDAO
from DAO_Module.DeviceDAO import DeviceDAO
from Data_functions import display_devices_data
from Models import Customer, Device

class DevicesFrame(Frame):
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
        self.treeView["columns"] = ("ID", "Device Manufacturer", "Type", "Inductance", "Dimensions", "Name", "Surname")
        columns = ["ID", "Device Manufacturer", "Type", "Inductance", "Dimensions", "Name", "Surname"]
        ## Formatting columns
        self.treeView.column("#0", width=0,stretch=NO)
        self.treeView.column(columns[0], anchor=CENTER, minwidth=30, width=30)
        for i in range(1, len(columns)):
            self.treeView.column(columns[i], anchor=W, minwidth=130, width=130)
        ## Creation of headings
        self.treeView.heading("#0", text="")
        self.treeView.heading(columns[0], text=columns[0], anchor=CENTER)
        for i in range(1, len(columns)):
            self.treeView.heading(columns[i], text=columns[i], anchor=W)
        ## Adding data
        display_devices_data(self.treeView)
        # END SECTION TREEVIEW DEVICES

        # BUTTON SECTION DEVICES
        self.registerDeviceButton = Button(self, text="Register", command=self.registerDevice, background="green", foreground="white", font="Sans-Serif 15 bold")
        self.registerDeviceButton.grid(row=1, column=0, padx=10, pady=10, ipadx=5, ipady=5)
        self.updateDeviceButton = Button(self, text="Update", command=self.updateDevice, background="green", foreground="white", font="Sans-Serif 15 bold")
        self.updateDeviceButton.grid(row=1, column=1, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)
        self.registerCustomerButton = Button(self, text="Register Customer", command=self.registerCustomer, background="green", foreground="white", font="Sans-Serif 15 bold")
        self.registerCustomerButton.grid(row=1, column=4, columnspan=3, padx=10, pady=10, ipadx=5, ipady=5)
        self.reloadButton = Button(self, text="Reload", command=self.reload, background="yellow", foreground="black", font="Sans-Serif 15 bold")
        self.reloadButton.grid(row=1, column=3, padx=10, pady=10, ipadx=5, ipady=5)
        self.deleteDeviceButton = Button(self, text="Delete", command=self.deleteDevice, background="darkred", foreground="white", font="Sans-Serif 15 bold")
        self.deleteDeviceButton.grid(row=1, column=7, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)
        # END BUTTON SECTION DEVICES

        # Variable permettant de savoir quel option est choisie entre Register et Update
        self.__check = 0

        # Responsive configuration
        for i in range(2):
            Grid.rowconfigure(self, index=i, weight=1)
        for i in range(8):
            Grid.columnconfigure(self, index=i, weight=1)

    def __saveDeviceInformation(self):
        device_manufacturer = self.manufacturerEntry.get()
        type = self.typeEntry.get()
        inductance = self.inductanceEntry.get()
        dimensions = self.dimensionsEntry.get()
        name = self.nameEntry.get()
        surname =  self.surnameEntry.get()
        device = Device(
            device_manufacturer.capitalize(), 
            type.capitalize(), 
            inductance, 
            dimensions, 
            name.capitalize(), 
            surname.capitalize())
        if (device_manufacturer != "" and type != "" and inductance != "" and dimensions != "" and name != "" and surname != ""):
            try:
                inductance = float(inductance)
            except:
                err = 1
            else:
                err = 0
            if (err == 1):
                self.message.configure(text="Enter a numeric for inductance")
            else:
                deviceDAO = DeviceDAO()
                if self.__check == 1:
                    result = deviceDAO.register_device(device)
                else:
                    selected = self.treeView.focus()
                    values = self.treeView.item(selected, "values")
                    result = deviceDAO.update_device(device, int(values[0]))
                if (result):
                    self.manufacturerEntry.config(bg="green")
                    self.typeEntry.config(bg="green")
                    self.inductanceEntry.config(bg="green")
                    self.dimensionsEntry.config(bg="green")
                    self.nameEntry.config(bg="green")
                    self.surnameEntry.config(bg="green")
                    self.window.after(1000, self.window.destroy)
                else:
                    self.message.configure(text="Customer information not found") 
        else:
            self.message.configure(text="All information must be provided !")
        
    
    def registerDevice(self):
        self.__check = 1
        self.window = Tk()
        self.window.title("Device Registration")
        frame = Frame(self.window, background="lightpink", height=780, width=450, highlightbackground="black", highlightthickness=3)
        frame.grid(row=0, column=0, ipadx=5, ipady=20, sticky="nsew")
        ### Responsive configuration for element in window
        Grid.rowconfigure(self.window, index=0, weight=1)
        Grid.columnconfigure(self.window, index=0, weight=1)
        ###
        Label(frame, text="Device Registration", background="red", foreground="white", highlightbackground="black", highlightthickness=3,
                         width=40, height=3, font="sans-serif 18 bold").grid(row=0, column=0, padx=20, pady=20)
        formFrame = Frame(frame,  width=600, height=600, background="red", highlightbackground="black", highlightthickness=3)
        formFrame.grid(row=1, column=0, padx=10, pady=10)
        ### Responsive configuration for element in frame
        Grid.rowconfigure(frame, index=0, weight=1)
        Grid.rowconfigure(frame, index=1, weight=1)
        Grid.columnconfigure(frame, index=0, weight=1)
        ###
        Label(formFrame, text="Device Manufacturer*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=0, padx=20, pady=10, sticky=W)
        self.manufacturerEntry = Entry(formFrame, width=50)
        self.manufacturerEntry.grid(row=0, column=1, padx=20)
        Label(formFrame, text="Type*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=1, padx=20, pady=10, sticky=W)
        self.typeEntry = Entry(formFrame, width=50)
        self.typeEntry.grid(row=1, column=1, padx=20)
        Label(formFrame, text="Inductance*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=2, padx=20, pady=10, sticky=W)
        self.inductanceEntry = Entry(formFrame, width=50)
        self.inductanceEntry.grid(row=2, column=1, padx=20)
        Label(formFrame, text="Dimensions*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=3, padx=20, pady=10, sticky=W)
        self.dimensionsEntry = Entry(formFrame, width=50)
        self.dimensionsEntry.grid(row=3, column=1, padx=20)
        Label(formFrame, text="Name*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=4, padx=20, pady=10, sticky=W)
        self.nameEntry = Entry(formFrame, width=50)
        self.nameEntry.grid(row=4, column=1, padx=20)
        Label(formFrame, text="Surname*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=5, padx=20, pady=10, sticky=W)
        self.surnameEntry = Entry(formFrame, width=50)
        self.surnameEntry.grid(row=5, column=1, padx=20)

        self.message = Label(formFrame, text="", font="sans-serif 10", foreground="black", background="red")
        self.message.grid(row=6, column=1, padx=5, pady=5)
        Button(formFrame, text="Save", command=self.__saveDeviceInformation, width=10, background="green", foreground="white", font="Sans-Serif 15 bold").grid(row=7, column=0, padx=30, pady=20)
        Button(formFrame, text="Cancel", command=self.window.destroy, width=10, background="darkred", foreground="white", font="Sans-Serif 15 bold").grid(row=7, column=1, padx=10, pady=20)
        
        ### Responsive configuration for elements in frame
        for i in range(8):
            Grid.rowconfigure(formFrame, index=i, weight=1)
        for i in range(2):
            Grid.columnconfigure(formFrame, index=i, weight=1)
        ###

        self.window.mainloop()


    def deleteDevice(self):
        selected = self.treeView.focus()
        values = self.treeView.item(selected, "values")
        deviceDAO = DeviceDAO()
        deviceDAO.delete_device(int(values[0]))
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
        self.treeView["columns"] = ("ID", "Device Manufacturer", "Type", "Inductance", "Dimensions", "Name", "Surname")
        columns = ["ID", "Device Manufacturer", "Type", "Inductance", "Dimensions", "Name", "Surname"]
        self.treeView.column("#0", width=0,stretch=NO)
        self.treeView.column(columns[0], anchor=CENTER, minwidth=30, width=30)
        for i in range(1, len(columns)):
            self.treeView.column(columns[i], anchor=W, minwidth=130, width=130)
        
        self.treeView.heading("#0", text="")
        self.treeView.heading(columns[0], text=columns[0], anchor=CENTER)
        for i in range(1, len(columns)):
            self.treeView.heading(columns[i], text=columns[i], anchor=W)
            
        display_devices_data(self.treeView)

    
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
                self.messageCustomer.configure(text="The phone number is invalid: It must be a set of at least 9 digits !")
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
                self.customerWindow.after(1000, self.customerWindow.destroy)
        else:
            self.messageCustomer.configure(text="All information must be provided !")
    
    
    def registerCustomer(self):
        self.customerWindow = Tk()
        self.customerWindow.title("Customer Registration")
        frame = Frame(self.customerWindow, background="lightpink", height=800, width=700, highlightbackground="black", highlightthickness=3)
        frame.grid(row=0, column=0, ipadx=5, ipady=20, sticky="nsew")
        ### Responsive configuration for element in window
        Grid.rowconfigure(self.customerWindow, index=0, weight=1)
        Grid.columnconfigure(self.customerWindow, index=0, weight=1)
        ###
        Label(frame, text="Customer Registration", background="red", foreground="white", highlightbackground="black", highlightthickness=3,
                         width=40, height=3, font="sans-serif 18 bold").grid(row=0, column=0, padx=20, pady=20)
        formFrame = Frame(frame,  width=600, height=600, background="red", highlightbackground="black", highlightthickness=3)
        formFrame.grid(row=1, column=0, padx=10, pady=10)
        ### Responsive configuration for element in frame
        Grid.rowconfigure(frame, index=0, weight=1)
        Grid.rowconfigure(frame, index=1, weight=1)
        Grid.columnconfigure(frame, index=0, weight=1)
        ###
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

        self.messageCustomer = Label(formFrame, text="", font="sans-serif 10", foreground="black", background="red")
        self.messageCustomer.grid(row=8, column=1, padx=5, pady=5)
        Button(formFrame, text="Save", command=self.__saveCustomerInformation, width=10, background="green", foreground="white", font="Sans-Serif 15 bold").grid(row=9, column=0, padx=30, pady=20)
        Button(formFrame, text="Cancel", command=self.customerWindow.destroy, width=10, background="darkred", foreground="white", font="Sans-Serif 15 bold").grid(row=9, column=1, padx=10, pady=20)
        
        ### Responsive configuration for elements in frame
        for i in range(10):
            Grid.rowconfigure(formFrame, index=i, weight=1)
        for i in range(2):
            Grid.columnconfigure(formFrame, index=i, weight=1)
        ###

        self.customerWindow.mainloop()


    def updateDevice(self):
        self.__check = 2
        # Recuperation des donnees du device choisi
        selected = self.treeView.focus()
        if (selected):
            values = self.treeView.item(selected, "values")
            # Affichage pour modification
            self.window = Tk()
            self.window.title("Update Device")
            frame = Frame(self.window, background="lightpink", height=800, width=700, highlightbackground="black", highlightthickness=3)
            frame.grid(row=0, column=0, ipadx=5, ipady=20, sticky="nsew")
            ### Responsive configuration for element in window
            Grid.rowconfigure(self.window, index=0, weight=1)
            Grid.columnconfigure(self.window, index=0, weight=1)
            ###
            Label(frame, text="Update Device Informations", background="red", foreground="white", highlightbackground="black", highlightthickness=3,
                            width=40, height=3, font="sans-serif 18 bold").grid(row=0, column=0, padx=20, pady=20)
            formFrame = Frame(frame,  width=600, height=600, background="red", highlightbackground="black", highlightthickness=3)
            formFrame.grid(row=1, column=0, padx=10, pady=10)
            ### Responsive configuration for element in frame
            Grid.rowconfigure(frame, index=0, weight=1)
            Grid.rowconfigure(frame, index=1, weight=1)
            Grid.columnconfigure(frame, index=0, weight=1)
            ###
            Label(formFrame, text="ID =====> "+values[0], background="red", foreground="white", font="sans-serif 15 bold").grid(row=0, padx=20, pady=10, sticky=W)
            Label(formFrame, text="Device Manufacturer*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=1, padx=20, pady=10, sticky=W)
            self.manufacturerEntry = Entry(formFrame, width=50)
            self.manufacturerEntry.grid(row=1, column=1, padx=20)
            self.manufacturerEntry.delete('0', 'end')
            self.manufacturerEntry.insert('0', values[1])
            Label(formFrame, text="Type*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=2, padx=20, pady=10, sticky=W)
            self.typeEntry = Entry(formFrame, width=50)
            self.typeEntry.grid(row=2, column=1, padx=20)
            self.typeEntry.delete('0', 'end')
            self.typeEntry.insert('0', values[2])
            Label(formFrame, text="Inductance*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=3, padx=20, pady=10, sticky=W)
            self.inductanceEntry = Entry(formFrame, width=50)
            self.inductanceEntry.grid(row=3, column=1, padx=20)
            self.inductanceEntry.delete('0', 'end')
            self.inductanceEntry.insert('0', values[3])
            Label(formFrame, text="Dimensions*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=4, padx=20, pady=10, sticky=W)
            self.dimensionsEntry = Entry(formFrame, width=50)
            self.dimensionsEntry.grid(row=4, column=1, padx=20)
            self.dimensionsEntry.delete('0', 'end')
            self.dimensionsEntry.insert('0', values[4])
            Label(formFrame, text="Name*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=5, padx=20, pady=10, sticky=W)
            self.nameEntry = Entry(formFrame, width=50)
            self.nameEntry.grid(row=5, column=1, padx=20)
            self.nameEntry.delete('0', 'end')
            self.nameEntry.insert('0', values[5])
            Label(formFrame, text="Surname*", background="red", foreground="white", font="sans-serif 15 bold underline").grid(row=6, padx=20, pady=10, sticky=W)
            self.surnameEntry = Entry(formFrame, width=50)
            self.surnameEntry.grid(row=6, column=1, padx=20)
            self.surnameEntry.delete('0', 'end')
            self.surnameEntry.insert('0', values[6])

            self.message = Label(formFrame, text="", font="sans-serif 10", foreground="black", background="red")
            self.message.grid(row=7, column=1, padx=5, pady=5)
            Button(formFrame, text="Update", command=self.__saveDeviceInformation, width=10, background="green", foreground="white", font="Sans-Serif 15 bold").grid(row=8, column=0, padx=30, pady=20)
            Button(formFrame, text="Cancel", command=self.window.destroy, width=10, background="darkred", foreground="white", font="Sans-Serif 15 bold").grid(row=8, column=1, padx=10, pady=20)
            
            ### Responsive configuration for element in form frame
            for i in range(9):
                Grid.rowconfigure(formFrame, index=i, weight=1)
            for i in range(2):
                Grid.columnconfigure(formFrame, index=i, weight=1)
            ###
            
            self.window.mainloop()
        else:
            # Affichage en cas de non selection de customer
            self.window = Tk()
            self.window.title("Error")
            Label(self.window, text="Select a device to update !", foreground="red", width=40, height=3, font="sans-serif 18 bold").pack(padx=20, pady=20)

