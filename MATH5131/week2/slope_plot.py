import numpy as np
from matplotlib import pyplot as plt

def diff(t,y,params):
	r = params[0] - params[1]
	K = params[2]
	eps = params[3]
	dydt = -y * r / K * (y - K * (1 - eps / r))
	return dydt

t = np.linspace(-4,4,20)
y = np.linspace(-4,4,20)

params = [0.34, 0.12, 250, 0.9]

for j in t:
    for k in y:
        slope = diff(j, k, params)
        domain = np.linspace(j-0.05,j+0.05,2)
        def fun(t1,y1):
            z = slope*(domain-t1)+y1
            return z
        plt.plot(domain,fun(j,k),solid_capstyle='projecting',solid_joinstyle='bevel')
        
plt.rcParams["figure.figsize"] = (10,10)
plt.grid(True)
plt.show()
