#sums_turner_hedy.py
#@author: TEJ
#@date: 2022-02-14

import numpy as np

N = 10 
a=0 #low limit of integration: start
b=2 #up limit of integratino: stop

iterator_array = np.arange(a,b+(a+b)/N,(a+b)/N)

s=0
x=0
h=float(b-a)/float(N)

def func(x):
	f=x**4-2*x+1
	return f
	
for i in iterator_array:
	s+=func(x)*h 
	x=a+i*h

def team_simp(a,b,f,N):
	h=(b-a)/N
	s=(func(a)+func(b))*h
	for i in range(1,N):
		s+=2.*f(a+i*h)*h
	s/=2.0
	return s
	
team_simp(a,b,func,N)

print(s,team_simp(a,b,func,N))
