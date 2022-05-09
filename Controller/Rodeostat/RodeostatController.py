from Model.VoltaMetricParamset import *

class RodeostatController: # Gerätecontroller
    def __init__(self):
        self.paramset = None
        self.data = {}

    def start_test(self):
        raise NotImplementedError('Please implement the start method before using your Rodeostat controller')

    def get_port(self):
        return [port for port, desc, hwid in sorted(serial.tools.list_ports.comports())]


class CycloController(RodeostatController): #Testmethoden des Geräts
    def __init__(self):
        super().__init__()
        #TODO Hier die View reinbuttern
        self.paramset = CycloParamset(None)

    def start_test(self):
        #Hier könnten deine Library Aufrufe stehen
        #Später extra Thread, wegen UI blockiert und so digga
        pass


class SquarewaveController(RodeostatController): #Testmethoden des Geräts
    def __init__(self):
        super().__init__()
        self.paramset = SquareWaveParamset(None)


    def start_test(self):
        # Parameter holen und loslegen
        pass



