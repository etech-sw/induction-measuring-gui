from tkinter import *
from Views.MainFrame import MainFrame


window = Tk()
window.title("GUI Interface")
window.geometry("1000x800")
frame = MainFrame(window)
frame.grid(row=0, column=0, sticky="nsew", ipadx=20, ipady=20)

# Responsive configuration
Grid.rowconfigure(window, index=0, weight=1)
Grid.columnconfigure(window, index=0, weight=1)

window.mainloop()