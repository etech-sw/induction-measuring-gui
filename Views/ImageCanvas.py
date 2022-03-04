from tkinter import *


class ImageCanvas(Canvas):
    def __init__(self, root):
        Canvas.__init__(self, master=root, width=250, height=250, background="slateblue")
        