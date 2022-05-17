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
from Controller.PlotViewController import PlotViewController

class PlotView(ttk.Frame):
    def __init__(self,master,datavar):
        super().__init__(master)
        self.controller = PlotViewController()
        self.datavar = datavar
        self.fig = None

        self.generate_canvas()
        self.canvas.mpl_connect("key_press_event", self.on_key_press)
        self.toolbar = self.generate_toolbar()

    def animate(self):
        xar = []
        yar = []
        data = self.datavar.get()
        if len(data) > 0:
            for t, v in list(data.items()):
                xar.append(float(t))
                yar.append(float(v))

        self.x_data = xar
        self.y_data = yar
        self.plot.set_xdata(self.x_data)
        self.plot.set_ydata(self.y_data)
        self.canvas.draw_idle()
        self.after(1000, self.animate)

    def on_key_press(self,event):
        print("you pressed {}".format(event.key))
        key_press_handler(event=event, canvas=self.canvas, toolbar=self.toolbar)

    def generate_canvas(self):
        self.fig = Figure(figsize=(4, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.x_data = []
        self.y_data = []
        # create the plot
        self.plot = self.ax.plot(self.x_data, self.y_data, label='Plot')[0]
        self.ax.set_ylim(0, 1)
        self.ax.set_xlim(0, 10)

        self.canvas = FigureCanvasTkAgg(self.fig, self)
        self.canvas.get_tk_widget().grid(row=0,column=0,sticky=tkinter.W)


    def generate_toolbar(self):
        toolbar = NavigationToolbar2Tk(self.canvas, self,pack_toolbar=False)
        toolbar.grid(row=1,column=0,sticky=tkinter.W)
        toolbar.update()

        return toolbar