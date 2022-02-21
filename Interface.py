from tkinter import *
import tkinter.font as tkFont
from DAO_Module.CustomerDAO import CustomerDAO
from DAO_Module.DeviceDAO import DeviceDAO

# Fonction qui vide le frame
def clear_frame():
    for widgets in secondFrame.winfo_children():
        widgets.destroy()


def homePage(event):
    homeButton.configure(background="deepskyblue")
    customerButton.configure(background="red")
    deviceButton.configure(background="red")
    measureButton.configure(background="red")
    titleLabel.configure(text="Home Page")
    # HOME FRAME
    homeTitleFrame = Label(secondFrame, text="Last edit...", background="red", foreground="white", font=tkFont.Font(family="Sans Serif", size=20, weight="bold"))
    homeTitleFrame.grid(row=0, column=0, columnspan=3, padx=10, pady=20)

        ## CUSTOMER COLUMN
    customersColumn = Label(secondFrame, text="Customers", underline=8, width=20, background="red", foreground="white", font=tkFont.Font(family="Sans Serif", size=15, weight="bold", underline=True))
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


def customerPage(event):
    clear_frame()
    homeButton.configure(background="red")
    customerButton.configure(background="deepskyblue")
    deviceButton.configure(background="red")
    measureButton.configure(background="red")
    titleLabel.configure(text="Customers Page")


def devicePage(event):
    clear_frame()
    homeButton.configure(background="red")
    customerButton.configure(background="red")
    deviceButton.configure(background="deepskyblue")
    measureButton.configure(background="red")
    titleLabel.configure(text="Devices Pages")


def mesurePage(event):
    clear_frame()
    homeButton.configure(background="red")
    customerButton.configure(background="red")
    deviceButton.configure(background="red")
    measureButton.configure(background="deepskyblue")
    titleLabel.configure(text="Measures Page")


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
homeButton = Button(mainFrame, text="Home", background="deepskyblue", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
homeButton.grid(row=1, column=0)
homeButton.bind("<Button-1>", homePage)

customerButton = Button(mainFrame, text="+ customer", background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
customerButton.grid(row=2, column=0, padx=5, pady=10)
customerButton.bind("<Button-1>", customerPage)

deviceButton = Button(mainFrame, text="+ device", background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
deviceButton.grid(row=3, column=0, padx=5, pady=10)
deviceButton.bind("<Button-1>", devicePage)

measureButton = Button(mainFrame, text="Measure", background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
measureButton.grid(row=4, column=0, padx=5, pady=10)
measureButton.bind("<Button-1>", mesurePage)

settingButton = Button(mainFrame, text="Setting", background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
settingButton.grid(row=7, column=0, padx=5, pady=10)

# END BUTTON SECTION

# HOME FRAME
secondFrame = Frame(mainFrame, width=780, height=450, background="red", highlightbackground="black", highlightthickness=3)
secondFrame.grid(row=1, column=1, rowspan=7, ipadx=5, ipady=10, padx=5)

homeTitleFrame = Label(secondFrame, text="Last edit...", background="red", foreground="white", font=tkFont.Font(family="Sans Serif", size=20, weight="bold"))
homeTitleFrame.grid(row=0, column=0, columnspan=3, padx=10, pady=20)

    ## CUSTOMER COLUMN
customersColumn = Label(secondFrame, text="Customers", underline=8, width=20, background="red", foreground="white", font=tkFont.Font(family="Sans Serif", size=15, weight="bold", underline=True))
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

window.mainloop()
