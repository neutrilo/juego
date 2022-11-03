# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 14:02:00 2022

@author: hokoox
"""

import matplotlib.pyplot as pdt
import numpy as np

tiempo = np.linspace(0,72,73)
velocidad = np.zeros(1,73)
for i in range(73):
            if i==1 or i ==62:
                a=10
            else:
                a=0
            velocidad[i+1]=velocidad[i]+a
