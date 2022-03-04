from math import sin
from numpy import arange, array, pi
import matplotlib.pyplot as plt

def f(r,t):
    g = 9.8
    l = 1
    x = r[0]
    v = r[1]
    fx = v
    fv = -g/l * sin(x)
    return array([fx,fv],float)
a = 0.0
b = 10.0
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
vpoints = []
x = 0.0


r = [0,6.25]
for t in tpoints:
    xpoints.append(r[0])#% (2 * pi))
    vpoints.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

plt.plot(tpoints,xpoints, label = 'theta')
plt.plot(tpoints, vpoints, label = 'velocity')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.legend()
plt.show()
