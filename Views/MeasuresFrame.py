from tkinter import *
from DAO_Module.DeviceDAO import DeviceDAO


class MeasuresFrame(Frame):
    def __init__(self, root):
        Frame.__init__(self, master=root, width=780, height=450, background="red", highlightbackground="black", highlightthickness=3)
        self.canvas = Canvas(self, width=780, height=300, background="white")
        self.canvas.grid(row=0, column=0,columnspan=5, padx=30, pady=5)
        # Radiobutton section
        self.var = IntVar()
        self.radio1 = Radiobutton(self, text=" 0 V", variable=self.var, value=0, background="red", font="Sans-Serif 15")
        self.radio1.grid(row=1, column=0)
        self.radio2 = Radiobutton(self, text="12 V", variable=self.var, value=12, background="red", font="Sans-Serif 15")
        self.radio2.grid(row=2, column=0)
        self.radio3 = Radiobutton(self, text="24 V", variable=self.var, value=24, background="red", font="Sans-Serif 15")
        self.radio3.grid(row=3, column=0)
        # Dropdown menu for devices
        self.selected = StringVar()
        self.selected.set("Select device")
        devices = self.__getDevices()
        self.device = OptionMenu(self, self.selected, *devices)
        self.device.grid(row=2, column=1)
        Button(self, text="Measure Start", background="green", foreground="white", font="Sans-Serif 15 bold").grid(row=2, column=2)
        Button(self, text="Measure End", background="darkred", foreground="white", font="Sans-Serif 15 bold").grid(row=3, column=2, pady=5)
        
        # Responsive configuration
        for i in range(4):
            Grid.rowconfigure(self, index=i, weight=1)
        for i in range(3):
            Grid.columnconfigure(self, index=i, weight=1)


    def __getDevices(self):
        devices_list = []
        devices = DeviceDAO().get_all_devices()
        if len(devices) == 0:
            devices_list = ["None"]
        else:
            for device in devices:
                devices_list.append(device[1])
        return devices_list
