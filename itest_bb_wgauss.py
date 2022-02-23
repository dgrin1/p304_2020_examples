from scipy import constants as constants
import numpy as np
from gaussxw import gaussxw,gaussxwab

#new gaussian integral stuff

#Define number of points and limits
N=50

epsilon=1.e-10
#start integral close to x=0 because integrand still dierges
a=epsilon
b=1.-epsilon

#make an integer range covering # of points


#define function
def f(x):
    import numpy as np
    f=(x**3)*np.exp(-x)/(1.-np.exp(-x))
#    print(x,f)
    return f   

#integrand with chang eof variables that is good to infinity
def g(z):
    import numpy as np
    x=z/(1.-z)
    g=(x**3)*np.exp(-x)/((1.-np.exp(-x))*(1.-z)**2)
#    print(x,f)
    return g

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
#trape(a,b,f,N)

#compare with riemann sum, using both terms in thermal integral
s=(trape(a,1,f,N)+trape(1/2,b,g,N))
stefan=s*(constants.Boltzmann**4.e0)/(4.*(np.pi*constants.speed_of_light)**2.e0*(constants.hbar**3.))
N*=2
s=(trape(a,1,f,N)+trape(1/2,b,g,N))
stefan_better=s*(constants.Boltzmann**4.e0)/(4.*(np.pi*constants.speed_of_light)**2.e0*(constants.hbar**3.))
error=(stefan_better-stefan)/stefan
print(stefan,error,"simpson's rule with remapped infinity")

#New stuff for gaussian integrals
Ngauss=N

#obtain weights and positions of points in first half of integral
xvals,wp=gaussxwab(Ngauss,a,1)
s=0
#sum them up
for k in range(Ngauss):
    s += wp[k]*f(xvals[k])
#obtain weights and positions of points in second half of integral

xvals,wp=gaussxwab(Ngauss,1/2,b)
#s = 0.0
#sum
for k in range(Ngauss):
    s += wp[k]*g(xvals[k])
#add two components of integral

#print rest
stefan_gauss=s*(constants.Boltzmann**4.e0)/(4.*(np.pi*constants.speed_of_light)**2.e0*(constants.hbar**3.))
print(stefan_gauss,"My gauss")

#this time with scipy gauss quad
import scipy.integrate
t1=scipy.integrate.fixed_quad(f, a, 1, n=Ngauss)
t2=scipy.integrate.fixed_quad(g, 1/2, b, n=Ngauss)
stefan_scipy_gauss=(t1[0]+t2[0])*(constants.Boltzmann**4.e0)/(4.*(np.pi*constants.speed_of_light)**2.e0*(constants.hbar**3.))
print(stefan_scipy_gauss,"scipy Gaussian")
#,s*(t1[1]+t2[1])*(constants.Boltzmann**4.e0)/(4.*(np.pi*constants.speed_of_light)**2.e0*(constants.hbar**3.)))

t1=scipy.integrate.romberg(f, a, 1)
t2=scipy.integrate.romberg(g, 1/2, b)
stefan_scipy_romberg=(t1+t2)*(constants.Boltzmann**4.e0)/(4.*(np.pi*constants.speed_of_light)**2.e0*(constants.hbar**3.))
print(stefan_scipy_romberg,"scipy Romberg")









