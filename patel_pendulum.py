from math import sin,pi
from numpy import array,arange, copy,abs,sqrt
import numpy as np
import matplotlib.pyplot as plt


g=9.81     # gravitational acceleration
l = 1      # length of the pendulum

def f(r,t):
    omega = - (g/l) * np.sin(r[0])
    ftheta = omega
    return np.array([ftheta, omega], float)

a = 0.0
b = 15.0
N = 100
h = (b-a)/N

tpoints = arange(a,b,h)
ftheta = []
omega = []

r = 1 # initial 

for t in tpoints:
    ftheta.append(r[0])
    omega.append(r[1])
    k1 = h*f(r,t) 
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6
plt.ion()
plt.figure(1)
plt.plot(tpoints,ftheta)
plt.plot(tpoints,omega)
plt.figure(2)

#plt.plot(ftheta,omega)

plt.xlabel("t")
plt.show()
