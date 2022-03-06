from tkinter import *


class Formula(Frame):
    def __init__(self, root):
        Frame.__init__(self, master=root, width=240, background="lightgrey")
        self.configure(bd=4, relief=GROOVE)
        Label(self, text="t = L/R = ... ms", background="lightgrey", font="sans-serif 13 bold").pack(padx=5, pady=5)
        Label(self, text="I = U/R(1 - exp(-1/t)) = ... A", background="lightgrey", font="sans-serif 13 bold").pack(side=BOTTOM, padx=5, pady=5)