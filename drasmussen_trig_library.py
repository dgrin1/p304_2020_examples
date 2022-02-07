import numpy as np
import math

def sine(x):
#take arg mod 2pi (radians)
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	s,sold = 0.e0,0.0001e0

#Keep at most 10000 terms in the Taylor series
	for i in range(10000):
		sold=s
		s+= float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
#If converged to machine precision then break out of loop
		if sold==s: break
	return s

#print(sine(0))

def cosine(x):
#take arg mod 2pi (radians)
	x=x%(2.e0*np.pi)
#initialize iterator and sum
	i = 0
	s,sold = 0.e0,0.0001e0

#Keep at most 10000 terms in the Taylor series
	for i in range(10000):
		sold=s
		s+= float(((-1)**i) * (x**(2*i))/float(math.factorial(2*i)))
#If converged to machine precision then break out of loop
		if sold==s: break
	return s


