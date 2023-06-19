# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 12:17:06 2023

@author: yesed
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy import signal

b,a = signal.cheby1(4, 5, 100, 'low', analog=True)
w,h = signal.freqs(b, a)

plt.plot(w, 20*np.log10(abs(h)))
plt.xscale('log')
plt.title('Chebysev Type 1 Frequency Response (rp=5)')
plt.xlabel('Frequency (rad/sec)')
plt.ylabel('Amplitude (dB)')
plt.margins(0, 0.1)
plt.grid(which = 'both', axis = 'both')
plt.axvline(100, color = 'green')
plt.axhline(-5, color = 'green')