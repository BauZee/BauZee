import re
from idlelib.tooltip import Hovertip
from tkinter import StringVar
import serial.tools.list_ports
from Util import Localization

#Model =
#Erstellung von Parametern
#Speicherung und Halten von Value
# Parameter Name -> Zugriff auf Localisationdict
#Vererbung


class Validation:
    def __init__(self):
        self.UpperBound = None
        self.LowerBoud = None

    def validate(self,value,widget):
        pass

    def on_invalid(self, widget):
        pass

class IntValidation(Validation):
    def __init__(self,lower,upper):
        super(IntValidation, self).__init__()
        self.UpperBound = upper
        self.LowerBoud = lower

    def validate(self, value, widget):
        if value == "": return False
        isvalid = False

        if re.search("^(0|(-)?[1-9][0-9]*)$", value):
            integer = int(value)
            isvalid = self.UpperBound >= integer >= self.LowerBoud

        if not isvalid:
            widget.config(fg='red')
            return False

        widget.config(fg='black')
        return True

class FloatValidation(Validation):
    def __init__(self,lower,upper):
        super(FloatValidation, self).__init__()
        self.UpperBound = upper
        self.LowerBoud = lower

    def validate(self, value, widget):
        if value == "": return False
        isvalid = False

        if re.search("^(0|[1-9][0-9]*)$", value):
            integer = float(value)
            isvalid = self.UpperBound >= integer >= self.LowerBoud

        if not isvalid:
            widget.config(fg='red')
            return False

        widget.config(fg='black')
        return True

class VoltametricParamset:
    def __init__(self,testname):
        self.textdata = (StringVar(value = "data.txt", name = "textdata"), None)
        self.port = (StringVar(value="COM1", name="serialport"), None)
        self.testname = (StringVar(value=testname, name="testname"), None)
        self.quietValue = (StringVar(value="0", name="quietvalue"), IntValidation(-10,10))
        self.quietTime = StringVar(value="0", name="quiettime"), None
        self.sampleRate = StringVar(value="100.0", name="samplerate"), None
        self.curr_range = StringVar(value="100uA", name="curr_range"), None


class CycloParamset(VoltametricParamset):
    def __init__(self):
        super().__init__("cyclic")
        self.volt_max = StringVar(value="1.0", name="voltmax"), None
        self.volt_min = StringVar(value="-0.1", name="voltmin"), None
        self.num_cycles = StringVar(value="1", name="numcycles"), None
        self.volt_second = StringVar(value="2.050", name="volts"), None
        self.shift = StringVar(value="0", name="shift"), None


class SquareWaveParamset(VoltametricParamset):
    def __init__(self):
        super().__init__("squareWave")
        self.amplitude = StringVar(value="0.05", name="amplitude")
        self.start_value = StringVar(value="-0.4", name="startvalue")
        self.final_value = StringVar(value="0.2", name="finalvalue")
        self.step_value = StringVar(value="0.005", name="stepvalue")
        self.sample_window = StringVar(value="0.2", name="samplewindow")
