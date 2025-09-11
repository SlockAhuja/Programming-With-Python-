# Ahuja Slock

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# Parameters
fs = 500  # Sampling frequency
f = 5     # Frequency of the signal
t = np.linspace(0, 1, fs, endpoint=False)  # Time array

triangular_wave = signal.sawtooth(2 * np.pi * f * t, 0.5)  # Triangular wave
ramp_signal = signal.sawtooth(2 * np.pi * f * t)           # Ramp (sawtooth) wave

plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(t, triangular_wave)
plt.title('Triangular Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(t, ramp_signal)
plt.title('Ramp Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')

plt.tight_layout()
plt.show()
