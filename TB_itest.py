from __future__ import print_function,division
import numpy as np
import matplotlib.pyplot as plt

N=100
a=0
b=2

s=0

def f(x):
	f=np.power((x-1),5.e0)-5.*x*(np.sin(5*x))
	return f

def intf(x):
	intf = 1/6*(-1+x)**6 + x * np.cos(5*x)-1/5*np.sin(5*x)
	return intf

def reiman(a,b,f,N):
	x=0
	s=0
	h=float(b-a)/float(N)
	for i in range(0,N+1):
		s+=f(x)*h
		x=a+i*h
	return s

reiman(a,b,f,N)

def trape(a,b,f,N):
	h=(b-a)/N
	s=(f(a)+f(b))*h
	for i in range(1,N):
		s+=2.*f(a+i*h)*h
	s/=2.0
	return s

trape(a,b,f,N)

print(reiman(a,b,f,N),trape(a,b,f,N))

dif = [0]
N_steps = 100

for N_var in range(10,1000,10):
	numer = trape(a,b,f,N_var)
	exact = intf(b) - intf(a)
	val = abs((numer - exact)/exact)
	dif.append(val)

dif.remove(0)
y = dif
x = range(10,1000,10)

plt.figure(1)
plt.plot(x,y)
plt.title("Plot of the numberical difference")

plt.figure(2)
plt.loglog(x,y)
plt.title("Loglog plot of the numberical difference")

dif2 = [0]

for N_var2 in range(10,1000,10):
	numer = trape(a,b,f,N_var2)
	numer2 = trape(a,b,f,2*N_var2)
	val = (numer2 - numer)/(numer)
	dif2.append(val)

dif2.remove(0)
y2 = dif2
x2 = x

plt.figure(3)
plt.loglog(x2,y2)
plt.title("Loglog plot of the numberical difference")

plt.show()
