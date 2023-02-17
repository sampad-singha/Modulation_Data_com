import matplotlib.pyplot as plt

time = []
voltage = []
bits = [0, 1, 0, 0, 1, 1, 1, 0]
sampling_rate = 1000
sample_time = 1/sampling_rate

for i in range(len(bits)):
    time += [i*sample_time, (i+0.5)*sample_time]
    time += [(i+0.5)*sample_time, (i+1)*sample_time]

for bit in bits:
    if bit == 0:
        voltage += [-1, -1]
        voltage += [0, 0]
    else:
        voltage += [1, 1]
        voltage += [0, 0]

plt.plot(time, voltage)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.title('Unipolar NRZ-L')
plt.ylim(-1.5, 1.5)
plt.axhline(0)
plt.show()
