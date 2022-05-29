import io
import threading
from io import BytesIO
import time
from queue import Queue

import serial.tools.list_ports
from potentiostat import Potentiostat

from Model.DictVar import DictVar
from Model.VoltaMetricParamset import *
from Util import Localization

import scipy
import serial


class RodeostatController:  # Gerätecontroller
    def __init__(self):
        self.paramset = None
        self.data = DictVar(name="plotdata", value=dict())
        self.worker = None

    def start_test(self):
        raise NotImplementedError('Please implement the start method before using your Rodeostat controller')

    def get_parameters(self):
        result = []
        for param, value in vars(self.paramset).items():
            variable = value[0]
            validation = value[1]

            locale_info = Localization.LocalizationDict[variable._name]

            result.append((variable, validation, locale_info[0], locale_info[1]))
            # Erzeugt Tupel(Stringvar,Tupel(string,string)), mit StringVar für die Entrybox und Label und
            # Hovertiptext aus dem Localization Dict )
        return result

    def clear(self):
        self.data.set({})

    def get_ports(self):
        portlist = [port for port, desc, hwid in sorted(serial.tools.list_ports.comports())]
        if len(portlist) == 0:
            return ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6"]
        return portlist


class CycloController(RodeostatController):  # Testmethoden des Geräts
    def __init__(self):
        super().__init__()
        self.paramset = CycloParamset()

    def measure_data(self):
        # Hier könnten deine Library Aufrufe stehen
        # Später extra Thread, wegen UI blockiert und so digga
        # self.".start_button.config(state = "DISABLED")
        # amplitude = ((float(self.paramset.volt_max.get())) - (float(self.paramset.volt_min.get())) / 2.0)
        # test_param = {
        #    'quietValue': float(self.paramset.quietValue.get()),
        #    'quietTime': int(self.paramset.quietTime.get()),
        #    'amplitude': amplitude,
        #    'offset': (float(self.paramset.volt_max.get())) + float(self.paramset.volt_min.get()) / 2.0,
        #    'period': int(float(1000 * 4 * float(amplitude) / float(self.paramset.volt_second.get()))),
        #    'numCycles': int(self.paramset.num_cycles.get()),
        #    'shift': float(self.paramset.shift.get())
        # }
        # port = self.paramset.port.get()
        # dev = Potentiostat(port) #port
        # dev.set_curr_range(self.paramset.curr_range.get())
        # dev.set_sample_rate(float(self.paramset.sampleRate.get()))
        # dev.set_param(self.paramset.testname.get(), test_param)
        # t, volt, curr = dev.run_test(self.paramset.testname.get(), display='pbar',
        #                             filename=self.paramset.textdata.get())
        # dev.stop_test()
        time.sleep(5)
        testdata = [x.strip().split(",") for x in open(str(self.paramset.textdata[0].get()), "r").readlines()]
        for t, v, c in testdata:
            data = self.data.get()
            data[t] = [v, c]
            self.data.set(data)

    def start_test(self):
        self.worker = threading.Thread(target=self.measure_data)
        self.worker.start()


class SquarewaveController(RodeostatController):  # Testmethoden des Geräts
    def __init__(self):
        super().__init__()
        self.paramset = SquareWaveParamset()

    def start_test(self):
        test_param = {
            "quietValue": float(self.paramset.quietValue.get()),
            "quietTime": int(self.paramset.quietTime.get()),
            "amplitude": float(self.paramset.amplitude.get()),
            "startValue": float(self.paramset.start_value.get()),
            "finalValue": float(self.paramset.final_value.get()),
            "stepValue": float(self.paramset.step_value.get()),
            "window": float(self.paramset.sample_window.get())
        }

        # dev = Potentiostat(self.paramset.port.get(), timeout=20)
        # dev.set_curr_range(self.paramset.curr_range.get())
        # dev.set_sample_rate(float(self.paramset.sampleRate.get()))
        # dev.set_param(self.paramset.testname.get(), test_param)  # TODO

        # filestream = io.StringIO("")
        # Run cyclic voltammetry test
        # t, volt, curr = dev.run_test(self.paramset.testname.get(), display='pbar',
        # filename=self.paramset.textdata.get())

        # TODO Hier müssen wir Multithreaden -> fick mich

        # Convert values to scipy arrays
        # t = scipy.array(t)
        # volt = scipy.array(volt)
        # curr = scipy.array(curr)

        # Remove values during quiet time
        # ind = t > test_param['quietTime'] * 1.0e-3
        # t, volt, curr = t[ind], volt[ind], curr[ind]
        # t = t - t[0]

        testdata = [x.strip().split(",") for x in open(str(self.paramset.textdata.get()), "r").readlines()]
        for t, v, c in testdata:
            data = self.data.get()
            data[t] = v, c
            self.data.set(data)
