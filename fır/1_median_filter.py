# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 19:19:31 2023

@author: yesed
"""

from scipy import signal
from matplotlib import pyplot as plt
import mysignals as sigs

median_filter_output = signal.medfilt(sigs.InputSignal_1kHz_15kHz,11)

f, plt_arr = plt.subplots(2, sharex=True)
f.suptitle("Median Filter")
plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz, color = "red")
plt_arr[0].set_title("Input Signal", color = "red")
plt_arr[1].plot(median_filter_output, color = "green")
plt_arr[1].set_title("Output Signal", color = "green")