import matplotlib.pyplot as plt
import numpy as np

# carrier signal
fc = 1000
Ac = 1
t = np.linspace(0, 0.2, 1000)
carrier_signal = Ac * np.sin(2 * np.pi * fc * t)

# message signal
fm = 4
Am = 0.5
message_signal = Am * np.sin(2 * np.pi * fm * t)

kp = (2 * np.pi) / 180

# modulated signal
modulated_signal = Ac * np.sin(2 * np.pi * fc * t + kp * message_signal)

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
