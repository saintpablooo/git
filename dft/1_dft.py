# -*- coding: utf-8 -*-
"""
Created on Mon May 15 14:26:57 2023

@author: yesed
"""

import mysignals as sigs
from matplotlib import pyplot as plt
from matplotlib import style
import math

def calc_dft(sig_src_arr):
    sig_dest_imx_arr = [None]*int(len(sig_src_arr)/2)
    sig_dest_rex_arr = [None]*int(len(sig_src_arr)/2)
    sig_dest_mag_arr = [None]*int(len(sig_src_arr)/2)
    for j in range(int(len(sig_src_arr)/2)):
        sig_dest_rex_arr[j] = 0
        sig_dest_imx_arr[j] = 0
    
    for k in range(int(len(sig_src_arr)/2)):
        for i in range(len(sig_src_arr)):
            sig_dest_rex_arr[k] = sig_dest_rex_arr[k] + sig_src_arr[i]*math.cos(2*math.pi*k*i/len(sig_src_arr))
            sig_dest_imx_arr[k] = sig_dest_imx_arr[k] - sig_src_arr[i]*math.sin(2*math.pi*k*i/len(sig_src_arr))
    
    for x in range(int(len(sig_src_arr)/2)):
        sig_dest_mag_arr[x] = math.sqrt(math.pow(sig_dest_rex_arr[x],2)+math.pow(sig_dest_imx_arr[x], 2))
        
        
    f,plt_arr = plt.subplots(4,sharex=True)
    f.suptitle("Discrete Fourier Transform")
    
    plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz, color = 'red')
    plt_arr[0].set_title("Input Signal",color='red')
    
    plt_arr[1].plot(sig_dest_rex_arr, color = 'green')
    plt_arr[1].set_title("Real Part",color='green')
    
    plt_arr[2].plot(sig_dest_imx_arr, color = 'blue')
    plt_arr[2].set_title("Imaginer Part",color='blue')
    
    plt_arr[3].plot(sig_dest_mag_arr, color = 'cyan')
    plt_arr[3].set_title("Magnitude Part",color='cyan')
    
    
calc_dft(sigs.InputSignal_1kHz_15kHz)