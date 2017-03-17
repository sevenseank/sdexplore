#  encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint
import sdeint
import sys

a = 0.2
b = 0.2 
c = 5.7
#tspan = np.linspace(0.0, 600*np.pi, 50001)
tspan = np.linspace(0.0, 60*np.pi, 50001)
#tspan = np.linspace(0.0, 2*60*np.pi, 2*5001)

#X0 = np.array([1.0,0.,0.])
X0 = np.array([-2., -4.,1.])

def f(X, t):
    x,y,z = X
    dxdt = -y-z
    dydt = x+a*y
    dzdt = b+z*(x-c)
    #return np.zeros(2) 
    return np.array([dxdt, dydt, dzdt])*0.1

def g(X, t):
    #return np.diag([0., 0., 0.])
    #return np.diag([A, 0., 0.])
    return np.diag([0., 0, A])
    #return np.diag([A, A, A])

#A = float(input("A: "))
A = float(sys.argv[1])
result = sdeint.itoint(f, g, X0, tspan)
#result = odeint(f, X0, tspan)

x = result[:,0]
y = result[:,1]
z = result[:,2]

fig = plt.figure()
plt.subplot(122)
plt.plot(tspan, x)
#plt.plot(tspan, y)
#plt.plot(tspan, z)
#plt.plot(x,y)
#plt.plot(x,z)
#plt.plot(y,z)

plt.subplot(121)
ax = fig.add_subplot(121, projection='3d')
#ax = fig.gca(projection='3d')
ax.plot(x, y, z)

plt.show()
