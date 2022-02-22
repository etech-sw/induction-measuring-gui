from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont
from DAO_Module.CustomerDAO import CustomerDAO
from DAO_Module.DeviceDAO import DeviceDAO

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
    homeTitleFrame = Label(secondFrame, text="Last edit...", background="red", foreground="white", font=tkFont.Font(family="Sans Serif", size=20, weight="bold"))
    homeTitleFrame.grid(row=0, column=0, columnspan=3, padx=10, pady=20)

        ## CUSTOMER COLUMN
    customersColumn = Label(secondFrame, text="Customers", width=20, background="red", foreground="white", font=tkFont.Font(family="Sans Serif", size=15, weight="bold", underline=True))
    customersColumn.grid(row=1, column=0, padx=5, pady=10, sticky=W)
    # Initialisation et recuperation de la BD
    customerDAO = CustomerDAO()
    customers = customerDAO.get_last_customers()
    compt, row = 1, 2
    # Affichage sur l'interface
    for customer in customers:
        Label(secondFrame, text=str(compt)+"."+customer[1], justify="right", background="red", foreground="white", font=tkFont.Font(family="Sans Serif", size=10, weight="bold")).grid(row=row, column=0, pady=10)
        compt += 1
        row += 1
        if (compt > 5):
            break
        ## CUSTOMER COLUMN END

        ## DEVICE COLOUMN
    devicesColumn = Label(secondFrame, text="Devices", width=20, background="red", foreground="white", font=tkFont.Font(family="Sans Serif", size=15, weight="bold", underline=True))
    devicesColumn.grid(row=1, column=1, padx=5, pady=10)
    # Initialisation et recuperation de la BD
    deviceDAO = DeviceDAO()
    devices = deviceDAO.get_last_devices()
    compt, row = 1, 2
    # Affichage sur l'interface
    for device in devices:
        Label(secondFrame, text=str(compt)+"."+device[1], justify="right", background="red", foreground="white", font=tkFont.Font(family="Sans Serif", size=10, weight="bold")).grid(row=row, column=1, pady=10)
        compt += 1
        row += 1
        if (compt > 5):
            break
        ## DEVICE COLUMN END

    measuresColumn = Label(secondFrame, text="Measures", background="red", width=20, foreground="white", font=tkFont.Font(family="Sans Serif", size=15, weight="bold", underline=True))
    measuresColumn.grid(row=1, column=2, padx=5, pady=10)
    # END HOME FRAME


def customerPage():
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
        fieldbackground="red"
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
    customerDAO = CustomerDAO()
    customers = customerDAO.get_all_customers()
    id = 0
    for customer in customers:
        treeView.insert(parent="", index="end", iid=id, text="", values=(customer[0], customer[5], customer[6], customer[7], customer[8], customer[4], customer[3], customer[1], customer[2]))
        id += 1

    # END SECTION TREEVIEW CUSTOMERS

    # BUTTON SECTION CUSTOMERS
    registerCustomerButton = Button(secondFrame, text="Register", background="green", foreground="white", font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
    registerCustomerButton.grid(row=1, column=1, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)

    registerDeviceButton = Button(secondFrame, text="Register Device", background="green", foreground="white", font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
    registerDeviceButton.grid(row=1, column=4, columnspan=3, padx=10, pady=10, ipadx=5, ipady=5)

    deleteCustomerButton = Button(secondFrame, text="Delete", background="darkred", foreground="white", font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
    deleteCustomerButton.grid(row=1, column=7, columnspan=2, padx=10, pady=10, ipadx=5, ipady=5)
    # END BUTTON SECTION CUSTOMERS


def devicePage():
    clear_frame()
    homeButton.configure(background="red")
    customerButton.configure(background="red")
    deviceButton.configure(background="deepskyblue")
    measureButton.configure(background="red")
    titleLabel.configure(text="Devices Pages")


def mesurePage():
    clear_frame()
    homeButton.configure(background="red")
    customerButton.configure(background="red")
    deviceButton.configure(background="red")
    measureButton.configure(background="deepskyblue")
    titleLabel.configure(text="Measures Page")


###     MAIN CODE       ###
window = Tk()
mainFrame = Frame(window, height=800, width=800, background="lightpink", highlightbackground="black", highlightthickness=3)
mainFrame.pack(ipadx=5, ipady=20)

# LABEL SECTION
menuLabel = Label(mainFrame, text="Menu", width=10, height=3, background="red", foreground="white", highlightbackground="black",
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
menuLabel.grid(row=0, column=0, padx=40, pady=20)

titleLabel = Label(mainFrame, text="Home Page", width=65, height=3, background="red", foreground="white", highlightbackground="black", 
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
titleLabel.grid(row=0, column=1, padx=5, pady=20)

# END LABEL SECTION

# BUTTON SECTION
homeButton = Button(mainFrame, text="Home", command=homePage, background="deepskyblue", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
homeButton.grid(row=1, column=0)

customerButton = Button(mainFrame, text="+ customer", command=customerPage, background="red", foreground="white", width=10, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
customerButton.grid(row=2, column=0, padx=5, pady=10)

deviceButton = Button(mainFrame, text="+ device", command=devicePage, background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
deviceButton.grid(row=3, column=0, padx=5, pady=10)

measureButton = Button(mainFrame, text="Measure", command=mesurePage, background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
measureButton.grid(row=4, column=0, padx=5, pady=10)

settingButton = Button(mainFrame, text="Setting", background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
settingButton.grid(row=7, column=0, padx=5, pady=10)

# END BUTTON SECTION

# HOME FRAME
secondFrame = Frame(mainFrame, width=780, height=450, background="red", highlightbackground="black", highlightthickness=3)
secondFrame.grid(row=1, column=1, rowspan=7, ipadx=5, ipady=5, padx=5)

homePage()
# END HOME FRAME

window.mainloop()
