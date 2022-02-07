import numpy as np
import math

def gsin(x):
#take arg mod 2pi
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	s,sold = 0.e0,0.e0

#Keep at most 10000 terms in the Taylor series
	for i in range(10000):
		sold=s
		s+= float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
#If converged to machine precision then break out of loop
		if sold==s: break
	return s

#We know that cos(x) = sin(x+pi/2)
def gcos(x):
	 c = gsin(x+(np.pi)/2)
	 return c

#We know that tan = sin/cos
def gtan(x):
	t = gsin(x)/gcos(x)
	return t

#cotan(x) = 1/tan(x)
def gcot(x):
	ct = 1/gtan(x)
	return ct

#sec(x) = 1/cos(x)
def gsec(x):
	sc = 1/gcos(x)
	return sc

#cosec(x) = 1/sin(x)
def gcosec(x):
	cs = 1/gsin(x)
	return cs
