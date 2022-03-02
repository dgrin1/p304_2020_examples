from math import sin,pi
from numpy import array,arange,sqrt,sin,cos,power,abs
import matplotlib.pyplot as plt
from scipy import integrate,constants

g=constants.g
l=0.1
om0=sqrt(g/l)
f=om0/(2.e0*pi)
T=1./f
print(T)

def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta)
    return array([ftheta,fomega],float)

a = 0.0
b = T*20
N = 100000
h = (b-a)/N

tpoints = arange(a,b,h)
thetapoints = []
omegapoints = []

r = array([3.0,0.0],float)
plt.figure(1)
for t in tpoints:
    thetapoints.append(r[0])
    omegapoints.append(r[1])
    k1 = h*f(r,t)
    k2 = h*f(r+0.5*k1,t+0.5*h)
    k3 = h*f(r+0.5*k2,t+0.5*h)
    k4 = h*f(r+k3,t+h)
    r += (k1+2*k2+2*k3+k4)/6
plt.plot(tpoints,thetapoints)
r_scipy=integrate.odeint(f,[3.0,0.0],tpoints)#
#plt.plot(tpoints,omegapoints)
plt.plot(tpoints,r_scipy[:,0],'r--')

plt.figure(2)
energy=(0.5e0)*power(omegapoints,2)*l*l+g*l*(1.-cos(thetapoints))
energy_scipy=(0.5e0)*power(r_scipy[:,1],2)*l*l+g*l*(1.-cos(r_scipy[:,0]))
etot=g*l*(1.-cos(thetapoints[0]))

plt.plot(tpoints,abs(energy-etot),'g--')
plt.figure(3)
plt.xlabel("t")
plt.xlim([0,20*T])
#plt.yscale('log')
plt.plot(tpoints,abs(energy_scipy-etot)/etot,'m')

plt.ion()
plt.show()
