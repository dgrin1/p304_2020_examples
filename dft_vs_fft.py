from numpy import zeros,loadtxt
from pylab import plot,xlim,show
from cmath import exp,pi
from numpy.fft import rfft
import timeit

#defs

def dft(y):
    N = len(y)
    c = zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c

y = loadtxt("pitch.txt",float)
c = dft(y)
d= rfft(y)
print('done with fft, starting dft')
#c=dft(y)
plot(abs(d))
xlim(0,500)
show()

