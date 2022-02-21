import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def f(x):
    return x**4 - 2*x + 1

def simp(f,a,b,N):
    h = abs(a-b)/(2*N)
    sum1 = 0
    sum2 = 0
    for k in range(int(N)+1) :
        sum1 += f(a+(2*k-1)*h)
    for k in range(int(N)) :
        sum2 += f(a+2*k*h)
    return (1/3)*h*(f(a) + f(b) + 4*sum1 + 2*sum2)

N = 100000
a = 0
b = 2

print("For N =",N,": I(a,b) =",simp(f,a,b,N))

# Trapezoid:
# Reimann:

print("Romberg:",integrate.romberg(f,a,b))
print("Quadrature:",integrate.fixed_quad(f,a,b))

Nrange = np.arange(10,1000)
intigle_array = np.zeros(len(Nrange))
for index, n in enumerate(Nrange) :
    intigle_array[index] = simp(f,a,b,n)
#
fig1, ax1 = plt.subplots()
# fig2, ax2 = plt.subplots()
ax1.loglog(Nrange,abs(intigle_array-4.4)/4.4)
plt.show()
