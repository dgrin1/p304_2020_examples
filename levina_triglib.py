import numpy as np
from math import pi, factorial

#Sasha Levina trig library

def sine(x):
    x = x%(2*pi)
    s, s_old = 0, 0.00001

    for i in range(10000):
        s = s_old
        s += (((-1)**i)*(x**(2*i + 1)))/factorial(2*i + 1)
        if (s - s_old)/s_old >= 0.00001: break
    return s

def cosine(x):
    x = x%(2*pi)
    s, s_old = 0, 0.00001

    for i in range(10000):
        s = s_old
        s += (((-1)**i)*(x**(2*i)))/factorial(2*i)

        if (s - s_old)/s_old >= 0.00001: break
    return s

def tangent(x):
    x = x%(2*pi)

    s =  sine(x)/cosine(x)

    return s

def cotangent(x):
    x = x%(2*pi)
    
    s = cosine(x)/sine(x)

    return s


def secant(x):
    x = x%(2*pi)

    s = 1/cosine(x)

    return s


def secant(x):
    x = x%(2*pi)

    s = 1/sine(x)

    return s

