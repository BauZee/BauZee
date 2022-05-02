from potentiostat import Potentiostat
import matplotlib.pyplot as plt
from gui import getcycurrentRange, getcysampleRate, getvoltMin, getvoltMax, getvoltpersecond,getshift,getnumCycle, getquietValue, getquietTime

port = "COM3"       # Serial port for potentiostat device
datafile = 'test.txt'       # Output file for time, curr, volt data

test_name = 'Cyclovoltametrie'        # The name of the test to run
curr_range = str(getcycurrentRange)        # The name of the current range [-100uA, +100uA]
sample_rate = getcysampleRate         # The number of samples/second to collect

volt_min = getvoltMin       # The minimum voltage in the waveform (V)
volt_max =  getvoltMax            # The maximum voltage in the waveform (V)
volt_per_sec = getvoltpersecond       # The rate at which to transition from volt_min to volt_max (V/s)
num_cycles = getnumCycle              # The number of cycle in the waveform

# Convert parameters to amplitude, offset, period, phase shift for triangle waveform
amplitude = (int(volt_max) - int(volt_min))/2.0            # Waveform peak amplitude (V)
offset = (int(volt_max) + int(volt_min))/2.0               # Waveform offset (V)
period_ms = float(1000*4*float(amplitude)/float(volt_per_sec))   # Waveform period in (ms)
shift = getshift                                      # Waveform phase shift - expressed as [0,1] number
                                                 # 0 = no phase shift, 0.5 = 180 deg phase shift, etc.

# Create dictionary of waveform parameters for cyclic voltammetry test
test_param = {
        'quietValue' : getquietValue,
        'quietTime'  : getquietTime,
        'amplitude'  : amplitude,
        'offset'     : offset,
        'period'     : period_ms,
        'numCycles'  : num_cycles,
        'shift'      : shift,
      }

# Create potentiostat object and set current range, sample rate and test parameters
dev = Potentiostat(port)
dev.set_curr_range(curr_range)
dev.set_sample_rate(sample_rate)
dev.set_param(test_name,test_param)

#Run cyclic voltammetry test

#def run():
   # t,volt,curr = dev.run_test(test_name,display='pbar',filename=datafile)
        #plt.figure(1)
        #plt.subplot(211)
        #plt.plot(t, volt)
        #plt.ylabel('potential (V)')
        #plt.grid('on')

        #plt.subplot(212)
        #plt.plot(t, curr)
        #plt.ylabel('current (uA)')
        #plt.xlabel('time (sec)')
        #plt.grid('on')

        #plt.figure(2)
        #plt.plot(volt, curr)
        #plt.xlabel('potential (V)')
        #plt.ylabel('current (uA)')
        #plt.grid('on')

        #plt.show()

# plot results using matplotlib

print(curr_range)
print(amplitude)
print(offset)
print(period_ms)