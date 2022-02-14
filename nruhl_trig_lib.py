# These trig functions are accurate to 8 decimal places

import math
import numpy as np

def sin(x):
    # Define term at n and n-1
    # start old sum at a non-zero number 
    s = 0.
    sum_old = 0.

    summ = 0   # total sum
    # We saw that > 51 breaks
    for n in range(50):
        # Once we get to a certain level of accuracy in terms ofdecimals, we will stop adding new terms to the sum.
        # Always include the first two terms
        if n > 1 and float(abs(summ - sum_old)) < 10e-8:
            break
        else:
            s = float((-1)**(n)*x**(2*n+1))/float(math.factorial(2*n+1))
            sold = s
            summ += s
    return summ

def cos(x):
    cosine = sin(x+0.5*math.pi)
    return cosine

def tan(x):
    return sin(x)/cos(x)

def csc(x):
    return 1/sin(x)

def sec(x):
    return 1/cos(x)

def cot(x):
    return 1/tan(x)

def main():
    print(tan(10))
    print(np.tan(10))
    return 0

if __name__ == '__main__':
    main()