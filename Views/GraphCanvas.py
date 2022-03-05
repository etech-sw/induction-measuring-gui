from tkinter import *


class Graph(Canvas):
    def __init__(self, root):
        Canvas.__init__(self, master=root, width=450, height=250, background="white")
        larg, haut = 450, 250
        self.create_line(10, haut-5, larg-5, haut-5, arrow=LAST) #X
        self.create_line(10, haut-5, 10, 5, arrow=LAST) #Y
        # pasX = (larg-20)/10  
        # for t in range(1,11):



# # ====================
# win = Tk()
# can = GraphCanvas(win)
# can.pack()
# win.mainloop()