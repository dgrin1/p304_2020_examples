#Define number of points and limits
N=10
a=0
b=2

#make an integer range covering # of points
ivec=range(0,N+1)
s=0
x=0

#obtain esstimate of step size
h=float(b-a)/float(N)

#define function
def f(x):
	f=np.power(x,4.e0)-2.*x+1.
	return f

#accumulate Riemann sum looping over all N function evaluations
for i in ivec:
	s+=f(x)*h
	x=a+i*h

#trapiezoidal rule function
#Syntax limits, function, Number of points
def trape(a,b,f,N):
#stepsize
	h=(b-a)/N
#End points
	s=(f(a)+f(b))*h
#Accumulate and normal sum by simpson formula
	for i in range(1,N):
		s+=2.*f(a+i*h)*h
	s/=2.0
	return s

#Call trapezoidal function to get integral estimate
trape(a,b,f,N)

#compare with riemann sum
print(s,trape(a,b,f,N))
