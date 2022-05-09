class VoltametricParamset:
    def __init__(self, port):
        self.port = port
        self.quietValue = 0
        self.quietTime = 0
        self.amplitude = 0.0
        self.sampleRate = 10

        self.paramset = {"Quiet Value": self.quietValue,
                         "Quiet Time": self.quietTime}

    def __getitem__(self, key):
        return self.paramset[key]

    def __setitem__ (self,key,value):
        self.paramset[key] = value

    def items(self):
        return self.paramset.items()


class CycloParamset(VoltametricParamset):
    def __init__(self, port):
        super().__init__(port)

        additional_params = {
            "Current Range": 1.0,
            "Sample Rate":  30.0,
            "Period": 0.0,
            'Num Cycles': 5.0,
            'Shift': 1.0,
        }

        for param_name, value in additional_params.items():
            self.paramset[param_name] = value


class SquareWaveParamset(VoltametricParamset):
    def __init__(self, port):
        super().__init__(port)
