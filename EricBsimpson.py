from __future__ import print_function,division
import numpy as np
import matplotlib.pyplot as plt
#N=10
a=0
b=2

def f(x):
	f=np.power(x,4.e0)-2.*x+1.
	return f

def simpson(a,b,f,N):
	h=float(b-a)/float(N)
	sum = (f(a) + f(b))
	for i in range(1,round(N),2):
		sum += 4 * f(a + i * h)
	for i in range(2,round(N-1),2):
		sum += 2 * f(a + i * h)

	return sum * (1/3) * h

def rect(a,b,f,N):
	h=float(b-a)/float(N)
	ivec=range(0,round(N+1))
	s=0
	x=0
	for i in ivec:
		s+=f(x)*h
		x=a+i*h
	return s

solns = np.zeros(10)
#print(s,simpson(a,b,f,N))
domain = np.linspace(10,10010,10)
for i,j in enumerate(domain):
	solns[i] = simpson(a,b,f,j)
exact = solns[9]

solns2 = np.zeros(10)
#print(s,simpson(a,b,f,N))
domain2 = np.linspace(10,10010,10)
for i,j in enumerate(domain2):
	solns2[i] = rect(a,b,f,j)
exact2 = solns2[9]

#print(4.4-solns)
#print(4.4-solns2)

plt.subplot(221)
plt.plot(np.log(domain), np.log((abs(4.4-solns))/4.4))
plt.title('simpson relative error')
plt.subplot(222)
plt.plot(np.log(domain2), np.log((abs(4.4-solns2))/4.4))
plt.title('reiman relative error')

'''
simpRel = np.zeros(10)
for i in range(10)
simpRel = ()
'''

plt.subplot(223)
plt.plot(np.log(domain), np.log((abs(4.4-solns))/4.4))
plt.title('simpson convergence')
plt.subplot(224)
plt.plot(np.log(domain2), np.log((abs(4.4-solns2))/4.4))
plt.title('reiman convergence')
plt.show()
