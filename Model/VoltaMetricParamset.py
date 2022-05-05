class VoltametricParamset:
    def __init__(self, port):
        self.port = port
        self.quietValue = 0
        self.quietTime = 0
        self.amplitude = 0.0
        self.sampleRate = 10

        self.paramset = {"Quiet Value": self.quietValue,
                         "Quiet Time": self.quietTime }


class CycloParamset(VoltametricParamset):
    def __init__(self, port):
        super().__init__(port)

        self.current_range = None
        self.paramset = self.paramset + {
            "Current Range": self.current_range
        }


class SquareWaveParamset(VoltametricParamset):
    def __init__(self, port):
        super().__init__(port)
