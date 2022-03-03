from tkinter import *
from tkinter import ttk
from Data_functions import display_customers_data

class CustomersFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, master=root, width=780, height=450, background="red", highlightbackground="black", highlightthickness=3)
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.style.configure("Treeview",
            background="red",
            foreground="white",
            fieldbackground="red",
            font="Sans-Serif 13 bold"
        )
        self.style.map("Treeview",
            background=[("selected", "lightpink")],
            foreground=[("selected", "black")]
        )

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

