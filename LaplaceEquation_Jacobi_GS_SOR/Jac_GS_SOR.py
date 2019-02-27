import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import timeit
from numba import jit

def grid(N):
    x, y = np.mgrid[0.:1.:complex(0,N),0.:1.:complex(0,N)]
    phi = x*x - y*y
    phi[1:-1,1:-1] = 0.0
    return  x, y, phi 

def epsilon():
    h = 1
    epsil1 = 1
    while(1+epsil1>1):
        h = 0.5*h
        epsil1 = h
    return epsil1

#Jacobi function
@jit
def Jacobi():
    N = input("What is the grid size? ")
    x, y, phi = grid(N)
    epsil = epsilon()
    phi1=np.array([])
    phi1  = phi.copy()
    phi1
    Err1 = 1
    Err2 = [1.0]
    i = 0
    start_time = timeit.default_timer()
    while(Err1>2*epsil):
        phi1[1:-1,1:-1] = 0.25*(phi[0:-2,1:-1]+phi[2:,1:-1]+phi[1:-1,0:-2]+phi[1:-1,2:])   
        err = phi1 - phi
        #print(phi1) 
        phi
        err = err*err
        #print np.sqrt(err.sum())
        Err1 = (np.sqrt(err.sum()))/N
        Err2.append(Err1)
        phi = phi1.copy()
        i = i+1
    elapsed = timeit.default_timer() - start_time
    print i
    print elapsed
    print phi
    plt.semilogy(Err2)
    plt.xlabel('Iterations')
    plt.ylabel('Error')
    plt.title('Jacobi, N=101 ')
    plt.show()


#Gauss-Seidel function
@jit
def Gauss():
    N = input("What is the grid size? ")
    x, y, phi = grid(N)
    epsil = epsilon()
    phi1=np.array([])
    phi1  = phi.copy()
    phi1
    Err1 = 1
    Err2 = [1.0]
    i = 0
    start_time = timeit.default_timer()
    while(Err1>2*epsil):
        for j in range(1,N-1):
            for k in range(1,N-1):
                phi1[j,k] = 0.25*(phi[j-1,k]+phi[j+1,k]+phi[j,k+1]+phi[j,k-1])   
        err = phi1 - phi
        #print(phi1) 
        phi
        err = err*err
        #print np.sqrt(err.sum())
        Err1 = (np.sqrt(err.sum()))/N
        Err2.append(Err1)
        phi = phi1.copy()
        i = i+1
    elapsed = timeit.default_timer() - start_time
    print i
    print elapsed
    plt.semilogy(Err2)
    plt.xlabel('Iterations')
    plt.ylabel('Error')
    plt.title('Gauss-Seidel, N=101 ')
    plt.show()

#SOR function for fixed number of iterations
@jit
def SOR(N,iterations,w):
    x,y,phi = grid(N)
    phi1=phi.copy()
    phiGS=phi.copy()
    error=[1.0]
    it=0
    
    for it in range(iterations):
        for i in range(1,N-1):
            for j in range(1,N-1):
                phiGS[i,j]=0.25*(phi[i-1,j]+phi[i+1,j]+phi[i,j-1]+phi[i,j+1])
                phi[i,j]=(1-w)*phi1[i,j]+w*phiGS[i,j]
        error.append(np.sqrt(((phi-phi1)**2).sum())/N)
        phi1=phi.copy()
    return phi,error[1:]

def callSOR(N,iterations,w):
    err=[]
    N=N   
    for wi in w:
        phi,error=SOR(N,iterations,wi)
        err.append(min(error))      
    return err,w
  
'''                                                                                    
err,w=callSOR(101,100,np.arange(1,2.1,0.1))
plt.plot(w,err)
plt.xlabel('w')
plt.ylabel('Err')
plt.title('N = 101 & Iterations = 100')
plt.show()
'''

@jit
def SOR2(N,w):
    x,y,phi = grid(N)
    phi1=phi.copy()
    phiGS=phi.copy()
    error=[1.0]
    epsil = 1.11022302463e-16
    iteration = 0
    Err = 1
    while(Err>epsil):
        for i in range(1,N-1):
            for j in range(1,N-1):
                phiGS[i,j]=0.25*(phi[i-1,j]+phi[i+1,j]+phi[i,j-1]+phi[i,j+1])
                phi[i,j]=(1-w)*phi1[i,j]+w*phiGS[i,j]
        Err = (np.sqrt(((phi-phi1)**2).sum()))/N
        error.append(Err)
        phi1=phi.copy()
        iteration= iteration + 1
    return phi,iteration, Err
   
   

def w_opt(N,w):
    #err=[]
    N=N
    iterationsl=[1.0]
    for wi in w:
        phi,iteration, Err =SOR2(N,wi)
        iterationsl.append(iteration)
    return iterationsl[1:],w


iter,w=w_opt(5,np.arange(1,2.1,0.1))
print w
print iter 


'''
plt.semilogy(iter,w)
plt.xlabel('w')
plt.ylabel('Iterations')
plt.title('N = 41')
plt.show()
'''

#Jacobi()
#Gauss()
