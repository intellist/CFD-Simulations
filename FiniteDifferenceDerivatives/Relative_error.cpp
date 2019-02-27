import matplotlib
    
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
    
import numpy as np

from math import *
    
x = np.pi*0.25

h = x

Err = []
Err2 = []
Err4 = []
DX = []
EX = []
FX = []
sx = np.sin(x)

cx = np.cos(x)
for i in range (60):       #first order approximation
    df = (np.sin(x+h) - sx)/h
    err = abs(df - cx)/cx
    Err.append(err)
    DX.append(h)
    h = 0.5*h

h = x    
for i in range (60):      #second order approximation
    df = (np.sin(x+h) - np.sin(x-h))/(2*h)
    err = abs(df - cx)/cx
    Err2.append(err)
    EX.append(h)
    h = 0.5*h   

h = x    
for i in range (60):      #fourth order approximation
    df = (np.sin(x-2*h) + 8*np.sin(x+h) - 8*np.sin(x-h) - np.sin(x+2*h))/(12*h)
    err = abs(df - cx)/cx
    Err4.append(err)
    FX.append(h)
    h = 0.5*h  
    
plt.loglog(DX, Err, 'r' )
plt.loglog(EX, Err2,'b')    
plt.loglog(FX, Err4,'g')
plt.ylabel('relative error(log scale)')
plt.xlabel('h(log scale)')
plt.show()