from idlelib.tooltip import Hovertip
from tkinter import StringVar

from Util import Localization


class VoltametricParamset:
    def __init__(self, testname):
        self.port = StringVar(value="COM1", name="serialport")
        self.testname = StringVar(value=testname, name="testname")
        self.quietValue = StringVar(value=0, name="quietvalue")
        self.quietTime = StringVar(value=0, name="quiettime")
        self.sampleRate = StringVar(value=0, name="samplerate")


class CycloParamset(VoltametricParamset):
    def __init__(self):
        super().__init__("Cyclo")

        self.volt_max = StringVar(value="1", name="voltmax")
        self.volt_min = StringVar(value="-1", name="voltmin")
        self.num_cycles = StringVar(value="-1", name="numcycles")
        self.volt_second = StringVar(value="-1", name="volts")
        self.shift = StringVar(value="-1", name="shift")


class SquareWaveParamset(VoltametricParamset):
    def __init__(self):
        super().__init__("SquareWave")
        self.amplitude = StringVar(value=0, name="amplitude")
        self.start_value = StringVar(value=0, name="startvalue")
        self.final_value = StringVar(value="-1", name="finalvalue")
        self.step_value = StringVar(value="-1", name="stepvalue")
        self.sample_window = StringVar(value="-1", name="samplewindow")
