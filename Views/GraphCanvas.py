from tkinter import *


class Graph(Canvas):
    def __init__(self, root):
        Canvas.__init__(self, master=root, width=450, height=260, background="white")
        larg, haut = 450, 250
        self.create_line(10, haut-5, larg-5, haut-5, arrow=LAST) #X
        self.create_line(10, haut-5, 10, 5, arrow=LAST) #Y
        # Drawing of vertical lines
        stepX = (larg-35)/10  
        for t in range(1,11):
            vl = 10 + t*stepX
            self.create_line(vl, 20, vl, haut-5, fill="lightgrey")
            self.create_text(vl, haut, text=str(t), anchor=CENTER, font="Sans-serif 6")
        # Drawing of horizontal lines
        stepY = (haut-25)/10
        for t in range(1,11):
            hl = haut-5 - t*stepY
            self.create_line(10, hl, larg-25, hl, fill="lightgrey")
            self.create_text(5, hl, text=str(t), anchor=CENTER, font="Sans-serif 6")

