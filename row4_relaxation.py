import numpy as np
#original code author Simon Perales
def relax(func, x_init):
#relaxation iterator, pass it any function

#initial guess
    x = x_init
    i=0
#iterate until machine precision reached
    while func(x)!=x:
        x=func(x)
        i+=1
        print(i,x)
#relax and print out iteration values
    return x

def func1(x):
#example function for numerical relaxation
    return 2-np.exp(-x)

y = relax(func1, .9)
print(y)
