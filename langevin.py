import numpy as np
import matplotlib.pyplot as plt
import sdeint

a = 1.0
b = 1.0
phi = 0.0
# can work
#f = 0.01; A = 0.3; sigma = 1.1; fs = 10.0; N = 40000
#f = 0.01; A = 0.3; sigma = 2.1; fs = 10.0; N = 40000
#f = 0.01; A = 0.3; sigma = 3.1; fs = 100.0; N = 4000*100
#f = 0.0625; A = 0.247; sigma = 2.1; fs = 10.0; N = 40000

f = 0.01; A = 0.20; sigma = 1.1; fs = 30.0; N = 40000*3


#f = 0.0625; A = 0.247; sigma = 2.47; fs = 10.0; N = 40000

#f = 0.0625; A = 0.247; sigma = 2.47
#f = 0.0625; A = 0.247; sigma = 1.1
#f = 0.0625; A = 0.247; sigma = 0.781
#f = 0.1; A = 0.5; sigma = 5.0

omega = 2*np.pi*f

tspan = N/fs
#t = np.linspace(0.0, 200.0, 10001)
t = np.linspace(0.0, tspan, N+1)
x0 = 0.1

def f_regular(x, t):
    return a*x - b*x**3 + A*np.cos(omega*t+phi)
    #return A*np.cos(omega*t+phi)

def f_noise(x, t):
    return sigma

result = sdeint.itoint(f_regular, f_noise, x0, t)

x = result[:,0]

spectrum = np.abs(np.fft.fft(x))**2
#spectrum = np.log(spectrum)
time_step = t[1]-t[0]
freqs = np.fft.fftfreq(x.size, time_step)
#idx = np.argsort(freqs)
idx = np.arange(N/2)

plt.subplot(3,1,1)
plt.plot(t, x)
plt.subplot(3,1,2)
plt.plot(freqs[idx], spectrum[idx])
plt.subplot(3,1,3)
plt.plot(freqs[idx], np.log(spectrum[idx]))
plt.show()
