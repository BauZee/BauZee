currentRangeTip = "Der Parameter currentRange beschreibt den Strombereich an der Y-Achse im Voltagramm.\nEs " \
                  "ist eine currentRange zwischen -100µA und 100µA möglich! "
sampleRateTip = "Der Parameter sampleRate beschreibt die Abtastraste der Messung (Hz). Hinweis: Die Abtastrate " \
                "ist 1/sample_period in Sekunden. "
quietTimeTip = "Der Parameter quietTime gibt an, wie lange der quietValue-Wert gehalten werden soll." \
               "\n Dies ist ein optionaler Wert. "
quietValueTip = "Der Parameter quietValue gibt an, ab welchem Potential die Squarewave-Voltametrie beginnen " \
                "soll\n " \
                   "Dies ist ein optionaler Wert. "
AmplitudeTip = "Der Parameter Amplitude gibt an, den Höchstwert der Rechteckwelle pro Zyklus!"
startValueTip = "Der Parameter Start Value gibt an, bei welchem Potential der Rechteckimpuls beginnen soll. "
finalValueTip = "Der Parameter Final Value gibt an, bei welchem Potential der Rechteckimpuls enden soll. "
stepValueTip = "Der Parameter stepValue gibt  an, um wie viel  sich  das Potential nach jedem Zyklus erhöhen soll."
windowTip = "fraction of half cycle used for sample"
serialportTip = ""
testnameTip= ""
Current_RangeTip = "Der Parameter currentRange beschreibt den Strombereich an der Y-Achse im Voltagramm.\nEs ist eine currentRange zwischen -100µA und 100µA möglich!"
Sample_RateTip = "'Der Parameter sampleRate beschreibt die Abtastraste der Messung (Hz). Hinweis: Die Abtastrate ist 1/sample_period in Sekunden."
ShiftTip = "Der Parameter shift gibt die Phasenverschiebung der Kurve an der X-Achse an.\n 0 = keine Phasenverschiebung, 0,5 = 180° Phasenverschiebung"
NumCycleTip = "Der Parameter numCycle gibt die Anzahl der Zyklen/Perioden an.\nEin Zyklus entspricht erst ein linear ansteigendes oder abfallendes Potential und anschließend ein rückläufiges Potential."
Volt_MinTip = "Der Parameter voltMin beschreibt die minimalste Spannung im Potential-Zeit-Diagramm und legt somit den Anfangs- und Endpunkt der Kurve fest.\n Die Amplitude resultiert aus (voltMax-voltMin)/2.'"
Volt_MaxTip = "Der Parameter voltMax beschreibt die maximale Spannung im Potential-Zeit-Diagramm und legt somit den Peak der Kurve fest.\n Die Amplitude resultiert aus (voltMax-voltMin)/2."
Volt_SecondTip= "Der Parameter V/s gibt an, wie um wie viel Volt sich das Potential pro Sekunde verändert"
Sample_WindowTip= ""

LocalizationDict = {
    "testname": ("Test Name",testnameTip),
    "voltmax": ("Volt Max",Volt_MaxTip),
    "voltmin": ("Volt Min",Volt_MinTip),
    "serialport": ("Serial Port", serialportTip),
    "quietvalue": ("Quiet Value", quietValueTip),
    "quiettime": ("Quiet Time", quietTimeTip),
    "samplerate": ("Sample Rate", sampleRateTip),
    "startvalue": ("Start Value",startValueTip),
    "samplewindow": ("Sample Window",Sample_WindowTip),
    "finalvalue": ("Final Value",finalValueTip),
    "stepvalue": ("Step Value",stepValueTip),
    "amplitude": ("Amplitude",AmplitudeTip),
    "numcycles": ("Number Cycles", NumCycleTip),
    "volts": ("Volt/s", Volt_SecondTip),
    "shift": ("Shift",ShiftTip),
    "currentrange" : ("Current Range",Current_RangeTip)
}
