from math import sin
from numpy import arange
from pylab import plot,xlabel,ylabel,show,semilogx

g=10#m/s^2
drag_coef=0.1#s^-1

def f(v,t):
    return g - drag_coef*v

a = 0.0
b = 100.0
N = 1000
h = (b-a)/N

tpoints = arange(a,b,h)
xpoints = []
x = 200 #m/s

for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6


plot(tpoints,xpoints)
xlabel("t")
ylabel("v(t)")
show()
