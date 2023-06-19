# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 12:50:43 2023

@author: yesed
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy import signal

b,a = signal.cheby2(4, 40, 100, 'low', analog = True)
w,h = signal.freqs(b,a)

plt.plot(w, 20*np.log10(abs(h)))
plt.xscale('log')
plt.title('Chebysev Type 2 Frequency Response (rs=40)')
plt.xlabel('Frequency (Rad/Second)')
plt.ylabel('Amplitude (dB)')
plt.margins(0, 0.2)
plt.grid(which = 'both', axis = 'both')
plt.axvline(100, color='red')
plt.axhline(-40, color='red')