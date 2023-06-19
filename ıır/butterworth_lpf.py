# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 18:46:32 2023

@author: yesed
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy import signal

b,a = signal.butter(4, 100, 'low', analog = True)
w,h = signal.freqs(b,a)

plt.plot(w, 20*np.log10(abs(h)))
plt.xscale('log')

plt.title('Butterworth Low Pass Filter')
plt.xlabel('Frequency (rad/sec)')
plt.ylabel('Amplitude (db)')
plt.margins(0,0.2)
plt.grid()
plt.axvline(100, color='green')
plt.style.use('dark_background')
