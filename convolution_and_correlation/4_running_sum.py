# -*- coding: utf-8 -*-
"""
Created on Wed May  3 17:10:04 2023

@author: yesed
"""

from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import mysignals as sigs

# If I find the peak values of the signal, this code is succesfull

output_signal = np.cumsum(sigs.InputSignal_1kHz_15kHz)
style.use("classic")
f,plt_arr = plt.subplots(2, sharex = True)
f.suptitle("Cummulative Summation")
plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz, color = "green")
plt_arr[0].set_title("Intput Signal")
plt_arr[1].plot(output_signal, color = "red")
plt_arr[1].set_title("Output signal")
