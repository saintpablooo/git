import numpy as np
from matplotlib import pyplot as plt
from scipy import signal

b,a = signal.ellip(4, 5, 40, 100, 'low', analog = True)
w,h = signal.freqs(b,a)

plt.plot(w, 20*np.log10(abs(h)))
plt.title('Elliptic filter frequency response (rp = 5, rs = 40)')
plt.xscale('log')
plt.xlabel('Frequency (rad/second)')
plt.ylabel('Amplitude (dB)')
plt.margins(0,0.2)
plt.grid(which = 'both', axis = 'both')
plt.axvline(100, color = 'magenta')
plt.axhline(-40, color = 'red')
plt.axhline(-5, color = 'green')

