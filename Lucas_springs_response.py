from numpy import zeros,empty
import numpy as np
from pylab import plot, show, legend

# Constants
N = 26
C = 1.0
m = 1.0
k = 6.0
omega = 0.5
alpha = 2*k-m*omega*omega

maxes = []
omegas = []
for omega in np.arange(0, 3, 0.025):
    alpha = 2*k-m*omega*omega
    # Set up the initial values of the arrays
    A = zeros([N,N],float)
    for i in range(N-1):
        A[i,i] = alpha
        A[i,i+1] = -k
        A[i+1,i] = -k
    A[0,0] = alpha - k
    A[N-1,N-1] = alpha - k

    v = zeros(N,float)
    v[0] = C

    # Perform the Gaussian elimination
    for i in range(N-1):

        # Divide row i by its diagonal element
        A[i,i+1] /= A[i,i]
        v[i] /= A[i,i]

        # Now subtract it from the next row down
        A[i+1,i+1] -= A[i+1,i]*A[i,i+1]
        v[i+1] -= A[i+1,i]*v[i]

    # Divide the last element of v by the last diagonal element
    v[N-1] /= A[N-1,N-1]

    # Backsubstitution
    x = empty(N,float)
    x[N-1] = v[N-1]
    for i in range(N-2,-1,-1):
        x[i] = v[i] - A[i,i+1]*x[i+1]

    # Make a plot using both dots and lines
    # plot(x, label=f'$\\omega={omega}$')
    # plot(x,"ko")
    maxes.append(max(x))
    omegas.append(omega)
# legend()
# show()
plot(omegas, maxes)
show()
