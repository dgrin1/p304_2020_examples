import numpy as np
import math

def gsin(x):
    #take arg mod 2pi
	x = x % (2*np.pi)
    #initialize iterator and sum
	s,sold = 0.e0,0.e0

    #Keep at most 1000 terms in the Taylor series
	for i in range(1000):
		sold = s
		s += float((-1)**i * ((x**(2*i+1)))/float(math.factorial(2*i+1)))
        #If converged to machine precision then break out of loop
		if abs(sold-s) < 10.e-14: break
	return s

def gcos(x):
    x = x%(2.e0*np.pi)
    i = 0
    s,sold = 0.e0, 0.e0

    for i in range(1000):
        sold = s
        s += float(((-1)**i) * (x**(2*i)))/float(math.factorial(2*i))
        if i > 1 and abs(sold-s) < 10.e-14: break
    return s

def gtan(x):
    if gcos(x) == 0:
        print("Tangent is not defined.")
    return gsin(x)/gcos(x)

def gsec(x):
    if gcos(x) == 0:
        print("Secant is not defined.")
    return 1/gcos(x)

def gcsc(x):
    if gsin(x) == 0:
        print("Cosecant is not defined.")
    return 1/gsin(x)

def gcot(x):
    if gsin(x) == 0:
        print("Cotangent is not defined.")
    return gcos(x)/gsin(x)