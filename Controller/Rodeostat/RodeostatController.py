import io
from io import BytesIO

import serial.tools.list_ports
from potentiostat import Potentiostat

from Model.DictVar import DictVar
from Model.VoltaMetricParamset import *
from Util import Localization


class RodeostatController:  # Gerätecontroller
    def __init__(self):
        self.paramset = None
        self.data = DictVar(name="plotdata",value=dict())

    def start_test(self):
        raise NotImplementedError('Please implement the start method before using your Rodeostat controller')

    def get_port(self):
        return [port for port, desc, hwid in sorted(serial.tools.list_ports.comports())]

    def get_parameters(self):
        result = []
        for param, value in vars(self.paramset).items():
            result.append((value, Localization.LocalizationDict[value._name]))
            # Erzeugt Tupel(Stringvar,Tupel(string,string)), mit StringVar für die Entrybox und Label und
            # Hovertiptext aus dem Localization Dict )
        return result

    def clear(self):
        self.data.set({})

class CycloController(RodeostatController):  # Testmethoden des Geräts
    def __init__(self):
        super().__init__()
        # TODO Hier die View reinbuttern
        self.paramset = CycloParamset()

    def start_test(self):
        # Hier könnten deine Library Aufrufe stehen
        # Später extra Thread, wegen UI blockiert und so digga
        amplitude = (int(self.paramset.volt_max.get())) - (int(self.paramset.volt_min.get())) / 2.0
        offset = (int(self.paramset.volt_max.get())) + (int(self.paramset.volt_min.get())) / 2.0
        period_ms = float(1000 * 4 * float(amplitude) / float(self.paramset.volt_second.get()))



        #Testdaten only
        testdata = [x.strip().split(",") for x in open("data.txt", "r").readlines()]
        for t, v, v2 in testdata:
            data = self.data.get()
            data[t] = v
            self.data.set(data)
        ###HIER RODEOSTAT GEDÖNS
           #1 Messen

           #2 Messdaten anch self.data.set(0 schreiben

class SquarewaveController(RodeostatController):  # Testmethoden des Geräts
    def __init__(self):
        super().__init__()
        self.paramset = SquareWaveParamset()

    def start_test(self):
        # Parameter holen und loslegen
        # Create potentiostat object and set current range, sample rate and test parameters
        dev = Potentiostat("COM1", timeout=20)
        dev.set_curr_range(self.paramset.current_range.get())
        dev.set_sample_rate(self.paramset.sampleRate.get())
        dev.set_param(self.paramset.testname.get(), "TODO")  # TODO

        filestream = io.StringIO("")

        # Run cyclic voltammetry test
        t, volt, curr = dev.run_test(self.paramset.testname.get(), display='pbar', filename=filestream)

        # TODO Hier müssen wir Multithreaden

        # Convert values to scipy arrays
        t = scipy.array(t)
        volt = scipy.array(volt)
        curr = scipy.array(curr)

        # Remove values during quiet time
        ind = t > test_param['quietTime'] * 1.0e-3
        t, volt, curr = t[ind], volt[ind], curr[ind]
        t = t - t[0]

        # plot results using matplotlib
        plt.figure(1)
        plt.subplot(211)
        plt.plot(t, volt)
        plt.ylabel('potential (V)')
        plt.grid('on')

        plt.subplot(212)
        plt.plot(t, curr)
        plt.ylabel('current (uA)')
        plt.xlabel('time (sec)')
        ymin = min(curr.min(), 0)
        ymax = max(curr.max(), 0)
        dy = ymax - ymin
        ymax += 0.1 * dy
        ymin -= 0.1 * dy
        plt.ylim(ymin, ymax)
        plt.grid('on')

        plt.figure(2)
        plt.plot(volt, curr)
        plt.xlabel('potential (V)')
        plt.ylabel('current (uA)')
        plt.ylim(ymin, ymax)
        plt.grid('on')

        plt.show()
