#Jack Crump trig library

#import factorial and pi
from math import pi
from math import factorial

#define sin function
def sin(x):
    y=x%(2*pi) #deal with oscillation
    #set placeholder values
    s=0.
    sold=0.
    for i in range(1000):
        sold=s #set previous value
        s+=(-1)**i*((y**(2*i+1))/(factorial(2*i+1))) #run Taylor series
        if i>1 and (sold-s)<0.00001 and (sold-s)>-0.00001: #break condition
            break
    return s

#define cos function
def cos(x):
    y=x%(2*pi) #deal with oscillation
    #set placeholder values
    c=0.
    cold=0.
    for i in range(1000):
        cold=c #set previous value
        c+=(-1)**i*((y**(2*i))/(factorial(2*i))) #run Taylor series
        if i>1 and (cold-c)<0.00001 and (cold-c)>-0.00001: #break condition
            break
    return c

#define tan function
def tan(x):
    s=sin(x) #set sin
    c=cos(x) #set cos
    t=s/c #tan=sin/cos
    return t

#define csc function
def csc(x):
    s=sin(x) #set sin
    cs=1/s #csc=1/sin
    return cs

#define sec function
def sec(x):
    c=cos(x) #set cos
    se=1/c #sec=1/cos
    return se

#define cot function
def cot(x):
    t=tan(x) #set tan
    co=1/t #cot=1/tan
    return co
