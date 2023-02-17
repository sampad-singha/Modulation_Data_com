# Formula
# y(t) = (Ac + m(t)*sin(2*pi*fc*t)
import matplotlib.pyplot as plt
import numpy as np

#Carrier signal
fc = 50
Ac = 1
t = np.linspace(0, 1, 10000)
carrier_signal = Ac*np.sin(2*np.pi*fc*t)

#Message signal
fm = 4
Am = 0.5
message_signal = Am*np.sin(2*np.pi*fm*t)

#Modulated signal
modulated_signal = (Ac + message_signal)*np.sin(2*np.pi*fc*t)

#Plotting
plt.subplot(3, 1, 1)
plt.plot(t, carrier_signal, label='Carrier signal')
plt.subplot(3, 1, 2)
plt.plot(t, message_signal, label='Message signal')
plt.subplot(3, 1, 3)
plt.plot(t, modulated_signal, label='Modulated signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
