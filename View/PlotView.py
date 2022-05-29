import tkinter
from tkinter import ttk

import numpy as np
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


class PlotView(ttk.Frame):
    """This class acts as a container for Plots and provides methods for drawing their data

    """


    def __init__(self,master, datavar):
        super().__init__(master)
        self.datavar = datavar
        self.fig = None
        self.generate_canvas()
        self.toolbar = self.generate_toolbar()
        self.refresh = False
        self.minxdata = 0
        self.maxxdata = 1
        self.minvoltage = 0
        self.maxvoltage = 1
        mincurrent = 0
        maxcurrent = 1

    def animate(self):
        time = []
        voltage = []
        current = []
        data = self.datavar.get()

        if len(data) <= 0: return

        for t, v in list(data.items()):
            time.append(float(t))
            voltage.append(float(v[0]))
            current.append(float(v[1]))

        self.x_data = time
        self.y_data = voltage
        self.z_data = current
        self.plot1.set_data(self.x_data,self.y_data)
        self.plot2.set_data(self.x_data,self.z_data)
        self.plot3.set_data(self.y_data,self.z_data)
        self.ax1.set_xlabel("time")
        self.ax1.set_ylabel("Voltage")
        self.ax1.set_xlim(min(time), max(time))
        self.ax1.set_ylim(min(voltage), max(voltage))
        self.ax2.set_xlabel("time")
        self.ax2.set_ylabel("Current")
        self.ax2.set_xlim(min(time), max(time))
        self.ax2.set_ylim(min(current), max(current))
        self.ax3.set_xlabel("Current")
        self.ax3.set_ylabel("Voltage")
        self.ax3.set_xlim(min(current), max(current))
        self.ax3.set_ylim(min(voltage), max(voltage))
        self.canvas.draw_idle()
        if self.refresh:
            self.after(500,self.animate)

    def generate_canvas(self):

        self.fig = Figure(figsize=(10, 7))
        self.ax1 = self.fig.add_subplot(221)
        self.ax2 = self.fig.add_subplot(222)
        self.ax3 = self.fig.add_subplot(223)
        # create the plot
        self.plot1 = self.ax1.plot([],[], label='Plot')[0]
        self.plot2 = self.ax2.plot([],[],label = "Schlampe")[0]
        self.plot3 = self.ax3.plot([],[], label = "Hurensohn")[0]
        self.ax1.set_xlabel("time")
        self.ax1.set_ylabel("Voltage")
        self.ax1.set_xlim(self.minxdata,self.maxxdata)
        self.ax1.set_ylim(0,10)
        self.ax2.set_xlabel("time")
        self.ax2.set_ylabel("Current")
        self.ax2.set_xlim(0,30)
        self.ax2.set_ylim(0 ,10)
        self.ax3.set_xlabel("Current")
        self.ax3.set_ylabel("Voltage")
        self.ax3.set_xlim(0,10)
        self.ax3.set_ylim(-13,13)

        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().grid(row=0, column=0, sticky=tkinter.W)

    def generate_toolbar(self):
        toolbar = NavigationToolbar2Tk(self.canvas, self,pack_toolbar=False)
        toolbar.grid(row=1, column=0, sticky=tkinter.W)
        toolbar.update()
        return toolbar
