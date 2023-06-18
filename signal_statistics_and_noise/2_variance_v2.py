# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 04:00:07 2023

@author: yesed
"""

import mysignals as sig

_mean = 0.0
_variance = 0.0

def calc_variance(sig_src_arr):
    global _mean
    global _variance
    
    for x in range(len(sig_src_arr)):
        _mean += sig_src_arr[x]
    _mean = _mean/len(sig_src_arr)
    
    
    for x in range(len(sig_src_arr)):
        _variance = _variance + (sig_src_arr[x]-_mean)**2
    _variance = _variance/len(sig_src_arr)
    return _variance
        
