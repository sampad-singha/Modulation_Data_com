import matplotlib.pyplot as plt

# create a list of bits
bits = [1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0]

# set the bit duration and sampling rate
bit_duration = 12  # in seconds
sampling_rate = 1000  # in Hz

# calculate the time for each sample
time_per_sample = 1 / sampling_rate

# create a list of time values for each sample
time = []
for i in range(len(bits)):
    time += [j * time_per_sample for j in range(i, i+2)]

# create a list of voltage levels for each sample
voltage = []
for bit in bits:
    if bit == 1:
        voltage += [1, 1]
    else:
        voltage += [0, 0]

# plot the unipolar NRZ signal
plt.plot(time, voltage)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.title('Unipolar NRZ Signal')
plt.ylim([-0.5, 1.5])
plt.show()
