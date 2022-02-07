""" Trig Function library
"""

import numpy as np
import math 
import doctest




def sin(x, err = 0.00000001):
    """" Computes sin of given value of x
    >>> err = 0.00000001
    >>> sin(1) - math.sin(1) < 1
    True

    >>> np.abs(sin(0.5) - math.sin(0.5)) < 1
    True

    >>> np.abs(sin(2*np.pi) - math.sin(2*np.pi)) < 1
    True 
    """

    # compute remainder to account for the periodicity of sin function  
    y = x % (2*np.pi)

    sin_y_prev = 0
    sin_y = 0

    for i in range(0,1000):
        sin_y_prev = sin_y

        sin_y += (-1)**i * ((y**(2*i+1))/math.factorial(2*i+1)) # taylor expansion

        if i > 1:
            if ((sin_y - sin_y_prev) < err):
                break

        

    return sin_y

def cos(x, err = 0.00000001):
    """" Computes cosine of given value of x
    >>> err = 0.00000001
    >>> cos(1) - math.cos(1) < err
    True

    >>> np.abs(cos(0.5) - math.cos(0.5)) < err
    True 

    >>> np.abs(cos(3.14) - math.cos(3.14)) < err
    True

    """


    # compute remainder to account for the periodicity of sin function  
    y = x % (2*np.pi)

    cos_y_prev = 0
    cos_y = 0

    for i in range(0,1000):
        cos_y_prev = cos_y
        cos_y += (-1)**i * ((y**(2*i))/math.factorial(2*i)) # taylor expansion

        if i > 1:
            if (np.abs(cos_y - cos_y_prev) < err):
                break

        
    
    return cos_y

def tan(x):
    return sin(x) / cos(x)


if __name__ == "__main__":
    import doctest
    doctest.testmod() # tests 


