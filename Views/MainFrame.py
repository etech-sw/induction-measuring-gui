from tkinter import *
from Views.CustomersFrame import CustomersFrame
from Views.HomeFrame import HomeFrame
from Views.DevicesFrame import DevicesFrame
from Views.MeasuresFrame import MeasuresFrame


class MainFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, master=root, height=800, width=800, background="lightpink", highlightbackground="black", highlightthickness=3)

        Label(self, text="Menu", width=10, height=3, background="red", foreground="white", highlightbackground="black",
                    highlightthickness=3, font="Sans-Serif 15 bold").grid(row=0, column=0, padx=40, pady=20)
    
        self.titleLabel = Label(self, text="Home Page", width=65, height=3, background="red", foreground="white", highlightbackground="black",
                     highlightthickness=3, font="Sans-Serif 16 bold")
        self.titleLabel.grid(row=0, column=1, padx=5, pady=20)

        self.homeButton = Button(self, text="Home", command=self.goToHomePage, background="deepskyblue", foreground="white", width=10, font="Sans-Serif 15 bold")
        self.homeButton.grid(row=1, column=0)
        self.customerButton = Button(self, text="+ Customer", command=self.goToCustomerPage, background="red", foreground="white", width=10, font="Sans-Serif 15 bold")
        self.customerButton.grid(row=2, column=0, padx=5, pady=10)
        self.deviceButton = Button(self, text="+ Device", command=self.goToDevicePage, background="red", foreground="white", width=10, font="Sans-Serif 15 bold")
        self.deviceButton.grid(row=3, column=0, padx=5, pady=10)
        self.measureButton = Button(self, text="Measure", command=self.goToMeasurePage, background="red", foreground="white", width=10, font="Sans-Serif 15 bold")
        self.measureButton.grid(row=4, column=0, padx=5, pady=10)

        self.frame = HomeFrame(self)
        self.frame.grid(row=1, column=1, rowspan=7, ipadx=5, ipady=5, padx=5)
        

    def goToHomePage(self):
        self.frame.destroy()
        self.homeButton.configure(background="deepskyblue")
        self.customerButton.configure(background="red")
        self.deviceButton.configure(background="red")
        self.measureButton.configure(background="red")
        self.titleLabel.configure(text="Home Page")
        self.frame = HomeFrame(self)
        self.frame.grid(row=1, column=1, rowspan=7, ipadx=5, ipady=5, padx=5)


    def goToCustomerPage(self):
        self.frame.destroy()
        self.homeButton.configure(background="red")
        self.customerButton.configure(background="deepskyblue")
        self.deviceButton.configure(background="red")
        self.measureButton.configure(background="red")
        self.titleLabel.configure(text="Customers Page")
        self.frame = CustomersFrame(self)
        self.frame.grid(row=1, column=1, rowspan=7, ipadx=5, ipady=5, padx=5)


    def goToDevicePage(self):
        self.frame.destroy()
        self.homeButton.configure(background="red")
        self.customerButton.configure(background="red")
        self.deviceButton.configure(background="deepskyblue")
        self.measureButton.configure(background="red")
        self.titleLabel.configure(text="Devices Page")
        self.frame = DevicesFrame(self)
        self.frame.grid(row=1, column=1, rowspan=7, ipadx=5, ipady=5, padx=5)


    def goToMeasurePage(self):
        self.frame.destroy()
        self.homeButton.configure(background="red")
        self.customerButton.configure(background="red")
        self.deviceButton.configure(background="red")
        self.measureButton.configure(background="deepskyblue")
        self.titleLabel.configure(text="Measures Page")
        self.frame = MeasuresFrame(self)
        self.frame.grid(row=1, column=1, rowspan=7, ipadx=5, ipady=5, padx=5)