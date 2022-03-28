from numpy import zeros,empty
from pylab import plot,show

def springs(omeg):

    # Constants
    N = 26
    C = 1.0
    m = 1.0
    k = 6.0
    omega = omeg
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

    return x


x1 = springs(0.6)  # plug in omega
x4 = springs(0.9)  # plug in omega
x2 = springs(1.2)  # plug in omega
x5 = springs(1.5)  # plug in omega
#x3 = springs(1.8)  # plug in omega
#x6 = springs(2.1)  # plug in omega

# Make a plot using both dots and lines
plot(x1)
plot(x1,"ko")
plot(x2)
plot(x2,"ko")
#plot(x3)
#plot(x3,"ko")
plot(x4)
plot(x4,"ko")
plot(x5)
plot(x5,"ko")
#plot(x6)
#plot(x6,"ko")

show()
