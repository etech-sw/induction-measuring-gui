from tkinter import *
import tkinter.font as tkFont

def homePage(event):
    homeButton.configure(background="deepskyblue")
    clientButton.configure(background="red")
    dispositifButton.configure(background="red")
    mesureButton.configure(background="red")
    titleLabel.configure(text="Page d'Accueil")


def clientPage(event):
    homeButton.configure(background="red")
    clientButton.configure(background="deepskyblue")
    dispositifButton.configure(background="red")
    mesureButton.configure(background="red")
    titleLabel.configure(text="Page Clients")


def dispositifPage(event):
    homeButton.configure(background="red")
    clientButton.configure(background="red")
    dispositifButton.configure(background="deepskyblue")
    mesureButton.configure(background="red")
    titleLabel.configure(text="Page des Dispositifs")


def mesurePage(event):
    homeButton.configure(background="red")
    clientButton.configure(background="red")
    dispositifButton.configure(background="red")
    mesureButton.configure(background="deepskyblue")
    titleLabel.configure(text="Page des Mesures")


window = Tk()
mainFrame = Frame(window, height=800, width=800, background="lightpink", highlightbackground="black", highlightthickness=3)
mainFrame.pack(ipadx=5, ipady=20)

secondFrame = Frame(mainFrame, width=780, height=450, background="red", highlightbackground="black", highlightthickness=3)
secondFrame.grid(row=1, column=1, rowspan=7, ipadx=5, ipady=10, padx=5)

menuLabel = Label(mainFrame, text="Menu", width=10, height=3, background="red", foreground="white", highlightbackground="black",
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
menuLabel.grid(row=0, column=0, padx=40, pady=20)

titleLabel = Label(mainFrame, text="Page d'Accueil", width=65, height=3, background="red", foreground="white", highlightbackground="black", 
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
titleLabel.grid(row=0, column=1, padx=5, pady=20)

homeButton = Button(mainFrame, text="Home", background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
homeButton.grid(row=1, column=0)
homeButton.bind("<Button-1>", homePage)

clientButton = Button(mainFrame, text="+ Client", background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
clientButton.grid(row=2, column=0, padx=5, pady=10)
clientButton.bind("<Button-1>", clientPage)

dispositifButton = Button(mainFrame, text="+ Dispositif", background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
dispositifButton.grid(row=3, column=0, padx=5, pady=10)
dispositifButton.bind("<Button-1>", dispositifPage)

mesureButton = Button(mainFrame, text="Mesure", background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
mesureButton.grid(row=4, column=0, padx=5, pady=10)
mesureButton.bind("<Button-1>", mesurePage)

reglageButton = Button(mainFrame, text="Reglage", background="red", foreground="white", highlightbackground="black", width=10, 
                    highlightthickness=3, font=tkFont.Font(family="Sans Serif", size=15, weight="bold"))
reglageButton.grid(row=7, column=0, padx=5, pady=10)


window.mainloop()
