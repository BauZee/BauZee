import tkinter as tk
from tkinter import ttk

import Controller.RodeostatController
from Controller.RodeostatController import RodeostatController


#Basisklasse, erbt von Frame, damit wir es in der GUI wie einen Frame benutzen können
class DeviceView(tk.Frame):
    name = "DefaultDevice"


    def __init__(self, master):
        super().__init__(master=master) # Constructor von Frame wird aufgerufen
        self.controller = None
        self.iterate_params()

    def start_measurement(self):
        self.controller.Start()

    def update_plot(self, event):
        pass

    def iterate_params(self):
        pass


class RodeostatView(DeviceView):
    def __init__(self, master):
        super().__init__(master)
        self.running = False


        #Messverfahren
        self.MethodDict = {"Cyclo": Controller.RodeostatController.CycloController(),
                           "Squarewave": Controller.RodeostatController.SquarewaveController()}

        #Variable für Callback
        variable = tk.StringVar(self)
        opt = ttk.OptionMenu(self, variable, list(self.MethodDict.keys())[0], *self.MethodDict.keys(),
                             command=lambda var: self.on_method_changed(var))
        opt.grid(row=0, column=0)

    def iterate_params(self):
        for column, para in enumerate(self.controller.paramset):
            pass

    def on_method_changed(self, variable):

        #Hier machen wir was aus der Auswahl
        # A) Controller des Typs MethodenameController() erzeugen
        self.controller = self.MethodDict[variable]
        # B) Den Startknopf mit der Start Methode des Controllers verbinden
        start_button = tk.Button(self, text="Start Test", command=lambda: self.controller.start_test())
        # C) Die Parameter in GUI Elemente verwandeln


        #Jede Methode hat einen Startknopf, also generieren wir den unabhängig von der Auswahl
        start_button.grid(row=1, column=0)
        clear_button = tk.Button(self, text="Clear Results", command=lambda: self.controller.data.clear())
        clear_button.grid(row=2, column=0)

