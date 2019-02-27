import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
fig, ax = plt.subplots()

x = np.arange(0, 1,0.01)

b=np.zeros((100,100))
#boundary and initial conditions 
for i in range(100):
    b[i,0]=0
for i in  range(1,100):
    b[0,i]=np.sin(2*pi*x[i]) + np.sin(20*pi*x[i])
#print(x[1],b[1])
#FTCS
'''for t in range(49):
    for j in range(1,99):
        b[t+1,j]=b[t,j]-0.5*0.2*(b[t,j+1]-b[t,j-1])
        b[t,0]=0'''


#FTBS
for t in range(99):
    for j in range(1,99):
        b[t+1,j]=b[t,j]-1.0*(b[t,j]-b[t,j-1])
        b[t,0]=0
    b[t+1,99]=b[t+1,98]
    b[t+1,0]=b[t+1,98]


#FTFS
'''for t in range(99):
    for j in range(99):
        b[t+1,j]=b[t,j]-0.2*(b[t,j+1]-b[t,j])
        b[t,0]=0
    b[t+1,99]=b[t+1,98]
    b[t+1,0]=b[t+1,98]'''

    

line, = ax.plot(x,b[1])
ax.axis([0,1.0,-3,3])

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
