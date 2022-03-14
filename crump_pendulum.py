from math import sin
from numpy import array,arange
#from pylab import plot,xlabel,show
import matplotlib.pyplot as plt

def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta)
    return array([ftheta,fomega],float)

def f2(s,t):
    theta = s[0]
    omega = s[1]
    ftheta = omega
    fomega = -(g/l)*theta
    return array([ftheta,fomega],float)

a = 0.0
b = 50.0
N = 1000
h = (b-a)/N

g=1.428 #m/s^2 (Ganymede)
l=1

tpoints = arange(a,b,h)
thetapoints = []
omegapoints = []

r = array([3,0],float)
for t in tpoints:
    thetapoints.append(r[0])
    omegapoints.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6

thetapointssmall = []
omegapointssmall = []
s = array([3,0],float)
for t in tpoints:
    thetapointssmall.append(s[0])
    omegapointssmall.append(s[1])
    k1 = h*f2(s,t)
    k2 = h*f2(s+0.5*k1,t+0.5*h)
    k3 = h*f2(s+0.5*k2,t+0.5*h)
    k4 = h*f2(s+k3,t+h)
    s += (k1+2*k2+2*k3+k4)/6


plt.ion()
plt.figure(1)
plt.plot(tpoints,thetapoints, label="Angle")
plt.plot(tpoints,omegapoints, label="Angular Velocity")
plt.legend(loc="upper right")
plt.title("No Small Angle Approximation")
plt.xlabel("Time")


plt.figure(2)
plt.plot(thetapoints,omegapoints)
plt.title("No Small Angle Approximation")
plt.xlabel("Angle")
plt.ylabel("Angular Velocity")


plt.figure(3)
plt.plot(tpoints,thetapointssmall, label="Angle")
plt.plot(tpoints,omegapointssmall, label="Angular Velocity")
plt.legend(loc="upper right")
plt.title("Small Angle Approximation")
plt.xlabel("Time")


plt.figure(4)
plt.plot(thetapointssmall,omegapointssmall)
plt.title("Small Angle Approximation")
plt.xlabel("Angle")
plt.ylabel("Angular Velocity")
plt.show()
