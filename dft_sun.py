from __future__ import print_function
from numpy import zeros,loadtxt
import numpy as np
import matplotlib.pyplot as plt
from cmath import exp,pi,polar

def dft(y):
    N = len(y)
    c = zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c
y = loadtxt("sunspots.txt",float)
c = dft(y[:,1])

nyears=float(int(len(y[:,1])/12.))
frequency=2.*pi*np.array(list(map(lambda y: y/nyears, range(len(y[:,1])/2))))
# c=c[range(len(y[:,1])/2)]
plt.ion()
r=np.power(c.real,2.e0)+np.power(c.imag,2.0e0)
plt.plot(np.array(range(len(c)))/nyears,r)
plt.xlabel('Frequency in Year^-1')
plt.xscale('log')
plt.yscale('log')
plt.show()
