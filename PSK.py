import matplotlib.pyplot as plt
import numpy as np

bits = [0, 1, 0, 0, 1, 1, 1, 0]
Ac = 1
fc = 10
t = np.linspace(0, 1, 1000)
modulated_signal = []

for bit in bits:
    modulated_signal += Ac * np.cos(2 * np.pi * fc * t + bit*np.pi)

plt.plot(t, modulated_signal)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.ylim(-1.5, 1.5)
plt.show()
