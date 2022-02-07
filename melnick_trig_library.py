from math import factorial, pi

__eps = 1e-20

def fsin(x,epsilon=__eps):
    x = x % (2*pi)
    s1 = 1
    s2 = 0
    i = 0
    while(abs(s1-s2)>abs(s1*epsilon) and i<1e6):
        s1 = s2
        s2 += ((-1)**i)/(factorial(2*i+1)) * x**(2*i+1)
        i += 1
    return s2

def fcos(x,epsilon=__eps):
    x = x % (2*pi)
    s1 = 1
    s2 = 0
    i = 0
    while(abs(s1-s2)>abs(s1*epsilon) and i<1e6):
        s1 = s2
        s2 += ((-1)**i)/(factorial(2*i)) * x**(2*i)
        i += 1
    return s2

def ftan(x,epsilon=__eps):
    if fcos(x,epsilon)==0 :
        return 'Undefined'
    return fsin(x,epsilon)/fcos(x,epsilon)

def fsec(x,epsilon=__eps):
    if fcos(x,epsilon)==0 :
        return 'Undefined'
    return 1/fcos(x,epsilon)

def fcsc(x,epsilon=__eps):
    if fsin(x,epsilon)==0 :
        return 'Undefined'
    return 1/fsin(x,epsilon)

def fcot(x,epsilon=__eps):
    if fsin(x,epsilon)==0 :
        return 'Undefined'
    return fcos(x,epsilon)/fsin(x,epsilon)
