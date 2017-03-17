import numpy as np
import matplotlib.pyplot as plt
import sdeint

a = 1.0
b = 0.8
tspan = np.linspace(0.0, 500.0, 3*5001)
x0 = 0.1

def f(x, t):
    #return -(a + x*b**2)*(1 - x**2)
    return 0.0

def g(x, t):
    #return b*(1 - x**2)
    return 1.0

count = 100
result = []
for i in range(count):
    if i % 5 == 0:
        print("{}/{}".format(i, count))
    x = sdeint.itoint(f, g, x0, tspan) [:,0]
    plt.plot(tspan, x) 
    result.append(x )
plt.show()
