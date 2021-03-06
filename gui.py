from tkinter import *
from tkinter import filedialog, Button
from tkinter import ttk
from idlelib.tooltip import Hovertip
import matplotlib.pyplot as plt
from potentiostat import Potentiostat
import serial


root = Tk() #Erstellung des Hauptfensters
root.title("Hegewald - Rodeostat") #Title des Hauptfensters
root.geometry("600x400") #Größe des Hauptfensters

maintab = ttk.Notebook(root) #Erstellung eines "Maintabs" in root
cyclovolt = Frame(maintab) #Erstellung des Punktes "Cyclovolt" in Maintab
squarevolt = Frame(maintab) #Erstellung des Punktes "Squarevolt" in Maintab

maintab.add(cyclovolt, text = "Cyclovoltametrie") #Hinzufügen des Punktes "Cyclovoltametrie" in Maintab
maintab.add(squarevolt, text = "Squarewave-Voltametrie") #Hinzufügen des Punktes "Squarewave-Voltametrie" in Maintab
maintab.grid(row = 0, column = 0)

def create_label(root,text,font,row,column,padx,pady):
    label = Label(root, text = text, font=font)
    label.grid(row = row, column = column, padx = 0, pady = 0)
    return label
def create_entry(root,width,borderwidth,row, column):
    entry = Entry(root, width = width, borderwidth = borderwidth)
    entry.grid(row = row, column = column,)
    return entry


def callback(input):
    if input.isdigit():
        print(input)
        return True

    elif input is "":
        print(input)
        return True

    else:
        print(input)
        return False
getcycurrentRange, getcysampleRate, getvoltMin, getvoltMax, getvoltpersecond,getshift,getnumCycle, getquietValue, getquietTime=0,0,0,0,0,0,0,0,0
def cybestätigen():
    global getcycurrentRange, getcysampleRate, getvoltMin, getvoltMax,getvoltpersecond,getshift,getnumCycle, getquietValue, getquietTime
    getcycurrentRange = cycurrentRange.get()
    getcysampleRate =cysampleRate.get()
    getvoltMin = voltMin.get()
    getvoltMax = voltMax.get()
    getvoltpersecond = voltpersecond.get()
    getshift = shift.get()
    getnumCycle= numCycle.get()
    getquietValue = quietValue.get()
    getquietTime = quietTime.get()

def startMessung():
    pass
def stopMessung():
    pass
def clearMessung():
    pass

def get_ports():
    return [port for port, desc, hwid in sorted(serial.tools.list_ports.comports())]

#Labels & Entryboxes
######################Cyclovoltametrie
cycurrentRangeLabel = create_label(cyclovolt,"currentRange: ",("Arial", 12), 1, 0,(2,5),(2,5))
cycurrentRange = create_entry(cyclovolt, 15, 3, 1, 1)
cycurrentRangeTip = Hovertip(cycurrentRange,'Der Parameter currentRange beschreibt den Strombereich an der Y-Achse im Voltagramm.\nEs ist eine currentRange zwischen -100µA und 100µA möglich!')

cysampleRateLabel = create_label(cyclovolt,"sampleRate: ",("Arial", 12), 2, 0,(2,5),(2,5))
cysampleRate = create_entry(cyclovolt, 15, 3, 2, 1)
cysampleRateTip = Hovertip(cysampleRate,'Der Parameter sampleRate beschreibt die Abtastraste der Messung (Hz). Hinweis: Die Abtastrate ist 1/sample_period in Sekunden.')

voltMinLabel = create_label(cyclovolt,"voltMin: ",("Arial", 12), 3, 0,(2,5),(2,5))
voltMin = create_entry(cyclovolt, 15, 3, 3, 1)
voltMinTip = Hovertip(voltMin,'Der Parameter voltMin beschreibt die minimalste Spannung im Potential-Zeit-Diagramm und legt somit den Anfangs- und Endpunkt der Kurve fest.\n Die Amplitude resultiert aus (voltMax-voltMin)/2.')

voltMaxLabel = create_label(cyclovolt,"voltMax: ",("Arial", 12), 4, 0,(2,5),(2,5))
voltMax = create_entry(cyclovolt, 15, 3, 4, 1)
voltMaxTip = Hovertip(voltMax,'Der Parameter voltMax beschreibt die maximale Spannung im Potential-Zeit-Diagramm und legt somit den Peak der Kurve fest.\n Die Amplitude resultiert aus (voltMax-voltMin)/2.')

voltpersecondLabel = create_label(cyclovolt, "volt_per_second: ",("Arial", 12), 5, 0,(2,5),(2,5))
voltpersecond = create_entry(cyclovolt, 15,3,5,1)
voltpersecondTip = Hovertip(voltpersecond, "sdsadas")

shiftLabel = create_label(cyclovolt,"Shift: ",("Arial", 12), 6, 0,(2,5),(2,5))
shift = create_entry(cyclovolt, 15, 3, 6, 1)
shiftTip = Hovertip(voltMax,'Der Parameter shift gibt die Phasenverschiebung der Kurve an der X-Achse an.\n 0 = keine Phasenverschiebung, 0,5 = 180° Phasenverschiebung')

numCycleLabel = create_label(cyclovolt, "numCycle: ",("Arial", 12), 7,0,(2,5),(2,5))
numCycle = create_entry(cyclovolt, 15, 3, 7, 1)
numCycleTip = Hovertip(numCycle,"Der Parameter numCycle gibt die Anzahl der Zyklen/Perioden an.\nEin Zyklus entspricht erst ein linear ansteigendes oder abfallendes Potential und anschließend ein rückläufiges Potential.")

quietValueLabel = create_label(cyclovolt, "quietValue: ",("Arial", 12), 8, 0,(2,5),(2,5))
quietValue = create_entry(cyclovolt, 15, 3, 8, 1)
quietValueTip = Hovertip(quietValue,"Der Parameter quietValue gibt an, ab welchem Potential die Cyclovoltametrie beginnen soll\n Dies ist ein optionaler Wert.")

quietTimeLabel = create_label(cyclovolt, "quietTime: ",("Arial", 12), 9, 0, (2,5),(2,5))
quietTime = create_entry(cyclovolt, 15, 3, 9, 1)
quietTimeTip = Hovertip(quietTime,"Der Parameter quietTime gibt an, wie lange der quietValue-Wert gehalten werden soll.\n Die ist ein optionaler Wert.")

###################Squarewave
sqcurrentRangeLabel = create_label(squarevolt,"currentRange: ",("Arial", 12), 1, 0,(2,5),(2,5))
sqcurrentRange = create_entry(squarevolt, 15, 3, 1, 1)
sqcurrentRangeTip = Hovertip(sqcurrentRange,'Der Parameter currentRange beschreibt den Strombereich an der Y-Achse im Voltagramm.\nEs ist eine currentRange zwischen -100µA und 100µA möglich!')

sqsampleRateLabel = create_label(squarevolt,"sampleRate: ",("Arial", 12), 2, 0,(2,5),(2,5))
sqsampleRate = create_entry(squarevolt, 15, 3, 2, 1)
sqsampleRateTip = Hovertip(sqsampleRate,'Der Parameter sampleRate beschreibt die Abtastraste der Messung (Hz). Hinweis: Die Abtastrate ist 1/sample_period in Sekunden.')

sqquietValueLabel = create_label(squarevolt, "quietValue: ",("Arial", 12), 3, 0,(2,5),(2,5))
sqquietValue = create_entry(squarevolt, 15, 3, 3, 1)
sqquietValueTip = Hovertip(sqquietValue,"Der Parameter quietValue gibt an, ab welchem Potential die Cyclovoltametrie beginnen soll\n Dies ist ein optionaler Wert.")

sqquietTimeLabel = create_label(squarevolt, "quietTime: ",("Arial", 12), 3, 0, (2,5),(2,5))
sqquietTime = create_entry(squarevolt, 15, 3, 3, 1)
sqquietTimeTip = Hovertip(sqquietTime,"Der Parameter quietTime gibt an, wie lange der quietValue-Wert gehalten werden soll.\n Die ist ein optionaler Wert.")

amplitudeLabel = create_label(squarevolt, "Amplitude: ",("Arial", 12), 4, 0, (2,5),(2,5))
amplitude = create_entry(squarevolt, 15, 3, 4, 1)
amplitudeTip = Hovertip(sqquietTime,"Der Parameter quietTime gibt an, wie lange der quietValue-Wert gehalten werden soll.\n Die ist ein optionaler Wert.")

startValueLabel = create_label(squarevolt, "startValue: ",("Arial", 12), 5, 0, (2,5),(2,5))
startValue = create_entry(squarevolt,15, 3, 5, 1)
startValueTip = Hovertip(startValue, "Später")

finalValueLabel = create_label(squarevolt, "finalValue: ",("Arial", 12), 6, 0, (2,5),(2,5))
finalValue = create_entry(squarevolt,15, 3, 6, 1)
finalValueTip = Hovertip(finalValue, "Später")

stepValueLabel = create_label(squarevolt, "stepValue: ",("Arial", 12), 7, 0, (2,5),(2,5))
stepValue = create_entry(squarevolt, 15, 3, 7, 1)
stepValueTip = Hovertip(stepValue, "Später")

#buttons
Bestätigung = Button(cyclovolt,text = "Bestätigen", command = cybestätigen, padx = 5, pady = 5)
Bestätigung.grid(row = 10, column = 1)
BestätigungTip = Hovertip(Bestätigung, "Alle Parameter werden eingelesen.\nErst dann kann die Messung gestartet werden.")
Start = Button(cyclovolt, text = "Messung starten!",command = startMessung, padx = 5, pady = 5)
Start.grid(row = 11, column = 1)
StartTip = Hovertip(Start, "Die Messung wird gestartet")
Stop = Button(cyclovolt, text = "Messung stoppen",command = stopMessung,padx = 5, pady = 5)
Stop.grid(row = 12, column = 1)
StopTip = Hovertip(Stop, "Die Messung wird gestoppt")
Clear = Button(cyclovolt, text = "Clear",command = clearMessung,padx = 5,pady = 5)
Clear.grid(row = 13, column = 1)
ClearTip = Hovertip(Clear,"Die Messung wird ")


#Befehle für den Menüleistenpunkt "File"
def openFile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, "r")
    print(file.read())
    file.close()
def saveFile():
    print("File is saved")



menüleiste = Menu(root) #Erstellung
root.config(menu = menüleiste) #Integrierung
file = Menu(menüleiste, tearoff = 0) #Erstellung des Menüpunktes "file"
menüleiste.add_cascade(label = "File", menu=file) # Integrierung des Menüpunktes "file" in der Menüleiste
#Optionen in File
file.add_command(label = "Open",command = openFile)
file.add_command(label = "Save",command = saveFile)
file.add_separator()
file.add_command(label = "Exit", command=quit)

#Punkt Interface in der Menüleiste
interface = Menu(menüleiste,tearoff = 0)
menüleiste.add_cascade(label = "Interface", menu = interface)

root.mainloop()