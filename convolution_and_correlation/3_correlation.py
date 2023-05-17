# -*- coding: utf-8 -*-
"""
Created on Wed May  3 16:50:46 2023

@author: yesed
"""
from matplotlib import pyplot as plt
from scipy import signal
import numpy as np
import mysignals as sigs


corr_output_signal = signal.correlate(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response, mode = "same")
conv_output_signal = signal.convolve(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response, mode = "same")

f, plt_arr = plt.subplots(3, sharex=True)
f.suptitle("Correlation")
plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz, color = "grey")
plt_arr[0].set_title("Input Signal")
plt_arr[1].plot(sigs.Impulse_response, color = "blue")
plt_arr[1].set_title("Impulse Response")
plt_arr[2].plot(corr_output_signal, color = "red")
plt_arr[2].set_title("Output Signal")
# plt.plot(corr_output_signal)
plt.show()

