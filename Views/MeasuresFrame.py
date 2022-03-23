from tkinter import *


class MeasuresFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, master=root, width=780, height=450, background="red", highlightbackground="black", highlightthickness=3)
        self.canvas = Canvas(self, width=780, height=300, background="white")
        self.canvas.grid(row=0, column=0,columnspan=4, padx=30, pady=5)
        self.radio1 = Radiobutton(self, text="0 V", background="red", font="Sans-Serif 15")
        self.radio1.grid(row=1, column=0)
        self.radio2 = Radiobutton(self, text="12 V", background="red", font="Sans-Serif 15")
        self.radio2.grid(row=2, column=0)
        self.radio3 = Radiobutton(self, text="24 V", background="red", font="Sans-Serif 15")
        self.radio3.grid(row=3, column=0)
        Button(self, text="Measure Start", background="green", foreground="white", font="Sans-Serif 15 bold").grid(row=2, column=1)
        Button(self, text="Measure End", background="darkred", foreground="white", font="Sans-Serif 15 bold").grid(row=2, column=2)
        
        # Responsive configuration
        for i in range(4):
            Grid.rowconfigure(self, index=i, weight=1)
        for i in range(3):
            Grid.columnconfigure(self, index=i, weight=1)
