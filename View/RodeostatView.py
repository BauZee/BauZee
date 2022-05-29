import abc
import tkinter as tk
import tkinter.ttk
from idlelib.tooltip import Hovertip
from tkinter import ttk, DISABLED, NORMAL
from tkinter.ttk import Label
import serial.tools.list_ports
import Controller.Rodeostat.RodeostatController
from Model.VoltaMetricParamset import *
from tkinter import filedialog

# Basisklasse, erbt von Frame, damit wir es in der GUI wie einen Frame benutzen können

from View.PlotView import PlotView


class DeviceView(ttk.Frame, metaclass=abc.ABCMeta):
    """This class acts as an abstract base class for all devices that need to be added to the UI

    Since this class inherits from Frame, it acts as a container which then can be added to an UI.
    Every device should utilize a Controller responsible for calculations etc.

    """
    name = "DefaultDevice"

    def __init__(self, master):
        super().__init__(master=master)  # Constructor von Frame wird aufgerufen

        # RodeostatController: Contains the controller of the choosen measument method
        self.controller = None

        # ttk.Frame: Container containing all Paremeter Widgets e.g. Entryboxes and labels
        self.paramframe = ttk.Frame(self)  # Container for adding parameters
        self.paramframe.grid(row=2, column=0, columnspan=2, sticky=tk.N + tk.S + tk.W + tk.E)

        # ttk.Frame: Container for Buttons related to the controller e.g. starting measurements
        self.buttonframe = ttk.Frame(self)

        # ttk.Frame: Container for port scanner widget
        self.portframe = ttk.Frame(self)
        self.portframe.grid(row=1, column=0, columnspan=2, sticky=tk.W, padx=2, pady=2)

    def start_measurement(self):
        """ This method will start the measurement by calling the corresponding controllers method

        This method will additionally call the check_running method which will periodically check
        the state of the worker thread and will enable/disable UI elements based on the result
        """
        self.controller.start_test()
        self.check_running()

    def create_label(self, text, row, column, padx=5, pady=2):
        """ Utility method used to create labels for parameters and adds it to the grid of self.paramframe


        Args:
            text (str): The content of the label
            row (int): The row of the containers grid
            column (int): The column of the containers grid
            padx (int): the padding in x direction
            pady (int): the padding in y direction

        Returns:
            A label with the given parameters
        """
        label = Label(self.paramframe, text=text, font=('Calibri', 14))
        label.grid(row=row, column=column, padx=padx, pady=pady, sticky=tk.W)
        return label

    def create_entry(self, width=30, borderwidth=None, row=0, column=0, textvariable=None):
        """ This method creates an entrybox with the given porameters and adds it to the grid of self.paramframe

        Args:
            width(int): the width of the entry box
            borderwidth(int): the width of the border
            row (int): The row of the containers grid
            column (int): The column of the containers grid
            textvariable: The tk.Variable which will contain the current value

        Returns:
            An entrybox object with the given params
        """
        entry = tk.Entry(self.paramframe, width=width, borderwidth=borderwidth, textvariable=textvariable,
                         font=("Calibri", 14))
        entry.grid(row=row, column=column, )
        return entry

    def generate_param_element(self, row, stringvar, labeltext, tooltip, validation=None):
        """ This method will create a pair of label-entrybox elements
        including validation information and hovertext  by calling helper methods

        Args:
            row(int):  The row of the pair in the self.paramframe grid
            stringvar(tk.StringVar): The variable for storing the entrybox value
            labeltext(str): The content of the label
            tooltip(str): The string the hovertip shall display
            validation(Model.Validation): The validation object for the entrybox value
        """
        label = self.create_label(labeltext, row, 0)
        entrybox = self.create_entry(row=row, column=1, textvariable=stringvar)

        # Validation
        if validation is not None:
            vcmd = (self.register(lambda value: validation.validate(value, entrybox)), '%P')
            entrybox.config(validate='focus', validatecommand=vcmd)

        hovertip = Hovertip(entrybox, tooltip)

    @abc.abstractmethod
    def check_running(self):
        """ Abstract method for handling the UI during measurements.

        This method must be implemented by all inheriting classes
        """
        pass


class RodeostatView(DeviceView):
    """ This class implements DeviceView for the specific Rodeostat device

        The on_method_changed method is called on method changing to load all necessary parameters and ui elements.

        Attributes:
            MethodDict (dict): A dictionary containing available measurement methods and
            the constructor of the controller
            method_menu (ttk.OptionMenu) The dropdown menu containing all avaialable methods
            port_menu (ttk.OptionMenu): Dropdown menu containing all scanned ports
            start_button (ttk.Button): The button object for the start button
            clear_button (ttk.Button): The button object for clearing the plots
            plotframe(PlotView): The view used for the plots

    """
    def __init__(self, master):
        """ Constructor for creating RodeostatViews

        The constructor will initialize all needed UI Elements (buttons, etc.)
        and load the first given method in MethodDict by calling on_method_changed initially
        without user interaction.

        Args:
            master(tk.Widget): The master widget containing this view

        """
        super().__init__(master)

        # Messverfahren
        self.MethodDict = {"Cyclo": Controller.Rodeostat.RodeostatController.CycloController,
                           "Squarewave": Controller.Rodeostat.RodeostatController.SquarewaveController}

        self.start_button = ttk.Button(self.buttonframe, text="Start Test", command=lambda: self.start_measurement())
        self.clear_button = ttk.Button(self.buttonframe, text="Clear Results", command=lambda: self.controller.clear())
        self.clear_port = ttk.Button(self.buttonframe, text="Clear Port", command=lambda: self.refresh())

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)

        self.rowconfigure(0)
        self.rowconfigure(0)
        self.rowconfigure(0)

        variable = tk.StringVar(self)
        methodframe = ttk.Frame(self)
        methodframe.grid(row=0, column=0, columnspan=2, sticky=tk.W, padx=5, pady=5)
        self.method_menu = ttk.OptionMenu(self, variable, list(self.MethodDict.keys())[0], *self.MethodDict.keys(),
                                          command=lambda var: self.on_method_changed(var))

        self.plotframe = PlotView(self, None)
        self.on_method_changed(list(self.MethodDict.keys())[0])  # Laden des default Wertes der Combobox

        # Variable for Callback
        methodlabel = Label(self, text="Measurement method:", font=('Calibri', 14))
        label = Label(self, text="Port", font=('Calibri', 14))
        label.pack(in_=self.portframe, side=tk.LEFT)

        self.port_menu = ttk.OptionMenu(self, self.controller.paramset.port[0], *self.controller.get_ports())
        self.port_menu.pack(in_=self.portframe, side=tk.LEFT)

        methodlabel.pack(in_=methodframe, side=tk.LEFT)
        self.method_menu.pack(in_=methodframe, side=tk.LEFT)

    def check_running(self):
        """ Method for handling the UI during test execution

        This method will disable parameters and buttons of the view as long as the background
        worker thread of the controller is alive. It will recall itself periodically
        until the controller finishes the measurement
        """
        widgets = [self.paramframe, self.buttonframe]
        if self.controller.worker.is_alive():
            self.plotframe.refresh = True
            self.after(0, self.plotframe.animate())
            for widget in widgets:
                for child in widget.children.values():
                    child["state"] = DISABLED
                self.after(1000, self.check_running)
        else:
            for widget in widgets:
                for child in widget.children.values():
                    child["state"] = NORMAL
                    self.plotframe.refresh = False

    def openFile(self):
        filepath = filedialog.askopenfilename()
        file = open(filepath, "r")
        self.controller.paramset.get()["textdata"] = ""  ###TODO filename + ".txt"
        file.close()

    def on_method_changed(self, methodname):
        """ This method handles the generation of the UI when the user chooses another measurement
        method of the device.

        First, the controller constructor is retrieved from MethoDict.
        Then the variable for storing the data which needs to be plotted is assigned from the controller.
        After cleaning up the widgets from the previous method, the UI elements are generated based on the Parameters
        of the controller

        Args:
            method (str): The measurement method that needs to be loaded. Should correspond to a key in MethodDict
        """

        # A) Controller des Typs MethodenameController() erzeugen
        self.controller = self.MethodDict[methodname]()
        self.plotframe.datavar = self.controller.data

        # B) Cleanup
        for widget in self.paramframe.grid_slaves():
            widget.grid_forget()

        # C) UI adaptions
        self.plotframe.grid(row=0, column=3, rowspan=len(vars(self.controller.paramset)), padx=5, pady=10,
                            sticky=tkinter.W + tkinter.E)
        self.buttonframe.grid(row=len(vars(self.controller.paramset)) - 9, column=0)

        self.start_button.pack(in_=self.buttonframe, side=tk.LEFT)
        self.clear_button.pack(in_=self.buttonframe, side=tk.LEFT)
        self.clear_port.pack(in_=self.buttonframe, side=tk.LEFT)

        # D) Generate UI Elements
        for row, (value, validation, label, tooltip) in enumerate(self.controller.get_parameters()):
            # 1) Get values from self.controller.get_parameters()
            # 2) Generate the UI Row by calling generate_param_element()
            self.generate_param_element(row, value, label, tooltip, validation)

    def selected_port(self, port):
        self.controller.paramset["serialport"] = port
