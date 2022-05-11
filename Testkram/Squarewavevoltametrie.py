import scipy
import matplotlib.pyplot as plt
from potentiostat import Potentiostat

port = '/dev/ttyACM0'       # Serial port for potentiostat device
datafile = 'data.txt'       # Output file for time, curr, volt data
test_name = 'squareWave'    # The name of the test to run
curr_range = '10uA'         # The name of the current range [-100uA, +100uA]
sample_rate = 10.0          # The number of samples/second to collect


# Create dictionary of waveform parameters squarewave annodic stripping
test_param = {
        'quietValue' : -0.4,
        'quietTime'  :  500,
        'amplitude'  :  0.05,
        'startValue' : -0.4,
        'finalValue' :  0.2,
        'stepValue'  :  0.005,
        'window'     :  0.2,
        }

