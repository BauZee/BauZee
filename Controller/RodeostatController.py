
from Model.VoltaMetricParamset import *

class RodeostatController: # Gerätecontroller
    def __init__(self):
        self.paramset = None
        self.data = {}

    def start_test(self):
        pass

    def get_port(self):
        pass


class SquarewaveController(RodeostatController): #Testmethoden des Geräts
    def __init__(self):
        super(SquarewaveController, self).__init__()
        self.paramset = SquareWaveParamset(self.get_port())

    def start_test(self):
        # Parameter holen und loslegen
        pass


class CycloController(RodeostatController): #Testmethoden des Geräts

    def start_test(self):
        # Parameter holen und loslegen
        pass
