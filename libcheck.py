import numpy as np
import math

def gsin(x):
#take arg mod 2pi
#initialize iterator and sum
	i = 0
	s,sold = 0.e0,0.0001e0

#Keep at most 10000 terms in the Taylor series
	for i in range(10000):
		s+= float((((-1)**i) * (x**((2*i) + 1))))/float(math.factorial(((2*i) + 1)))
#If converged to machine precision then break out of loop
		continue_criterion=(((s-sold)/sold)>0.00000000001)
		print(continue_criterion)
		if (continue_criterion==0): break
		sold=s

	return s

def fac(n):
	i=1
	val=i
	while i<=n:
		val*=i
		i+=1
	return val
