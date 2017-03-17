#  encoding=utf-8
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
import sdeint

#a = 1.0
#b = 0.8 
tspan = np.linspace(0.0, 600*np.pi, 50001)
#tspan = np.linspace(0.0, 60*np.pi, 5001)
omega = 1.0
X0 = np.array([1.0,0.])

def f(X, t):
    x,v = X
    dxdt = v
    dvdt = -omega**2*x
    #return np.zeros(2) 
    return np.array([dxdt, dvdt]) 

def g(X, t):
    #return np.diag([0., A])
    return np.diag([A, A])

A = float(input("A: "))
result = sdeint.itoint(f, g, X0, tspan)
#result = odeint(f, X0, tspan)

x = result[:,0]
v = result[:,1]

plt.plot(tspan, x)
plt.plot(tspan, v)
plt.show()
