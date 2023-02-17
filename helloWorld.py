import numpy as np
import matplotlib.pyplot as plt

# Define the signal parameters
f_c = 1000  # Carrier frequency (Hz)
f_m = 10  # Modulating frequency (Hz)
T_b = 1 / f_m  # Bit duration (s)
A_c = 1  # Carrier amplitude
num_bits = 16  # Number of bits to transmit
bit_stream = np.random.randint(2, size=num_bits)  # Random binary bit stream

# Generate the time array
t_step = T_b / 10
t = np.arange(0, num_bits * T_b, t_step)

# Generate the carrier waveform
c_t = A_c * np.sin(2 * np.pi * f_c * t)

# Generate the BPSK waveform
bpsk_t = []
for bit in bit_stream:
    if bit == 1:
        bpsk_t += A_c * np.sin(2 * np.pi * f_c * t + np.pi)
    else:
        bpsk_t += A_c * np.sin(2 * np.pi * f_c * t)

# Plot the waveforms
fig, ax = plt.subplots()
ax.plot(t, c_t, label='Carrier Signal')
ax.plot(t, bpsk_t, label='BPSK Signal')
ax.set_xlabel('Time (s)')
ax.set_ylabel('Amplitude')
ax.set_title('BPSK Modulation')
ax.legend()
plt.show()
