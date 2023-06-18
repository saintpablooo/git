# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 16:56:06 2023

@author: yesed
"""

import mysignals as sigs
from matplotlib import pyplot as plt
from scipy.fftpack import fft,ifft 
import numpy as np

freq_domain_signal = fft(sigs.ecg_signal)
time_domain_signal = ifft(freq_domain_signal)
magnitude = np.abs(freq_domain_signal)

f, plt_arr = plt.subplots(4, sharex=True)

f.suptitle("Fast Fourier Transform (FFT)")

plt_arr[0].plot(sigs.ecg_signal, color="red")
plt_arr[0].set_title("Time Domain (Input Signal)", color = "red")
plt_arr[1].plot(freq_domain_signal,color = "blue")
plt_arr[1].set_title("Frequency Domain (FFT)", color = "blue")
plt_arr[2].plot(time_domain_signal, color= "green")
plt_arr[2].set_title("Time Domain (IFFT)", color = "green")
plt_arr[3].plot(magnitude, color= "cyan")
plt_arr[3].set_title("Magnitude", color = "cyan")

plt.show()