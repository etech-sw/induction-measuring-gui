from tkinter import Label
from DAO_Module.CustomerDAO import CustomerDAO
from DAO_Module.DeviceDAO import DeviceDAO


def display_last_customers(secondFrame):
    # Initialization and recovery of the database
    customerDAO = CustomerDAO()
    customers = customerDAO.get_last_customers()
    compt, row = 1, 2
    # Display on the interface
    for customer in customers:
        Label(secondFrame, text=str(compt)+"."+customer[1], justify="right", background="red", foreground="white", font="Sans-Serif 10 bold").grid(row=row, column=0, pady=10)
        compt += 1
        row += 1
        if (compt > 5):
            break


def display_last_devices(secondFrame):
    # Initialization and recovery of the database
    deviceDAO = DeviceDAO()
    devices = deviceDAO.get_last_devices()
    compt, row = 1, 2
    # Display on the interface
    for device in devices:
        Label(secondFrame, text=str(compt)+"."+device[1], justify="right", background="red", foreground="white", font="Sans-Serif 10 bold").grid(row=row, column=1, pady=10)
        compt += 1
        row += 1
        if (compt > 5):
            break


def display_customers_data(treeView):
    customerDAO = CustomerDAO()
    customers = customerDAO.get_all_customers()
    id = 0
    for customer in customers:
        treeView.insert(parent="", index="end", iid=id, text="", values=(customer[0], customer[5], customer[6], customer[7], customer[8], customer[4], customer[3], customer[1], customer[2]))
        id += 1


def display_devices_data(treeView):
    deviceDAO = DeviceDAO()
    devices = deviceDAO.get_all_devices()
    id = 0
    for device in devices:
        treeView.insert(parent="", index="end", iid=id, text="", values=(device[0], device[1], device[2], device[3], device[4], device[5], device[6]))
        id += 1


