import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def f1(x):
    return(x**4 - 2*x +1)

def f2(x):
    return(np.sin(x))

def riemann(N, a, b, f):
    h = (b-a)/N
    s = 0
    for k in range(1, N):
        s += f(a + k*h)
    I = h*s
    return(I)

def trapezoidal(N, a, b, f):
    h = (b-a)/N
    s = 0
    for k in range(1, N):
        s += f(a + k*h)
    I = h*((f(a)+f(b))/2 + s)
    return(I)

def simpson(N, a, b, f):
    h = (b-a)/N
    s1 = 0
    s2 = 0
    for k in range(1, N, 2):
        s1 += f(a + k*h)
    for k in range(2, N, 2):
        s2 += f(a + k*h)
    I = (h/3) * (f(a) + f(b) + 4*s1 + 2*s2)
    return(I)

#polynomial
a = 0
b = 2
N = 10

s = simpson(N, a, b, f1)
t = trapezoidal(N, a, b, f1)
r = riemann(N, a, b, f1)

romberg = integrate.romberg(f1, a, b)
print("Riemann:", r)
print("Trapezoid:", t)
print("Simpson:", s)
print("Romberg:", romberg)

#sine
a = 0
b = np.pi
N = 10

s = simpson(N, a, b, f2)
t = trapezoidal(N, a, b, f2)
r = riemann(N, a, b, f2)
romberg = integrate.romberg(f2, a, b)

print("Riemann:", r)
print("Trapezoid:", t)
print("Simpson:", s)
print("Romberg:", romberg)

#error in simpson
N = np.arange(10, 1001)
a = 0
b = 2

num = []
for n in N:
    num.append(simpson(n, a, b, f1))
ex =  22/5

error = []
for i in range(len(num)):
    error.append(abs(num[i]-ex)/ex)


plt.plot(N, error)
plt.show()
