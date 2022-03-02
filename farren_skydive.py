from math import sin
from numpy import arange
from pylab import plot,xlabel,ylabel,show,semilogx
#fundamental constants
g=10#m/s^2
drag_coef=0.1#s^-1
#ODE
def f(v,t):
    return g - drag_coef*v

a = 0.0
b = 100.0
N = 100
h = (b-a)/N
#lists
tpoints = arange(a,b,h)
xpoints = []

#i condition
x = 0
#200 #m/s

#rk4
for t in tpoints:
    xpoints.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6

#plot
plot(tpoints,xpoints)
xlabel("t")
ylabel("v(t)")
show()
