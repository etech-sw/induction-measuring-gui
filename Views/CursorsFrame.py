from tkinter import *


class Cursors(Frame):
    def __init__(self, root):
        Frame.__init__(self, master=root, width=240)
        self.configure(bd=4, relief=GROOVE)
        self.R, self.L, self.U = 0, 0, 0
        # Definition of the cursors widgets
        Label(self, text="R:").grid(row=0, column=0, padx=5)
        Scale(self, length=200, orient=HORIZONTAL).grid(row=0, column=1, padx=5)
        Label(self, text="L:").grid(row=1, column=0, padx=5)
        Scale(self, length=200, orient=HORIZONTAL).grid(row=1, column=1, padx=5)
        Label(self, text="U:").grid(row=2, column=0, padx=5)
        Scale(self, length=200, orient=HORIZONTAL).grid(row=2, column=1, padx=5)
