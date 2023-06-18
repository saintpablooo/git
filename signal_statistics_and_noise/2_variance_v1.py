# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 03:57:26 2023

@author: yesed
"""

import numpy as np
import mysignals as sigs

variance = np.var(sigs.InputSignal_1kHz_15kHz)
print(variance)