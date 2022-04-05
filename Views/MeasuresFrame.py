from tkinter import *
from DAO_Module.DeviceDAO import DeviceDAO
from DAO_Module.MeasurementDAO import MeasurementDAO
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk)
from datetime import datetime
from threading import Thread
import requests

class MeasurementJob(Thread):
    def __init__(self, canvas, device_selected, startMeasure, measurementStatus):
        super().__init__()
        self.canvas = canvas
        self.id = device_selected
        self.startMeasure = startMeasure
        self.measurementStatus = measurementStatus
        # Visualizing voltage and intensity
        self.fig = plt.figure(figsize=(8,6), dpi = 100)
        plt.xlabel('time in seconds')
        plt.ylabel('voltage/current values')
        plt.grid()
        plt.legend(loc='upper right')
        #plt.show()
        self.measurement_canvas = FigureCanvasTkAgg(self.fig, master=self.canvas)

    def run(self):
        print("Measurement thread job started...")
        while(1):
            measurements = MeasurementDAO().get_all_measurements(self.id, self.startMeasure)
            measured_at = []
            voltage = []
            intensity = []

            for i in measurements:
                measured_at.append(i[0])
                voltage.append(i[1])
                intensity.append(i[2])

            print("measurement timestamp: ", measured_at)
            print("voltage values: ", voltage)
            print("intensity values: ", intensity)

            if self.measurementStatus == False:
                print("Measurement thread job stop...")
                return

            if len(measured_at) > 0:
                # Visualizing voltage and intensity
                plt.plot(measured_at, voltage, label='voltage', lw=2, marker='o')
                plt.plot(measured_at, intensity, label='intensity', lw=2, marker='s')
                plt.gcf().autofmt_xdate()
                #plt.show()
                self.measurement_canvas.draw()
                self.measurement_canvas.get_tk_widget().pack()
                #toolbar = NavigationToolbar2Tk(canvas,self.canvas)
                #toolbar.update()
                #canvas.get_tk_widget().pack()
            else:
                print("There isn't data recorded for the selected device_id: %s from %s" % (self.id, self.startMeasure))

class MeasuresFrame(Frame):
    # Status of the measurement status
    measurementStatus = False

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
        self.device = OptionMenu(self, self.selected, *devices, command=self.__getSelectedOptionMenu)
        self.device.grid(row=2, column=1)
        self.measureStart = Button(self, text="Measure Start", command=self.startMeasure, background="green", foreground="white", width=20, font="Sans-Serif 15 bold").grid(row=2, column=2)
        self.measureEnd = Button(self, text="Measure End", command=self.measureEnd, background="darkred", foreground="white", width=20, font="Sans-Serif 15 bold").grid(row=3, column=2, pady=5)

        # Responsive configuration
        for i in range(4):
            Grid.rowconfigure(self, index=i, weight=1)
        for i in range(3):
            Grid.columnconfigure(self, index=i, weight=1)


    def startMeasure(self):
        try:
            url = 'https://localhost:5000/api/messung'
            body = {'id': int(self.selected.get()),'action': 1,'tension': self.var.get()}
            #startMeasurement = requests.post(url, data = body)
            #print(startMeasurement.text)
            self.measurementStatus = True

            # Create measurement thread
            now = datetime.utcnow()
            self.measurement_thread = MeasurementJob(self.canvas, int(self.selected.get()), now.strftime('%Y-%m-%d %H:%M:%S'), self.measurementStatus)
            self.measurement_thread.start()
            #self.monitor(measurement_thread)
        except requests.ConnectionError as e:
            print(e)


    def measureEnd(self):
        try:
            url = 'https://localhost:5000/api/messung'
            body = {'id': int(self.selection_option_menu),'action': 0,'tension': self.var.get()}
            #stopMeasurement = requests.post(url, data = body)
            #print(stopMeasurement.text)
            self.measurementStatus = False
            # Signal termination
            self.measurement_thread.terminate()
        except requests.ConnectionError as e:
                    print(e)

    def __getDevices(self):
        devices_list = []
        devices = DeviceDAO().get_all_devices()
        if len(devices) == 0:
            devices_list = ["None"]
        else:
            for device in devices:
                devices_list.append(device[1])
        return devices_list

    def __getSelectedOptionMenu(self,selection):
        self.selection_option_menu = self.selected.get()
        print(self.selection_option_menu)