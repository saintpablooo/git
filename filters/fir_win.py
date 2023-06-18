# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 02:48:40 2023

@author: yesed
"""

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# Sampling rate = 2000
t = np.linspace(0,1.0,2001)

sig_5hz = np.sin(2*np.pi*5*t)
sig_50hz = np.sin(2*np.pi*50*t)
sig_250hz = np.sin(2*np.pi*250*t)

sig_5_50_250hz = sig_5hz + sig_50hz + sig_250hz

# plt.plot(sig_5_50_250hz)

numtaps = 101
lpf_cutoff = 7
hpf_cutoff = 100
bpf_cutoff1 = 40
bpf_cutoff2 = 100

# Low-pass
lowpass_coef = signal.firwin(numtaps, lpf_cutoff, nyq = 1000)
lpf_output = np.convolve(sig_5_50_250hz, lowpass_coef, mode="same")
# plt.plot(lpf_output)

# High-pass
highpass_coef = signal.firwin(numtaps, hpf_cutoff, pass_zero = False, nyq = 1000)
hpf_output = np.convolve(sig_5_50_250hz, highpass_coef, mode="same")
# plt.plot(hpf_output)

# Band-pass
bandpass_coef = signal.firwin(numtaps, [bpf_cutoff1, bpf_cutoff2], pass_zero = False, nyq = 1000)
bpf_output = np.convolve(sig_5_50_250hz, bandpass_coef, mode="same")
plt.plot(bpf_output)
