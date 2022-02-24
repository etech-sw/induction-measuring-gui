from tkinter import *
from tkinter import ttk
from Button_functions import registerCustomer, registerDevice
from Data_functions import *

# Fonction qui vide le frame
def clear_frame():
    for widgets in secondFrame.winfo_children():
        widgets.destroy()


def homePage():
    clear_frame()
    homeButton.configure(background="deepskyblue")
    customerButton.configure(background="red")
    deviceButton.configure(background="red")
    measureButton.configure(background="red")
    titleLabel.configure(text="Home Page")
    # HOME FRAME
    homeTitleFrame = Label(secondFrame, text="Last edit...", background="red", foreground="white", font="Sans-Serif 20 ")
    homeTitleFrame.grid(row=0, column=0, columnspan=3, padx=10, pady=20)

    ## CUSTOMER COLUMN
    customersColumn = Label(secondFrame, text="Customers", width=20, background="red", foreground="white", font="Sans-Serif 15 bold underline")
    customersColumn.grid(row=1, column=0, padx=5, pady=10, sticky=W)
    
    display_last_customers(secondFrame)
    ## CUSTOMER COLUMN END

    ## DEVICE COLOUMN
    devicesColumn = Label(secondFrame, text="Devices", width=20, background="red", foreground="white", font="Sans-Serif 15 bold underline")
    devicesColumn.grid(row=1, column=1, padx=5, pady=10)
    
    display_last_devices(secondFrame)
    ## DEVICE COLUMN END

    measuresColumn = Label(secondFrame, text="Measures", background="red", width=20, foreground="white", font="Sans-Serif 15 bold underline")
    measuresColumn.grid(row=1, column=2, padx=5, pady=10)
    # END HOME FRAME


def customerPage():

    # Fonction qui supprime un client
    def deleteCustomer():
        selected = treeView.focus()
        values = treeView.item(selected, "values")
        customerDAO = CustomerDAO()
        customerDAO.delete_customer(int(values[0]))
        customerPage()


    clear_frame()
    homeButton.configure(background="red")
    customerButton.configure(background="deepskyblue")
    deviceButton.configure(background="red")
    measureButton.configure(background="red")
    titleLabel.configure(text="Customers Page")

    # SECTION STYLE OF TREEVIEW CUSTOMERS
    ## Creation du style
    style = ttk.Style()
    ## Definition du theme a utiliser
    style.theme_use("default")
    ## Configuration du style
    style.configure("Treeview",
        background="red",
        foreground="white",
        fieldbackground="red",
        font="Sans-Serif 13 bold"
    )
    ## Configuration du style au niveau des selections
    style.map("Treeview",
       background=[("selected", "lightpink")],
       foreground=[("selected", "black")]
    )
    # END SECTION STYLE TREEVIEW CUSTOMERS
    
    ## Creation du frame de la treeView
    treeFrame = Frame(secondFrame)
    treeFrame.grid(row=0, column=0, columnspan=9, padx=5, pady=5)

    # SECTION SCROLLBAR
    scroll = Scrollbar(treeFrame)
    scroll.pack(side=RIGHT, fill=Y)
    # END SECTION SCROLLBAR

    # SECTION TREEVIEW CUSTOMERS
    ## Creation du Treeview et configuration du scrollbar
    treeView = ttk.Treeview(treeFrame, yscrollcommand=scroll.set)
    treeView.pack()
    scroll.config(command=treeView.yview)
    ## Definition des colonnes
    treeView["columns"] = ("ID", "Company", "Street", "Location", "Postal Code", "Phone", "Email", "Name", "Surname")
    columns = ["ID", "Company", "Street", "Location", "Postal Code", "Phone", "Email", "Name", "Surname"]
    ## Formatage des colonnes
    treeView.column("#0", width=0,stretch=NO)
    treeView.column(columns[0], anchor=CENTER, minwidth=20, width=20)
    for i in range(1, len(columns)):
        treeView.column(columns[i], anchor=W, minwidth=100, width=100)
    ## Creation des rubriques
    treeView.heading("#0", text="")
    treeView.heading(columns[0], text=columns[0], anchor=CENTER)
    for i in range(1, len(columns)):
        treeView.heading(columns[i], text=columns[i], anchor=W)
    ## Ajout des donnees
    display_customers_data(treeView)

    # END SECTION TREEVIEW CUSTOMERS

    # BUTTON SECTION CUSTOMERS
    registerCustomerButton = Button(secondFrame, text="Register", command=registerCustomer, background="green", foreground="white", font="Sans-Serif 15 bold")
    registerCustomerButton.grid(row=1, column=1, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)
    
    registerDeviceButton = Button(secondFrame, text="Register Device", command=registerDevice, background="green", foreground="white", font="Sans-Serif 15 bold")
    registerDeviceButton.grid(row=1, column=4, columnspan=3, padx=10, pady=10, ipadx=5, ipady=5)

    reloadButton = Button(secondFrame, text="Reload", command=customerPage, background="yellow", foreground="black", font="Sans-Serif 15 bold")
    reloadButton.grid(row=1, column=3, padx=10, pady=10, ipadx=5, ipady=5)

    deleteCustomerButton = Button(secondFrame, text="Delete", command=deleteCustomer, background="darkred", foreground="white", font="Sans-Serif 15 bold")
    deleteCustomerButton.grid(row=1, column=7, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)
    # END BUTTON SECTION CUSTOMERS


def devicePage():

    # Fonction qui supprime un dispositif
    def deleteDevice():
        selected = treeView.focus()
        values = treeView.item(selected, "values")
        deviceDAO = DeviceDAO()
        deviceDAO.delete_device(int(values[0]))
        devicePage()


    clear_frame()
    homeButton.configure(background="red")
    customerButton.configure(background="red")
    deviceButton.configure(background="deepskyblue")
    measureButton.configure(background="red")
    titleLabel.configure(text="Devices Pages")

     # SECTION STYLE OF TREEVIEW DEVICES
    ## Creation du style
    style = ttk.Style()
    ## Definition du theme a utiliser
    style.theme_use("default")
    ## Configuration du style
    style.configure("Treeview",
        background="red",
        foreground="white",
        fieldbackground="red",
        font="Sans-Serif 13 bold"
    )
    ## Configuration du style au niveau des selections
    style.map("Treeview",
       background=[("selected", "lightpink")],
       foreground=[("selected", "black")]
    )
    # END SECTION STYLE TREEVIEW DEVICES
    
    ## Creation du frame de la treeView
    treeFrame = Frame(secondFrame)
    treeFrame.grid(row=0, column=0, columnspan=9, padx=5, pady=5)

    # SECTION SCROLLBAR
    scroll = Scrollbar(treeFrame)
    scroll.pack(side=RIGHT, fill=Y)
    # END SECTION SCROLLBAR

    # SECTION TREEVIEW DEVICES
    ## Creation du Treeview et configuration du scrollbar
    treeView = ttk.Treeview(treeFrame, yscrollcommand=scroll.set)
    treeView.pack()
    scroll.config(command=treeView.yview)
    ## Definition des colonnes
    treeView["columns"] = ("ID", "Device Manufacturer", "Type", "Inductance", "Dimensions", "Name", "Surname")
    columns = ["ID", "Device Manufacturer", "Type", "Inductance", "Dimensions", "Name", "Surname"]
    ## Formatage des colonnes
    treeView.column("#0", width=0,stretch=NO)
    treeView.column(columns[0], anchor=CENTER, minwidth=20, width=20)
    for i in range(1, len(columns)):
        treeView.column(columns[i], anchor=W, minwidth=120, width=120)
    ## Creation des rubriques
    treeView.heading("#0", text="")
    treeView.heading(columns[0], text=columns[0], anchor=CENTER)
    for i in range(1, len(columns)):
        treeView.heading(columns[i], text=columns[i], anchor=W)
    ## Ajout des donnees
    display_devices_data(treeView)

    # END SECTION TREEVIEW DEVICES

    # BUTTON SECTION DEVICES
    registerDeviceButton = Button(secondFrame, text="Register", command=registerDevice, background="green", foreground="white", font="Sans-Serif 15 bold")
    registerDeviceButton.grid(row=1, column=1, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)
    
    registerCustomerButton = Button(secondFrame, text="Register Customer", command=registerCustomer, background="green", foreground="white", font="Sans-Serif 15 bold")
    registerCustomerButton.grid(row=1, column=4, columnspan=3, padx=10, pady=10, ipadx=5, ipady=5)

    reloadButton = Button(secondFrame, text="Reload", command=devicePage, background="yellow", foreground="black", font="Sans-Serif 15 bold")
    reloadButton.grid(row=1, column=3, padx=10, pady=10, ipadx=5, ipady=5)

    deleteDeviceButton = Button(secondFrame, text="Delete", command=deleteDevice, background="darkred", foreground="white", font="Sans-Serif 15 bold")
    deleteDeviceButton.grid(row=1, column=7, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)
    # END BUTTON SECTION DEVICES


def mesurePage():
    clear_frame()
    homeButton.configure(background="red")
    customerButton.configure(background="red")
    deviceButton.configure(background="red")
    measureButton.configure(background="deepskyblue")
    titleLabel.configure(text="Measures Page")


###     MAIN CODE       ###
window = Tk()
window.title("GUI Interface")
mainFrame = Frame(window, height=800, width=800, background="lightpink", highlightbackground="black", highlightthickness=3)
mainFrame.pack(ipadx=5, ipady=20)

# LABEL SECTION
menuLabel = Label(mainFrame, text="Menu", width=10, height=3, background="red", foreground="white", highlightbackground="black",
                    highlightthickness=3, font="Sans-Serif 15 bold")
menuLabel.grid(row=0, column=0, padx=40, pady=20)

titleLabel = Label(mainFrame, text="Home Page", width=65, height=3, background="red", foreground="white", highlightbackground="black", 
                    highlightthickness=3, font="Sans-Serif 16 bold")
titleLabel.grid(row=0, column=1, padx=5, pady=20)

# END LABEL SECTION

# BUTTON SECTION
homeButton = Button(mainFrame, text="Home", command=homePage, background="deepskyblue", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font="Sans-Serif 15 bold")
homeButton.grid(row=1, column=0)

customerButton = Button(mainFrame, text="+ Customer", command=customerPage, background="red", foreground="white", width=10, font="Sans-Serif 15 bold")
customerButton.grid(row=2, column=0, padx=5, pady=10)

deviceButton = Button(mainFrame, text="+ Device", command=devicePage, background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font="Sans-Serif 15 bold")
deviceButton.grid(row=3, column=0, padx=5, pady=10)

measureButton = Button(mainFrame, text="Measure", command=mesurePage, background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font="Sans-Serif 15 bold")
measureButton.grid(row=4, column=0, padx=5, pady=10)

settingButton = Button(mainFrame, text="Setting", background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font="Sans-Serif 15 bold")
settingButton.grid(row=7, column=0, padx=5, pady=10)

# END BUTTON SECTION

# HOME FRAME
secondFrame = Frame(mainFrame, width=780, height=450, background="red", highlightbackground="black", highlightthickness=3)
secondFrame.grid(row=1, column=1, rowspan=7, ipadx=5, ipady=5, padx=5)

homePage()
# END HOME FRAME

window.mainloop()
