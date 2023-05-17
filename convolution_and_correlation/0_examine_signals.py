# -*- coding: utf-8 -*-
"""
Created on Tue May  2 02:12:57 2023

@author: yesed
"""

from matplotlib import pyplot as plt
import mysignals as sigs
from matplotlib import style

style.use("ggplot")
f, plt_arr = plt.subplots(2, sharex = True)
f.suptitle("Input signal and impulse response")
plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz)
plt_arr[1].plot(sigs.Impulse_response)
plt.show()