import numpy as np
import matplotlib.pyplot as plt

# initialize LaTeX font for plots
plt.rc('text',usetex=True)
plt.rc('font', **{'family':'serif','serif':['Times New Roman']}) 



def trapezoid(a, b, N):

    """ Performs trapezoidal integration on function f.

        Parameters: 
        a,b - limits of integration 
        N - number of slices for our integration 
    """

    def f(x):
        """ integrand function """
        return x**4 - 2*x + 1

    h = (b-a) / N 

    sum = (0.5 * f(a)) + (0.5 * f(b))

    for k in range(1,N):

        sum += f(a+k*h)
        #print(sum)

    return sum * h



def frac_err_first(a, b, N):
    """ Computes the fractional error of our gaussian function as a function of the step size N (eqn 5.20 from Newman)
        Parameters:
        a, b - limits of integration
        N - the number of slices of the integral
    """
    integral = trapezoid(a, b, N)
    
    return (integral - 4.4) / 4.4
    

N = 1000 # number of points 
a = 0 # limits of integration
b = 2.

frac_err = []
print("Integral using Trapezoid Rule", trapezoid(a,b,N))

for i in range(1,N,1):
    frac_err.append(frac_err_first(a,b,i))

plt.plot(np.arange(1,N,1),frac_err)
plt.xlabel("N")
plt.ylabel("Fractional Error")
plt.yscale('log')
plt.xscale('log')
plt.show()