from tkinter import *
from Views.MainFrame import MainFrame

window = Tk()
window.title("GUI Interface")
frame1 = MainFrame(window)
frame1.pack(ipadx=5, ipady=20)

window.mainloop()