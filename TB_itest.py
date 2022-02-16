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

def reiman(a,b,f,N):
	x=0
	s=0
	ivec=range(0,N+1)
	h=float(b-a)/float(N)
	for i in ivec:
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
	numer = reiman(a,b,f,N_var)
	exact = trape(a,b,f,N_var)
	val = (numer - exact)/exact
	dif.append(val)

dif.remove(0)
y = dif
x = range(10,1000,10)

plt.figure(1)
plt.plot(x,y)

plt.figure(2)
plt.loglog(x,y)

plt.show()
