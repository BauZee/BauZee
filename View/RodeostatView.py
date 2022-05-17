import tkinter as tk
import tkinter.ttk
from idlelib.tooltip import Hovertip
from tkinter import ttk
from tkinter.ttk import Label

import Controller.Rodeostat.RodeostatController


# Basisklasse, erbt von Frame, damit wir es in der GUI wie einen Frame benutzen können
from View.PlotView import PlotView


class DeviceView(ttk.Frame):
    name = "DefaultDevice"

    def __init__(self, master):
        super().__init__(master=master)  # Constructor von Frame wird aufgerufen
        self.controller = None
        self.paramframe = ttk.Frame(self)  # Container for adding parameters
        self.paramframe.grid(row=1, column=0, columnspan=2, sticky=tk.N + tk.S + tk.W + tk.E)
        self.buttonframe = ttk.Frame(self)

    def start_measurement(self):
        self.controller.start_test()

    def update_plot(self, event):
        pass

    def create_label(self, text, row, column, padx=5, pady=2):
        label = Label(self.paramframe, text=text)
        label.grid(row=row, column=column, padx=padx, pady=pady, sticky=tk.W)
        return label

    def create_entry(self, width=None, borderwidth=None, row=0, column=0, textvariable=None):
        entry = tk.Entry(self.paramframe, width=width, borderwidth=borderwidth,textvariable=textvariable )
        entry.grid(row=row, column=column, )
        return entry

    def generate_param_element(self,row, stringvar, label, tooltip):
        label = self.create_label(label, row, 0)
        entrybox = self.create_entry(row=row, column=1, textvariable=stringvar)
        hovertip = Hovertip(entrybox,tooltip)

class RodeostatView(DeviceView):
    def __init__(self, master):
        super().__init__(master)
        self.running = False

        # Messverfahren
        self.MethodDict = {"Cyclo": Controller.Rodeostat.RodeostatController.CycloController,
                           "Squarewave": Controller.Rodeostat.RodeostatController.SquarewaveController}

        # Jede Methode hat einen Startknopf, also generieren wir den unabhängig von der Auswahl
        self.start_button = ttk.Button(self.buttonframe, text="Start Test",command=lambda:self.controller.start_test())
        self.clear_button = ttk.Button(self.buttonframe, text="Clear Results",command=lambda:self.controller.clear())

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=3)

        self.rowconfigure(0)
        self.rowconfigure(0)
        self.rowconfigure(0)

        methodframe = ttk.Frame(self)
        methodframe.grid(row=0,column=0,columnspan=2, sticky=tk.W, padx=5,pady=10)

        self.plotframe = PlotView(self, None)

        # Variable für Callback
        methodlabel = Label(self, text="Measurement method:")

        variable = tk.StringVar(self)
        self.method_menu = ttk.OptionMenu(self, variable, list(self.MethodDict.keys())[0], *self.MethodDict.keys(),
                                  command=lambda var: self.on_method_changed(var))

        methodlabel.pack(in_=methodframe, side=tk.LEFT)
        self.method_menu.pack(in_=methodframe, side=tk.LEFT)

        # Laden des default Wertes der Combobox
        self.on_method_changed(list(self.MethodDict.keys())[0])

    def on_method_changed(self, variable):
    #'''Diese Methode wird aufgerufen, wenn die Messmethode verändert wird '''
        # Hier machen wir was aus der Auswahl
        # A) Controller des Typs MethodenameController() erzeugen
        self.controller = self.MethodDict[variable]()
        self.plotframe.datavar = self.controller.data


    # Aufräumen vom letzten UI
        for widget in self.paramframe.grid_slaves():
            widget.grid_forget()

        # )B UI Anpassungen
        self.plotframe.grid(row=0, column=3, rowspan=len(vars(self.controller.paramset)), padx=5, pady=10,
                        sticky=tkinter.W + tkinter.E)
        self.buttonframe.grid(row=len(vars(self.controller.paramset)) + 1, column=0, sticky=tk.W,pady=20,padx =10)


        self.start_button.pack(in_=self.buttonframe,side=tk.LEFT)
        self.clear_button.pack(in_=self.buttonframe,side=tk.LEFT)

        # C) Die Parameter in GUI Elemente verwandeln
        for row, (value, (label,tooltip)) in enumerate(self.controller.get_parameters()):

            # 1) Get 3-tupel from self.controller.get_parameters() -> (value,(label,tooltip)) [("Stringvar",("Label","Tooltip"))]
            # 2) "Unpack" them to row,value,label,tooltip
            # 3) Generate the UI Row by calling generate_param_element()
            self.generate_param_element(row, value, label, tooltip)

        self.plotframe.animate()