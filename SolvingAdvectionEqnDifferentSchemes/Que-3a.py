import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
fig, ax = plt.subplots()

x = np.arange(-1, 1,0.05)

b=np.zeros((100,40))
#boundary and initial conditions 
#for i in range(100):
#    b[i,0]=0
for i in  range(1,40):
    b[0,i]=-1.0*(np.sin(pi*x[i]))
#print(x[1],b[1])


#FTBS
for t in range(99):
    for j in range(1,39):
        b[t+1,j]=b[t,j]-0.8*(b[t,j]-b[t,j-1])
        
    b[t+1,39]=b[t+1,38]
    b[t+1,0]=b[t+1,38] 

#FTCS2
'''for t in range(99):
    for j in range(1,39):
        b[t+1,j]=b[t,j]-0.5*0.8*(b[t,j+1]-b[t,j-1]) + ((0.8**2)*0.5)*(b[t,j+1]+b[t,j-1]-2*b[t,j])
    b[t+1,39] = b[t+1,38]
    b[t+1,0]=b[t+1,38]
'''



line, = ax.plot(x,b[1])
ax.axis([-1.0,1.0,-2,2])

def animate(i):
    time.sleep(0.1)
    line.set_ydata(b[i])  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x[1], mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 45), init_func=init,
                              interval=25, blit=True)
plt.show()
