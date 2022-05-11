import tkinter
from tkinter import Tk
from tkinter import ttk

from View.RodeostatView import RodeostatView, DeviceView


class PyjamaParty(Tk):
    def __init__(self):
        super().__init__()  # Erstellung des Hauptfensters
        # Erstellung eines "Maintabs" in root
        self.title("PyjamaPartGUI")  # Title des Hauptfensters
        self.geometry("800x500")  # Größe des Hauptfensters


        self.view = None
        self.mainTab = ttk.Notebook(self)
        self.create_tabs()
        self.create_main_menu()

        self.configure()

    def create_main_menu(self):
        pass

    def create_tabs(self):
        self.mainTab.grid(row=0, column=0, sticky=tkinter.N + tkinter.E)

        # Rodeostat
        rodeo_tab = RodeostatView(self.mainTab)
        self.mainTab.add(rodeo_tab, text="Rodeostat")

        # Random new Device
        device_tab = DeviceView(self.mainTab)
        self.mainTab.add(device_tab, text="Generic Device")
        self.mainTab.pack(fill="both", expand=1)

        # Event Binding for controller assignment
        self.mainTab.bind("<<NotebookTabChanged>>", self.tab_changed)

    def tab_changed(self, event):
        """" This methods is the event handler for changes in the main tab"""
        selected_index = event.widget.index("current")
        self.view = event.widget.tab(selected_index)




# # Befehle für den Menüleistenpunkt "File"
# def openFile():
#     filepath = filedialog.askopenfilename()
#     file = open(filepath, "r")
#     print(file.read())
#     file.close()
#
#
# def saveFile():
#     print("File is saved")
#
#
# menüleiste = Menu(root)  # Erstellung
# root.config(menu=menüleiste)  # Integrierung
# file = Menu(menüleiste, tearoff=0)  # Erstellung des Menüpunktes "file"
# menüleiste.add_cascade(label="File", menu=file)  # Integrierung des Menüpunktes "file" in der Menüleiste
# # Optionen in File
# file.add_command(label="Open", command=openFile)
# file.add_command(label="Save", command=saveFile)
# file.add_separator()
# file.add_command(label="Exit", command=quit)
#
# # Punkt Interface in der Menüleiste
# interface = Menu(menüleiste, tearoff=0)
# menüleiste.add_cascade(label="Interface", menu=interface)
#
# root.mainloop()
