import numpy as np
import matplotlib.pyplot as plt

# carrier signal
fc = 50
Ac = 0.5
t = np.linspace(0, 1, 10000)
carrier_signal = Ac * np.sin(2 * np.pi * fc * t)

# message signal
fm = 4
Am = 1
message_signal = Am * np.sin(2 * np.pi * fm * t)

kf = 10

# modulated signal
modulated_signal = Ac * np.sin(2 * np.pi * fc * t + kf * message_signal)

# plotting
plt.subplot(3, 1, 1)
plt.plot(t, carrier_signal, label='Carrier signal')
plt.subplot(3, 1, 2)
plt.plot(t, message_signal, label='Message signal')
plt.subplot(3, 1, 3)
plt.plot(t, modulated_signal, label='Modulated signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()
