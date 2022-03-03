import numpy as np
import matplotlib.pyplot as plt

l= 1
g=10
def f(x, t):
    theta = x[0]
    der_theta = x[1]
    dtheta = der_theta
    theta_second_der= -(g/l)*np.sin(theta)
    return np.array([dtheta, theta_second_der], float)


a = 0
b = 50.0
N = 100000
h = (b-a)/N

tpoints = np.arange(a,b,h)
xpoints = []
rk2xpoints=[]
vpoints = []
rk2vpoints=[]
theta = np.array([0, 5], float)
rk2= np.array([0, 5], float)
for t in tpoints:
    xpoints.append(theta[0])
    vpoints.append(theta[1])
    rk2xpoints.append(rk2[0])
    rk2vpoints.append(rk2[1])
    k1 = h*f(theta,t)
    k1rk2 = h*f(rk2,t)
    k2 = h*f(theta+0.5*k1,t+0.5*h)
    k2rk2 = h*f(rk2+0.5*k1,t+0.5*h)
    rk2 +=(k1rk2+2*k2rk2)/6
    k3 = h*f(theta+0.5*k2,t+0.5*h)
    k4 = h*f(theta+k3,t+h)
    theta += (k1+2*k2+2*k3+k4)/6


plt.plot(tpoints,xpoints, label = 'RK 4th Order')
plt.plot(tpoints,rk2xpoints, label = 'RK 2nd Order')
plt.xlabel("t")
plt.ylabel(r'$\theta(t)$')
plt.legend()
plt.show(block=True)

plt.plot(xpoints,vpoints, label = 'RK4')
plt.plot(rk2xpoints,rk2vpoints, label = 'RK2')
plt.xlabel(r'$ \theta(t)$')
plt.ylabel(r'$ \theta^{\prime}(t)$')
plt.legend()
plt.show(block=True)
