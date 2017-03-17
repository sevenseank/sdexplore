import matplotlib.pyplot as plt
import numpy as np
import sdeint

A = np.array([[-0.5, -2.0],
              [ 2.0, -1.0]])

B = np.diag([0.5, 0.5]) # diagonal, so independent driving Wiener processes

tspan = np.linspace(0.0, 10.0, 10001)
x0 = np.array([3.0, 3.0])

def f(x, t):
    return A.dot(x)

def G(x, t):
    return B

result = sdeint.itoint(f, G, x0, tspan)

x = result[:,0]
y = result[:,1]

plt.plot(tspan, x)
plt.plot(tspan, y)
plt.figure()
plt.plot(x,y)
plt.show()
