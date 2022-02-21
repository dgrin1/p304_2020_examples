# simpson's rule for x**4 - 2x + 1
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

N=1000
a=0
b=2

def f(x):
    f=np.power(x,4.e0)-2.*x+1.
    return(f)

def simpson(a,b,f,N):
    h = (b-a)/N
    sum1 = 0
    sum2 = 0
    for k in range(1,int(N/2)):
        sum1 += f(a + h*(2*k-1))
    for k in range(1,int(N/2-1)):
        sum2 += f(a + 2*k*h)
    I = h/3 *(f(a) + f(b) + 4*sum1 + 2*sum2)
    return(I)

print("Simpson approx:",simpson(a,b,f,N))

# ------------------------------------------------------------------------------
# Romberg integration (from scipy)

function = lambda x: np.power(x,4.e0)-2.*x+1.

romberg = integrate.romberg(function, a, b)

print("Scipy integration:",romberg)

# ------------------------------------------------------------------------------
# plot (numerical-exact)/exact as function of N on log plot

i = 0
exact = 4.4
Nvals = np.arange(10,1000)
numerical = np.zeros(len(Nvals))

for N in range(10,1000):
    newterm = simpson(a,b,f,N)
    numerical[i] = newterm
    i += 1

errorvals = abs((numerical-exact)/exact)

plt.ion()
plt.plot(Nvals,errorvals,label='Error from exact value')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("N (log scale)")
plt.ylabel("Fractional error (log scale)")

# ------------------------------------------------------------------------------
# plot (numerical(2N)-numerical(N))/numerical(N) as function of N on log plot

i = 0
Nvals = np.arange(10,1000)

errorvals2 = np.zeros(len(Nvals))

for N in range(10,1000):
    newterm_N = simpson(a,b,f,N)
    newterm_2N = simpson(a,b,f,2*N)
    errorvals2[i] = abs((newterm_2N - newterm_N)/newterm_N)
    i += 1

plt.ion()
plt.plot(Nvals,errorvals2,label='Difference between N and 2N values')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("N (log scale)")
plt.ylabel("Fractional difference (log scale)")
plt.legend()
