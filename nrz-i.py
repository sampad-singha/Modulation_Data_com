import matplotlib.pyplot as plt

sampling_rate = 1000
sample_time = 1/sampling_rate
time = []
voltage = []
bits = [0, 1, 0, 0, 1, 1, 1, 00]

for i in range(len(bits)):
    time += [i*sample_time, (i+1)*sample_time]

prev_volt = 1
for bit in bits:
    if bit == 0:
        voltage += [prev_volt, prev_volt]
    else:
        voltage += [1, 1] if prev_volt == 0 else [0, 0]
        prev_volt = 1 if prev_volt == 0 else 0


plt.plot(time, voltage)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.title('Unipolar NRZ-I')
plt.ylim(-1, 1.5)
plt.axhline(0.5)
plt.show()
