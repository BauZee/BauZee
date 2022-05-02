class VoltametricMethod:
    def __init__(self, port, name):
        self.port = port
        self.name = name
        self.quietValue = 0
        self.quietTime = 0
        self.amplitude = 0.0
        self.sampleRate = 10



class CycloVoltametrie(VoltametricMethod):
    def __init__(self, port):
        super().__init__(port, "Cyclovoltametrie")


        self.paramset = {
            "Current Range" : self.current_range
        }


class SquareWaveVoltametrie(VoltametricMethod):
    def __init__(self, port):
        super().__init__(port, "Squarewavevoltametrie")

