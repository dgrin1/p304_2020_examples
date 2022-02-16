from __future__ import print_function,division
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
N=1000
a=0
b=2

ivec=range(0,N+1)
s=0
x=0
h=float(b-a)/float(N)

def f(x):
	f=np.power(x,4.e0)-2.*x+1.
	return f


for i in ivec:
	s+=f(x)*h
	x=a+i*h

def trape(a,b,f,N):
	h=(b-a)/N
	s=(f(a)+f(b))*h
	for i in range(1,N):
		s+=2.*f(a+i*h)*h
	s/=2.0
	return s

def simp(a,b,f,N):
	h=(b-a)/N
	k=N/2
	sumodd=0
	sumeven=0
	for i in range(1,int(k)+1):
		sumodd+=f(a+(2*i-1)*h)
		sumeven+=f(a+2*i*h)
	I=(1/3)*h*((f(a)+f(b))+4*sumodd+2*sumeven)
	return I

#romb=integrate.romberg(f,a,b)

print(s,trape(a,b,f,N),simp(a,b,f,N),romb)

N=range(10,1000)

trap=[]

for n in N:
	t=trape(a,b,f,n)
	trap.append(t)

plt.plot(N,trap)

plt.show()
