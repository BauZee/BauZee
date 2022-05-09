import tkinter
from tkinter import Tk, Frame, Label, Entry
from tkinter import ttk
from idlelib.tooltip import Hovertip
import matplotlib.pyplot as plt
import serial as serial
from potentiostat import Potentiostat
from View.RodeostatView import RodeostatView, DeviceView


class PyjamaParty(Tk):
    def __init__(self):
        super().__init__()  # Erstellung des Hauptfensters
        # Erstellung eines "Maintabs" in root
        self.title("PyjamaPartGUI")  # Title des Hauptfensters
        self.geometry("600x400")  # Größe des Hauptfensters
        self.view = None
        self.mainTab = ttk.Notebook(self)
        self.create_tabs()
        self.create_main_menu()

    def create_main_menu(self):
        pass

    def create_tabs(self):
        self.mainTab.grid(row=0, column=0, sticky=tkinter.N + tkinter.S + tkinter.W + tkinter.E)

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



# # Labels & Entryboxes
# ######################Cyclovoltametrie
# cycurrentRangeLabel = create_label(cyclovolt, "currentRange: ", ("Arial", 12), 1, 0, (2, 5), (2, 5))
# cycurrentRange = create_entry(cyclovolt, 15, 3, 1, 1)
# cycurrentRangeTip = Hovertip(cycurrentRange,
#                              'Der Parameter currentRange beschreibt den Strombereich an der Y-Achse im Voltagramm.\nEs ist eine currentRange zwischen -100µA und 100µA möglich!')
#
# cysampleRateLabel = create_label(cyclovolt, "sampleRate: ", ("Arial", 12), 2, 0, (2, 5), (2, 5))
# cysampleRate = create_entry(cyclovolt, 15, 3, 2, 1)
# cysampleRateTip = Hovertip(cysampleRate,
#                            'Der Parameter sampleRate beschreibt die Abtastraste der Messung (Hz). Hinweis: Die Abtastrate ist 1/sample_period in Sekunden.')
#
# voltMinLabel = create_label(cyclovolt, "voltMin: ", ("Arial", 12), 3, 0, (2, 5), (2, 5))
# voltMin = create_entry(cyclovolt, 15, 3, 3, 1)
# voltMinTip = Hovertip(voltMin,
#                       'Der Parameter voltMin beschreibt die minimalste Spannung im Potential-Zeit-Diagramm und legt somit den Anfangs- und Endpunkt der Kurve fest.\n Die Amplitude resultiert aus (voltMax-voltMin)/2.')
#
# voltMaxLabel = create_label(cyclovolt, "voltMax: ", ("Arial", 12), 4, 0, (2, 5), (2, 5))
# voltMax = create_entry(cyclovolt, 15, 3, 4, 1)
# voltMaxTip = Hovertip(voltMax,
#                       'Der Parameter voltMax beschreibt die maximale Spannung im Potential-Zeit-Diagramm und legt somit den Peak der Kurve fest.\n Die Amplitude resultiert aus (voltMax-voltMin)/2.')
#
# voltpersecondLabel = create_label(cyclovolt, "volt_per_second: ", ("Arial", 12), 5, 0, (2, 5), (2, 5))
# voltpersecond = create_entry(cyclovolt, 15, 3, 5, 1)
# voltpersecondTip = Hovertip(voltpersecond, "sdsadas")
#
# shiftLabel = create_label(cyclovolt, "Shift: ", ("Arial", 12), 6, 0, (2, 5), (2, 5))
# shift = create_entry(cyclovolt, 15, 3, 6, 1)
# shiftTip = Hovertip(voltMax,
#                     'Der Parameter shift gibt die Phasenverschiebung der Kurve an der X-Achse an.\n 0 = keine Phasenverschiebung, 0,5 = 180° Phasenverschiebung')
#
# numCycleLabel = create_label(cyclovolt, "numCycle: ", ("Arial", 12), 7, 0, (2, 5), (2, 5))
# numCycle = create_entry(cyclovolt, 15, 3, 7, 1)
# numCycleTip = Hovertip(numCycle,
#                        "Der Parameter numCycle gibt die Anzahl der Zyklen/Perioden an.\nEin Zyklus entspricht erst ein linear ansteigendes oder abfallendes Potential und anschließend ein rückläufiges Potential.")
#
# quietValueLabel = create_label(cyclovolt, "quietValue: ", ("Arial", 12), 8, 0, (2, 5), (2, 5))
# quietValue = create_entry(cyclovolt, 15, 3, 8, 1)
# quietValueTip = Hovertip(quietValue,
#                          "Der Parameter quietValue gibt an, ab welchem Potential die Cyclovoltametrie beginnen soll\n Dies ist ein optionaler Wert.")
#
# quietTimeLabel = create_label(cyclovolt, "quietTime: ", ("Arial", 12), 9, 0, (2, 5), (2, 5))
# quietTime = create_entry(cyclovolt, 15, 3, 9, 1)
# quietTimeTip = Hovertip(quietTime,
#                         "Der Parameter quietTime gibt an, wie lange der quietValue-Wert gehalten werden soll.\n Die ist ein optionaler Wert.")
#
# ###################Squarewave
# sqcurrentRangeLabel = create_label(squarevolt, "currentRange: ", ("Arial", 12), 1, 0, (2, 5), (2, 5))
# sqcurrentRange = create_entry(squarevolt, 15, 3, 1, 1)
# sqcurrentRangeTip = Hovertip(sqcurrentRange,
#                              'Der Parameter currentRange beschreibt den Strombereich an der Y-Achse im Voltagramm.\nEs ist eine currentRange zwischen -100µA und 100µA möglich!')
#
# sqsampleRateLabel = create_label(squarevolt, "sampleRate: ", ("Arial", 12), 2, 0, (2, 5), (2, 5))
# sqsampleRate = create_entry(squarevolt, 15, 3, 2, 1)
# sqsampleRateTip = Hovertip(sqsampleRate,
#                            'Der Parameter sampleRate beschreibt die Abtastraste der Messung (Hz). Hinweis: Die Abtastrate ist 1/sample_period in Sekunden.')
#
# sqquietValueLabel = create_label(squarevolt, "quietValue: ", ("Arial", 12), 3, 0, (2, 5), (2, 5))
# sqquietValue = create_entry(squarevolt, 15, 3, 3, 1)
# sqquietValueTip = Hovertip(sqquietValue,
#                            "Der Parameter quietValue gibt an, ab welchem Potential die Cyclovoltametrie beginnen soll\n Dies ist ein optionaler Wert.")
#
# sqquietTimeLabel = create_label(squarevolt, "quietTime: ", ("Arial", 12), 3, 0, (2, 5), (2, 5))
# sqquietTime = create_entry(squarevolt, 15, 3, 3, 1)
# sqquietTimeTip = Hovertip(sqquietTime,
#                           "Der Parameter quietTime gibt an, wie lange der quietValue-Wert gehalten werden soll.\n Die ist ein optionaler Wert.")
#
# amplitudeLabel = create_label(squarevolt, "Amplitude: ", ("Arial", 12), 4, 0, (2, 5), (2, 5))
# amplitude = create_entry(squarevolt, 15, 3, 4, 1)
# amplitudeTip = Hovertip(sqquietTime,
#                         "Der Parameter quietTime gibt an, wie lange der quietValue-Wert gehalten werden soll.\n Die ist ein optionaler Wert.")
#
# startValueLabel = create_label(squarevolt, "startValue: ", ("Arial", 12), 5, 0, (2, 5), (2, 5))
# startValue = create_entry(squarevolt, 15, 3, 5, 1)
# startValueTip = Hovertip(startValue, "Später")
#
# finalValueLabel = create_label(squarevolt, "finalValue: ", ("Arial", 12), 6, 0, (2, 5), (2, 5))
# finalValue = create_entry(squarevolt, 15, 3, 6, 1)
# finalValueTip = Hovertip(finalValue, "Später")
#
# stepValueLabel = create_label(squarevolt, "stepValue: ", ("Arial", 12), 7, 0, (2, 5), (2, 5))
# stepValue = create_entry(squarevolt, 15, 3, 7, 1)
# stepValueTip = Hovertip(stepValue, "Später")
#
# # buttons
# Bestätigung = Button(cyclovolt, text="Bestätigen", command=cybestätigen, padx=5, pady=5)
# Bestätigung.grid(row=10, column=1)
# BestätigungTip = Hovertip(Bestätigung,
#                           "Alle Parameter werden eingelesen.\nErst dann kann die Messung gestartet werden.")
# Start = Button(cyclovolt, text="Messung starten!", command=startMessung, padx=5, pady=5)
# Start.grid(row=11, column=1)
# StartTip = Hovertip(Start, "Die Messung wird gestartet")
# Stop = Button(cyclovolt, text="Messung stoppen", command=stopMessung, padx=5, pady=5)
# Stop.grid(row=12, column=1)
# StopTip = Hovertip(Stop, "Die Messung wird gestoppt")
# Clear = Button(cyclovolt, text="Clear", command=clearMessung, padx=5, pady=5)
# Clear.grid(row=13, column=1)
# ClearTip = Hovertip(Clear, "Die Messung wird ")
#
#
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
