from tkinter import *
from Views.CursorsFrame import Cursors
from Views.GraphCanvas import Graph
from Views.ImageCanvas import ImageCanvas


class MeasuresFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, master=root, width=780, height=450, background="red", highlightbackground="black", highlightthickness=3)
        self.canvasGraph = Graph(self)
        self.canvasGraph.grid(row=0, column=0, padx=15, pady=5)
        self.canvasImage = ImageCanvas(self)
        self.canvasImage.grid(row=0, column=1, padx=15, pady=5)
        self.optionsFrame = Frame(self, width=730, background="white")
        self.optionsFrame.grid(row=1, column=0, columnspan=2, padx=15, pady=5)
        Cursors(self.optionsFrame).pack(side=LEFT, padx=10, pady=5)
        self.formulaFrame = Frame(self.optionsFrame, width=240, background="lightgrey")
        self.formulaFrame.pack(side=LEFT, padx=10, pady=5, ipadx=20, ipady=20)
        Label(self.formulaFrame, text="t = L/R = ... ms", background="lightgrey", font="sans-serif 15 bold").pack(padx=5, pady=5)
        Label(self.formulaFrame, text="I = U/R(1 - exp(-1/t)) = ... A", background="lightgrey", font="sans-serif 15 bold").pack(side=BOTTOM, padx=5, pady=5)
        self.buttonsFrame = Frame(self.optionsFrame, width=240, background="lightgrey")
        self.buttonsFrame.pack(side=LEFT, padx=10, pady=5, ipadx=20, ipady=20)
        Button(self.buttonsFrame, text="Start").pack(padx=10, pady=10)
