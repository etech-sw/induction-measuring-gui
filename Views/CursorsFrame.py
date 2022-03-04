from tkinter import *


class Cursors(Frame):
    def __init__(self, root):
        Frame.__init__(self, master=root, width=240)
        self.configure(bd=4, relief=GROOVE)
        self.R, self.L, self.U = 0, 0, 0
        # Definition of the cursors widgets
        Scale(self, length=200, orient=HORIZONTAL, label="R :").pack(padx=5)
        Scale(self, length=200, orient=HORIZONTAL, label="L :").pack(side=BOTTOM, padx=5)
        Scale(self, length=200, orient=HORIZONTAL, label="U :").pack(side=BOTTOM, padx=5)
