from tkinter import *


class Buttons(Frame):
    def __init__(self, root):
        Frame.__init__(self, master=root, width=240, background="lightgrey")
        self.configure(bd=4, relief=GROOVE)
        Button(self, text="Start", width=10).grid(row=0, column=0, padx=5, pady=5)
        Button(self, text="Reset", width=10).grid(row=0, column=1, padx=5, pady=5)
        Button(self, text="Device", width=10).grid(row=1, column=0, padx=5, pady=5)
        Button(self, text="Close", width=10).grid(row=1, column=1, padx=5, pady=5)
