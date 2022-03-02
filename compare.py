from math import sin
from numpy import arange
from pylab import plot,xlabel,ylabel,show,close,yscale,legend
import numpy as np

#insert function here
def f(x,t):
    return -x**3 + sin(t)
#boundaries and step size
#make ilsts
a = 0.0           # Start of the interval
b = 10.0          # End of the interval
N = 1000          # Number of steps
h = (b-a)/N       # Size of a single step
x = 0.0           # Initial condition

tpoints = arange(a,b,h)
xpoints = []
#Euler's method
for t in tpoints:
    xpoints.append(x)
    x += h*f(x,t)

plot(tpoints,xpoints,'k')
xlabel("t")
ylabel("x(t)")


a = 0.0
b = 10.0
h = (b-a)/N
#boundaries and step size
#make ilsts

tpoints = arange(a,b,h)
x2points = []

x = 0.0
#standard #RK4 with 2 steps

for t in tpoints:
    x2points.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    x += k2

plot(tpoints,x2points,'r--')




#boundaries and step size
a = 0.0
b = 10.0
h = (b-a)/N
#make ilsts
tpoints = arange(a,b,h)
x4points = []
x = 0.0

#standard #RK4 with 4 steps
for t in tpoints:
    x4points.append(x)
    k1 = h*f(x,t)
    k2 = h*f(x+0.5*k1,t+0.5*h)
    k3 = h*f(x+0.5*k2,t+0.5*h)
    k4 = h*f(x+k3,t+h)
    x += (k1+2*k2+2*k3+k4)/6

plot(tpoints,x4points,'m')


# 
# a = 0.0
# b = 10.0
# h = (b-a)/N
# 
# tpoints = arange(a,b,h)
# x4points = []
# x = 0.0
# 
# for t in tpoints:
#     x4points.append(x)
#     k1 = h*f(x,t)
#     k2 = h*f(x+0.5*k1,t+0.5*h)
#     k3 = h*f(x+0.5*k2,t+0.5*h)
#     k4 = h*f(x+k3,t+h)
#     x += (k1+2*k2+2*k3+k4)/6
# 
# plot(tpoints,x4points,'m')
# 


show()
close()

#residual plots
plot(tpoints,np.abs((np.array(xpoints)-np.array(x4points))/np.array(x4points)),label='Euler Residual')
plot(tpoints,np.abs((np.array(x2points)-np.array(x4points))/np.array(x4points)),label='rk2 residual')
yscale('log')
legend()
show()
