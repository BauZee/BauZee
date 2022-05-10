from Model.VoltaMetricParamset import *
from Util import Localization


class RodeostatController: # Gerätecontroller
    def __init__(self):
        self.paramset = None
        self.data = {}

    def start_test(self):
        raise NotImplementedError('Please implement the start method before using your Rodeostat controller')

    def get_port(self):
        return [port for port, desc, hwid in sorted(serial.tools.list_ports.comports())]

    def get_parameters(self):
        result = []
        for param,value in vars(self.paramset).items():
            result.append((value,Localization.LocalizationDict[value._name]))
        return result

class CycloController(RodeostatController): #Testmethoden des Geräts
    def __init__(self):
        super().__init__()
        #TODO Hier die View reinbuttern
        self.paramset = CycloParamset()

    def start_test(self):
        #Hier könnten deine Library Aufrufe stehen
        #Später extra Thread, wegen UI blockiert und so digga
        amplitude = (int(self.paramset.volt_max.get())) - (int(self.paramset.volt_min.get())) / 2.0
        offset = (int(self.paramset.volt_max.get())) + (int(self.paramset.volt_min.get())) / 2.0
        period_ms = float(1000 * 4 * float(amplitude) / float(self.paramset.volt_second.get()))


class SquarewaveController(RodeostatController): #Testmethoden des Geräts
    def __init__(self):
        super().__init__()
        self.paramset = SquareWaveParamset()


    def start_test(self):
        # Parameter holen und loslegen
        pass



