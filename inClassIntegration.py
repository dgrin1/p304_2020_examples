import numpy as np
from scipy import integrate

#Set some values
N=10

a1=0
b1=2

a2=0
b2=np.pi

#function 1
def f1(x):
    return x**4 - 2*x + 1

#function 2
def f2(x):
    return np.sin(x)


r1 = np.linspace(a1,b1,N+1)
r2 = np.linspace(a2,b2,N+1)

#riemann sum method 1

riemann1 = np.sum(f1(r1)[:-1])*(b1-a1)/N

#trapezoid method 1

trap1 = (np.sum(f1(r1)[:-1])+(f1(r1)[0]+f1(r1)[-1])/2)*(b1-a1)/N

#riemann sum method 2

riemann2 = np.sum(f2(r2)[:-1])*(b2-a2)/N

#trapezoid method 2

trap2 = (np.sum(f2(r2)[:-1])+(f2(r2)[0]+f2(r2)[-1])/2)*(b2-a2)/N

#scipy quadrature on f1
quad1 = integrate.fixed_quad(f1, a1, b1)

#scipy quadrature on f2
quad2 = integrate.fixed_quad(f2, a2, b2)

print("the results for f1 are: \n riemann:",riemann1,"\n trapezoid:",trap1,"\n Scipy quadrature:",quad1[0])
print("the results for f2 are: \n riemann:",riemann2,"\n trapezoid:",trap2,"\n Scipy quadrature:",quad2[0])

#TODO: make plot
