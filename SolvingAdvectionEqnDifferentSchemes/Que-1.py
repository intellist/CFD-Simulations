import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


def Initialize(N):
    x = np.arange(0, 1,1/float(N))
    b=np.zeros((100,50))
    #1)boundary and initial conditions 
    for i in range(100):
        b[i,0]=1
    for i in  range(1,50):
        b[0,i]=0
    return(x,b)



def FTCS(N,CFL,b):
    b = Initialize(N)
    for t in range(99):
        for j in range(1,N-1):
            b[t+1,j]=b[t,j]-0.5*CFL*(b[t,j+1]-b[t,j-1])
        b[t,0]=1
        b[t+1,N-1]=b[t+1,N-2]
    return(b)


def FTBS(N,CFL,b):
    b = Initialize(N)
    for t in range(99):
        for j in range(1,N-1):
            b[t+1,j]=b[t,j]-1*(b[t,j]-b[t,j-1])
        b[t,0]=1
        b[t+1,N-2]=b[t+1,N-2]
    return(b)
    

def FTFS(N,CFL,b):
    b = Initialize(N)
    for t in range(99):
        for j in range(N-1):
            b[t+1,j]=b[t,j]-CFL*(b[t,j+1]-b[t,j])
        b[t,0]=1
        b[t+1,N-1]=b[t+1,N-2]
    return(b)


fig, ax = plt.subplots()
x,b = Initialize(50)
b1=FTCS(50,0.2,b)
#b2=FTBS(N,CFL,b)
#b3=FTCS(N,CFL,b)
line, = ax.plot(x,b1[1])
ax.axis([0,1.0,-2,2])

def animate(i):
    time.sleep(0.1)
    line.set_ydata(b1[i])  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 48), init_func=init,
                              interval=25, blit=True)
plt.show()

