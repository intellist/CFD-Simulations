import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
from math import *
x= np.linspace(-4*10**-8,4*10**-8,100)
y=(0.5*(np.sin(x))**2)/x**2
plt.plot(x,y)
plt.show()
