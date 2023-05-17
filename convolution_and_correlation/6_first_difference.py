# -*- coding: utf-8 -*-
"""
Created on Wed May  3 17:44:36 2023

@author: yesed
"""
from matplotlib import pyplot as plt
import numpy as np
import mysignals as sigs

output_signal = np.diff(sigs.InputSignal_1kHz_15kHz)

f, plt_arr = plt.subplots(2, sharex = True)
f.suptitle("First Difference")

plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz,color='red')
plt_arr[0].set_title("Input Signal")

plt_arr[1].plot(output_signal,color ='magenta')
plt_arr[1].set_title("Output Signal")