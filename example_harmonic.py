from __future__ import division,print_function

from numpy import loadtxt,array,dot
s=0
t=0.1
for k in range(1,101):
	s+=1./k
	t*=1./k
print(s)
