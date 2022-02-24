from tkinter import *
from DAO_Module.CustomerDAO import CustomerDAO
from DAO_Module.DeviceDAO import DeviceDAO
from Models import Customer, Device

def registerCustomer():

    def save():
        company = companyEntry.get()
        street = streetEntry.get()
        location = locationEntry.get()
        postal_code = postalEntry.get()
        phone = phoneEntry.get()
        email = emailEntry.get()
        name = nameEntry.get()
        surname =  surnameEntry.get()
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
                message.configure(text="The phone number is invalid: It must be a set of at least 9 digits !")
            else:
                customerDAO = CustomerDAO()
                customerDAO.register_customer(customer)
                print("Saved !")
                companyEntry.config(bg="green")
                streetEntry.config(bg="green")
                locationEntry.config(bg="green")
                postalEntry.config(bg="green")
                phoneEntry.config(bg="green")
                emailEntry.config(bg="green")
                nameEntry.config(bg="green")
                surnameEntry.config(bg="green")
                window.after(1000, window.destroy)
        else:
            message.configure(text="All information must be provided !")
        
        
    window = Tk()
    window.title("Customer Registration")
    frame = Frame(window, background="lightpink", height=800, width=700, highlightbackground="black", highlightthickness=3)
    frame.pack(ipadx=5, ipady=20)
    
    title = Label(frame, text="Customer Registration", background="red", foreground="white", highlightbackground="black", highlightthickness=3,
                         width=40, height=3, font="sans-serif 18 bold")
    title.grid(row=0, column=0, padx=20, pady=20)

    formFrame = Frame(frame,  width=600, height=600, background="red", highlightbackground="black", highlightthickness=3)
    formFrame.grid(row=1, column=0, padx=10, pady=10)
 
    companyLabel = Label(formFrame, text="Company*", background="red", foreground="white", font="sans-serif 15 bold underline")
    companyLabel.grid(row=0, padx=20, pady=10, sticky=W)
    companyEntry = Entry(formFrame, width=50)
    companyEntry.grid(row=0, column=1, padx=20)
    streetLabel = Label(formFrame, text="Street*", background="red", foreground="white", font="sans-serif 15 bold underline")
    streetLabel.grid(row=1, padx=20, pady=10, sticky=W)
    streetEntry = Entry(formFrame, width=50)
    streetEntry.grid(row=1, column=1, padx=20)
    locationLabel = Label(formFrame, text="Location*", background="red", foreground="white", font="sans-serif 15 bold underline")
    locationLabel.grid(row=2, padx=20, pady=10, sticky=W)
    locationEntry = Entry(formFrame, width=50)
    locationEntry.grid(row=2, column=1, padx=20)
    postalLabel = Label(formFrame, text="Postal Code*", background="red", foreground="white", font="sans-serif 15 bold underline")
    postalLabel.grid(row=3, padx=20, pady=10, sticky=W)
    postalEntry = Entry(formFrame, width=50)
    postalEntry.grid(row=3, column=1, padx=20)
    phoneLabel = Label(formFrame, text="Phone*", background="red", foreground="white", font="sans-serif 15 bold underline")
    phoneLabel.grid(row=4, padx=20, pady=10, sticky=W)
    phoneEntry = Entry(formFrame, width=50)
    phoneEntry.grid(row=4, column=1, padx=20)
    emailLabel = Label(formFrame, text="Email*", background="red", foreground="white", font="sans-serif 15 bold underline")
    emailLabel.grid(row=5, padx=20, pady=10, sticky=W)
    emailEntry = Entry(formFrame, width=50)
    emailEntry.grid(row=5, column=1, padx=20)
    nameLabel = Label(formFrame, text="Name*", background="red", foreground="white", font="sans-serif 15 bold underline")
    nameLabel.grid(row=6, padx=20, pady=10, sticky=W)
    nameEntry = Entry(formFrame, width=50)
    nameEntry.grid(row=6, column=1, padx=20)
    surnameLabel = Label(formFrame, text="Surname*", background="red", foreground="white", font="sans-serif 15 bold underline")
    surnameLabel.grid(row=7, padx=20, pady=10, sticky=W)
    surnameEntry = Entry(formFrame, width=50)
    surnameEntry.grid(row=7, column=1, padx=20)

    message = Label(formFrame, text="", font="sans-serif 10", foreground="black", background="red")
    message.grid(row=8, column=1, padx=5, pady=5)
    saveButton = Button(formFrame, text="Save", command=save, width=10, background="green", foreground="white", font="Sans-Serif 15 bold")
    saveButton.grid(row=9, column=0, padx=30, pady=20)
    cancelButton = Button(formFrame, text="Cancel", command=window.destroy, width=10, background="darkred", foreground="white", font="Sans-Serif 15 bold")
    cancelButton.grid(row=9, column=1, padx=10, pady=20)

    window.mainloop()


def registerDevice():
    
    def save():
        device_manufacturer = manufacturerEntry.get()
        type = typeEntry.get()
        inductance = inductanceEntry.get()
        dimensions = dimensionsEntry.get()
        name = nameEntry.get()
        surname =  surnameEntry.get()
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
                message.configure(text="Enter a numeric for inductance")
            else:
                deviceDAO = DeviceDAO()
                result = deviceDAO.register_device(device)
                if (result):
                    print("Saved!")
                    manufacturerEntry.config(bg="green")
                    typeEntry.config(bg="green")
                    inductanceEntry.config(bg="green")
                    dimensionsEntry.config(bg="green")
                    nameEntry.config(bg="green")
                    surnameEntry.config(bg="green")
                    window.after(1000, window.destroy)
                else:
                    message.configure(text="Customer information not found") 
        else:
            message.configure(text="All information must be provided !")
        
        
    window = Tk()
    window.title("Device Registration")
    frame = Frame(window, background="lightpink", height=800, width=700, highlightbackground="black", highlightthickness=3)
    frame.pack(ipadx=5, ipady=20)
    
    title = Label(frame, text="Device Registration", background="red", foreground="white", highlightbackground="black", highlightthickness=3,
                         width=40, height=3, font="sans-serif 18 bold")
    title.grid(row=0, column=0, padx=20, pady=20)

    formFrame = Frame(frame,  width=600, height=600, background="red", highlightbackground="black", highlightthickness=3)
    formFrame.grid(row=1, column=0, padx=10, pady=10)
 
    manufacturerLabel = Label(formFrame, text="Device Manufacturer*", background="red", foreground="white", font="sans-serif 15 bold underline")
    manufacturerLabel.grid(row=0, padx=20, pady=10, sticky=W)
    manufacturerEntry = Entry(formFrame, width=50)
    manufacturerEntry.grid(row=0, column=1, padx=20)
    typeLabel = Label(formFrame, text="Type*", background="red", foreground="white", font="sans-serif 15 bold underline")
    typeLabel.grid(row=1, padx=20, pady=10, sticky=W)
    typeEntry = Entry(formFrame, width=50)
    typeEntry.grid(row=1, column=1, padx=20)
    inductanceLabel = Label(formFrame, text="Inductance*", background="red", foreground="white", font="sans-serif 15 bold underline")
    inductanceLabel.grid(row=2, padx=20, pady=10, sticky=W)
    inductanceEntry = Entry(formFrame, width=50)
    inductanceEntry.grid(row=2, column=1, padx=20)
    dimensionsLabel = Label(formFrame, text="Dimensions*", background="red", foreground="white", font="sans-serif 15 bold underline")
    dimensionsLabel.grid(row=3, padx=20, pady=10, sticky=W)
    dimensionsEntry = Entry(formFrame, width=50)
    dimensionsEntry.grid(row=3, column=1, padx=20)
    nameLabel = Label(formFrame, text="Name*", background="red", foreground="white", font="sans-serif 15 bold underline")
    nameLabel.grid(row=4, padx=20, pady=10, sticky=W)
    nameEntry = Entry(formFrame, width=50)
    nameEntry.grid(row=4, column=1, padx=20)
    surnameLabel = Label(formFrame, text="Surname*", background="red", foreground="white", font="sans-serif 15 bold underline")
    surnameLabel.grid(row=5, padx=20, pady=10, sticky=W)
    surnameEntry = Entry(formFrame, width=50)
    surnameEntry.grid(row=5, column=1, padx=20)

    message = Label(formFrame, text="", font="sans-serif 10", foreground="black", background="red")
    message.grid(row=6, column=1, padx=5, pady=5)
    saveButton = Button(formFrame, text="Save", command=save, width=10, background="green", foreground="white", font="Sans-Serif 15 bold")
    saveButton.grid(row=7, column=0, padx=30, pady=20)
    cancelButton = Button(formFrame, text="Cancel", command=window.destroy, width=10, background="darkred", foreground="white", font="Sans-Serif 15 bold")
    cancelButton.grid(row=7, column=1, padx=10, pady=20)

    window.mainloop()