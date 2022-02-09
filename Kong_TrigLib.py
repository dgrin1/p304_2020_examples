import math as math
import numpy as np

def sin(x):
    x = x % (2*np.pi)
    sinx = 0.0
    sold = 0.0
    for i in range(50):
        sinx = sold
        sinx += (x ** (2 * i + 1) * (( - 1) ** i)) / math.factorial(2 * i + 1)
        if abs(sold-sinx)<0.00001:
            break
    return sinx

def cos(x):
    x = x % (2*np.pi)
    cosx = 0.0
    cold = 0.0
    for i in range(50):
        cosx = cold
        cosx += (x ** (2 * i ) * ( - 1) ** i) / math.factorial(2 * i)
        if abs(cold-cosx)<0.00001:
            break
    return cosx


def tan(x):
    if cos(x)==0:
        print("Tan is undefined")
    else:
        return sin(x)/cos(x)

def cotan(x):
    if sin(x)==0:
        print("Cotan is undefined")
    else:
        return cos(x)/sin(x)

def sec(x):
    if cos(x)==0:
        print("Sec is undefined")
    else:
        return 1/cos(x)

def cosec(x):
    if sin(x)== 0:
        print("Cosec is undefined")
    else:
        return 1/sin(x)

print(sin(np.pi))