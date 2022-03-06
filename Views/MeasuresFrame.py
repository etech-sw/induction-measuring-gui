from tkinter import *
from Views.ButtonsFrame import Buttons
from Views.CursorsFrame import Cursors
from Views.FormulaFrame import Formula
from Views.GraphCanvas import Graph
from Views.ImageCanvas import ImageCanvas


class MeasuresFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, master=root, width=780, height=450, background="mediumslateblue", highlightbackground="black", highlightthickness=3)
        self.canvasGraph = Graph(self)
        self.canvasGraph.grid(row=0, column=0, padx=15, pady=5)
        self.canvasImage = ImageCanvas(self)
        self.canvasImage.grid(row=0, column=1, padx=15, pady=5)
        self.optionsFrame = Frame(self, width=730, background="lightgrey")
        self.optionsFrame.grid(row=1, column=0, columnspan=2, padx=15, pady=5)
        Cursors(self.optionsFrame).pack(side=LEFT, padx=10, pady=5)
        Formula(self.optionsFrame).pack(side=LEFT, padx=10, pady=5)
        Buttons(self.optionsFrame).pack(side=LEFT, padx=10, pady=5)
        
