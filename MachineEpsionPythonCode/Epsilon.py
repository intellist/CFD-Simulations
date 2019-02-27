epsilon= float(1.0)
e= float(2.0)
while(e>1):
    epsilon = 0.5*epsilon
    e = 1+epsilon
    print(epsilon)
print"Machine epsilon is:",epsilon

#5.55111512313e-17
