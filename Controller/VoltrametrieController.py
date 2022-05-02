class VoltametrieController:
    def __init__(self):
        self.method = None
        self.data = None

    def get_Value(self):
        """ This method will trigger a measurement of the given method"""
        pass
        #return messwert

class SquarewaveController(VoltametrieController):
    pass

class CycloController(VoltametrieController):
    pass

