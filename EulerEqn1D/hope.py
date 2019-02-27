import numpy as np
import matplotlib.pyplot as plt

n = int(raw_input("Enter the number of grid points:"))
P_o = int(raw_input("Enter the total chamber pressure:"))
T_o = int(raw_input("Enter the total temperature:"))
P_a = int(raw_input("Enter the pressure at the exit:"))
T_a = int(raw_input("Enter the exit temperature:"))
cfl = float(raw_input("Enter the (dt by dx) for computing:"))
u1 = float(raw_input("Enter the artificial dissipation coefficient of second derivative:"))
u2 = float(raw_input("Enter the artificial dissipation coefficient of fourth derivative:"))


x = np.mgrid[0.:1.:n*1j];
g = 1.4


####### SET UP THE INITIAL AND BOUNDARY CONDITIONS  #########
u = [0] * n

rho = [0.97526] * n
rho[0] = 1.1764

p = [P_a] * n
p[0] = P_o

#print p,rho,u


####### Dummy variables ###########
q1 = [] 
q2 = []
q3 = []
q2cap = []
q3cap = []
q22cap = []
q33cap = []
c = []

######## Actual variables ###########
q11 = []
q22 = []
q33 = []
q11[:] = rho[:]
e1 = []
e2 = []
e3 = []

for i in range(n):
    q22.append(rho[i]*u[i])
    e1.append(rho[i]*u[i])
    e2.append(rho[i]*u[i]*u[i] + p[i])
    q33.append(p[i]/(g-1) + rho[i]*u[i]*u[i]*0.5)
    e3.append((q33[i]+p[i])*u[i])
    c.append(np.sqrt(1.4*p[i])/(rho[i]))
    #print c[i]
    q22cap.append(u[i]+ (2*c[i]/(g-1)))
    q33cap.append(u[i]- (2*c[i]/(g-1)))

######### PLOTTING COMMANDS ################3
plt.ion()
plt.figure(1)
plt.subplot(311)
plt.axis([0,1,0.8,1.3])
plt.ylabel('Density')
graph = plt.plot(x,rho)[0]
plt.subplot(312)
plt.axis([0,1,-50,200])
plt.ylabel('Velocity')
graph1 = plt.plot(x,u)[0]
plt.subplot(313)
plt.axis([0,1,75000,102000])
plt.ylabel('Pressure')
graph2 = plt.plot(x,p)[0]

for k in range(100000):
    q1[:] = q11[:]
    q2[:] = q22[:]
    q3[:] = q33[:]
    q2cap[:] = q22cap[:]
    q3cap[:] = q33cap[:]
    #print q2,e2
    for i in range (1,n-1):
        if(i==1):
            q11[i] = q1[i] - cfl * 0.5 * (e1[i+1] - e1[i-1]) + u1*(q1[i+1] - 2*q1[i] + q1[i-1]) - u2*(-4*q1[i+3] + q1[i] - 4*q1[i+1] +q1[i+4] + 6*q1[i+2])
            q22[i] = q2[i] - cfl * 0.5 * (e2[i+1] - e2[i-1]) + u1*(q2[i+1] - 2*q2[i] + q2[i-1]) - u2*(-4*q2[i+3] + q2[i] - 4*q2[i+1] +q2[i+4] + 6*q2[i+2])
            q33[i] = q3[i] - cfl * 0.5 * (e3[i+1] - e3[i-1]) + u1*(q3[i+1] - 2*q3[i] + q3[i-1]) - u2*(-4*q3[i+3] + q3[i] - 4*q3[i+1] +q3[i+4] + 6*q3[i+2])
        if(i==(n-2)):
            q11[i] = q1[i] - cfl * 0.5 * (e1[i+1] - e1[i-1]) + u1*(q1[i+1] - 2*q1[i] + q1[i-1]) - u2*(-4*q1[i-3] + q1[i] - 4*q1[i-1] +q1[i-4] + 6*q1[i-2])
            q22[i] = q2[i] - cfl * 0.5 * (e2[i+1] - e2[i-1]) + u1*(q2[i+1] - 2*q2[i] + q2[i-1]) - u2*(-4*q2[i-3] + q2[i] - 4*q2[i-1] +q2[i-4] + 6*q2[i-2])
            q33[i] = q3[i] - cfl * 0.5 * (e3[i+1] - e3[i-1]) + u1*(q3[i+1] - 2*q3[i] + q3[i-1]) - u2*(-4*q3[i-3] + q3[i] - 4*q3[i-1] +q3[i-4] + 6*q3[i-2])      
        else:
            q11[i] = q1[i] - cfl * 0.5 * (e1[i+1] - e1[i-1]) + u1*(q1[i+1] - 2*q1[i] + q1[i-1]) - u2*(-4*q1[i-1] + 6*q1[i] - 4*q1[i+1] +q1[i-2] + q1[i+2])
            q22[i] = q2[i] - cfl * 0.5 * (e2[i+1] - e2[i-1]) + u1*(q2[i+1] - 2*q2[i] + q2[i-1]) - u2*(-4*q2[i-1] + 6*q2[i] - 4*q2[i+1] +q2[i-2] + q2[i+2])
            q33[i] = q3[i] - cfl * 0.5 * (e3[i+1] - e3[i-1]) + u1*(q3[i+1] - 2*q3[i] + q3[i-1]) - u2*(-4*q3[i-1] + 6*q3[i] - 4*q3[i+1] +q3[i-2] + q3[i+2])
        #print q11[i], q22[i], q33[i]
    #print q11,q22
    ######### UPDATING NEW VARIABLES ###############
    for i in range (1,n-1):
		rho[i] = q11[i]
		u[i] = q22[i]/q11[i]
		p[i] = q33[i]*(g-1) - 0.5*(g-1)*rho[i]*u[i]*u[i]
		e1[i] = q22[i]
		e2[i] = rho[i]*u[i]*u[i] + p[i]
		e3[i] = (q33[i]+p[i])*u[i]  
    #print q11


    for i in range(0,n):
		q22cap[i] = u[i]+ (2*c[i]/(g-1))
		q33cap[i] = u[i]- (2*c[i]/(g-1))
		c[i] = np.sqrt(1.4*p[i]/rho[i])
		#print u
    #print q33
    print p
######### INLET ###########     
	#print p[0],rho[0]
    #c = np.sqrt(1.4*p[0]/rho[0])
    #print c
    #print q3[0],u[0],q3[1],q2[0],q2[1]
    u[0] = u[1]
    a = u[0]
    #print q33cap[0],q22cap[0],c[0]
    #q33cap[0] = q3cap[0] - (a-c[0])*cfl*(q3cap[1] - q3cap[0])
    #q22cap[0] = q2cap[0] - (a+c[0])*cfl*(q2cap[1] - q2cap[0])
    #print q33cap[0],q22cap[0]
    #u[0] = (q33cap[0] + q22cap[0]) * 0.5
    #print u[0]
    t = T_o - ((u[0]**2)/(2010))
    #print t
    p[0] = P_o*((t/T_o)**(3.5))
    rho[0] = p[0]/(287.1*t)
    q11[0] = rho[0]
    q22[0] = rho[0]*u[0]
    q33[0] = p[0]/(g-1) + rho[0]*u[0]*u[0]*0.5
    e1[0] = q22[0]
    e2[0] = rho[0]*u[0]*u[0] + p[0]
    e3[0] = (q33[0]+p[0])*u[0]
######## EXIT CONDITION ##############
    #c = np.sqrt(g*p[n-1]/rho[n-1])
   	#q33[n-1] = q3[n-1] - (u[n-1]-c)*cfl*(q3[n-1] - q3[n-2])
    #q22cap[n-1] = q2cap[n-1] - (u[n-1]+c)*cfl*(q2[n-1] - q2[n-2])
    #u[n-1] = (q33[n-1] + q22[n-1]) * 0.5
    u[n-1] = u[n-2]
    a = u[n-1]
    #rho[n-1] = rho[n-2]
    #q33cap[n-1] = q3cap[n-1] - (a-c[n-1])*cfl*(q3cap[n-1] - q3cap[n-2])
    #q22cap[n-1] = q2cap[n-1] - (a+c[n-1])*cfl*(q2cap[n-1] - q2cap[n-2])
    #print q33[0]
    #u[n-1] = (q33cap[n-1] + q22cap[n-1]) * 0.5
    #print u[n-1]
    t = T_o - u[n-1]**2/(2010)
    #print t
    #p[n-1] = P_o*((t/T_o)**(3.5))
    p[n-1] = P_a
    rho[n-1] = p[n-1]/(287.1*t)
    q11[n-1] = rho[n-1]
    #print q11[n-1]
    q22[n-1] = rho[n-1]*u[n-1]
    q33[n-1] = p[n-1]/(g-1) + rho[n-1]*u[n-1]*u[n-1]*0.5
    e1[n-1] = q22[n-1]
    e2[n-1] = rho[n-1]*u[n-1]*u[n-1] + p[n-1]
    e3[n-1] = (q33[n-1]+p[n-1])*u[n-1] 
    #print u
    graph.set_ydata(rho)
    graph1.set_ydata(u)
    graph2.set_ydata(p)
    #plt.plot(x,rho)
    plt.draw()
    plt.pause(0.00001)

plt.pause(10)   

    
    
    
    
    
    
    
    
    
    
    
    

