class VoltametricParamset:
    def __init__(self, port):
        self.port = port
        self.quietValue = 0
        self.quietTime = 0
        self.amplitude = 0.0
        self.sampleRate = 10

        self.paramset = {"Quiet Value": self.quietValue,
                         "Quiet Time": self.quietTime}

    def items(self):
        return self.paramset.items()


class CycloParamset(VoltametricParamset):
    def __init__(self, port):
        super().__init__(port)

        self.current_range = 1.0
        additional_params = {
            "Current Range": self.current_range
        }

        for param_name, value in additional_params.items():
            self.paramset[param_name] = value


class SquareWaveParamset(VoltametricParamset):
    def __init__(self, port):
        super().__init__(port)
