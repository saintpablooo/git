import numpy as np
from matplotlib import pyplot as plt
from scipy import signal

b = signal.firwin(80,0.5, window=("kaiser",8))

w, h = signal.freqz(b)
plt.semilogy(w, np.abs(h), 'g')
plt.ylabel('Amplitude (dB)', color = 'b')
plt.xlabel('Frequency (rad/sample)')
plt.show()
