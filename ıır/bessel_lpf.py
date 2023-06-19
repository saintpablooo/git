import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
from scipy import signal 

b,a = signal.butter(4,100, 'low', analog = True)
w,h = signal.freqs(b, a)

style.use('dark_background')
plt.plot(w, 20*np.log10(abs(h)), color = 'blue', ls = 'dashed')

b,a = signal.bessel(4, 100, 'low', analog = True)
w,h = signal.freqs(b, a)

plt.plot(w, 20*np.log10(abs(h)))
plt.xscale('log')
plt.title("Bessel filter frequency response (with Butterworth)")
plt.xlabel('Frequency (rad/second)')
plt.ylabel('Amplitude (dB)')
plt.margins(0, 0.2)
plt.grid(which='both', axis='both')
plt.axvline(100, color = 'green')
plt.show()