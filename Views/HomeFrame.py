from tkinter import *
from Data_functions import display_last_customers, display_last_devices

class HomeFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, master=root, width=800, height=450, background="red", highlightbackground="black", highlightthickness=3)
        Label(self, text="Last edit...", background="red", foreground="white", font="Sans-Serif 20 ").grid(row=0, column=0, columnspan=3, padx=20, pady=20)
        Label(self, text="Customers", width=20, background="red", foreground="white", font="Sans-Serif 15 bold underline").grid(row=1, column=0, padx=15, pady=10, sticky=W)
        display_last_customers(self)

        Label(self, text="Devices", width=20, background="red", foreground="white", font="Sans-Serif 15 bold underline").grid(row=1, column=1, padx=15, pady=10)
        display_last_devices(self)

        Label(self, text="Measures", background="red", width=20, foreground="white", font="Sans-Serif 15 bold underline").grid(row=1, column=2, padx=15, pady=10)

        # Responsive configuration
        for i in range(2):
            Grid.rowconfigure(self, index=i, weight=1)
        for i in range(3):
            Grid.columnconfigure(self, index=i, weight=1)

