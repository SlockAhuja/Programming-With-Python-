# Ahuja Slock   


import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import fftconvolve

def read_wav(p):
    sr, x = wavfile.read(p)
    x = x.astype(float)
    if np.max(np.abs(x)) > 1: x /= np.max(np.abs(x))
    return sr, x

def circ_conv(x, h):
    L = max(len(x), len(h))
    x = np.pad(x, (0, L-len(x)))
    h = np.pad(h, (0, L-len(h)))
    return np.real(np.fft.ifft(np.fft.fft(x)*np.fft.fft(h)))

sr1, x = read_wav(r"C:/Users/student/Desktop/audio.wav")
sr2, h = read_wav(r"C:/Users/student/Desktop/impulse.wav")

y_lin = fftconvolve(x, h, mode="full"); y_lin /= np.max(np.abs(y_lin))
y_circ = circ_conv(x, h); y_circ /= np.max(np.abs(y_circ))

plt.figure(figsize=(12,8))
plt.subplot(3,1,1); plt.plot(x); plt.title("Original")
plt.subplot(3,1,2); plt.plot(y_lin); plt.title("Linear Convolution")
plt.subplot(3,1,3); plt.plot(y_circ); plt.title("Circular Convolution")
plt.tight_layout(); plt.show()
