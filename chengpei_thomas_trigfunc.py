#Thomas Dandino and Chengpei
import math
from math import *
#Defining my own function to compute the value of sine(n)!
def gsin(x):
    print(x)
    while x>2*(pi):
        x=x-2*(pi)
        #print(x)
    s = 0
    s_temp = 0.000001
    for n in range(0,10000):
        s_temp = (-1)**(n)*x**(2*n+1)/(factorial(2*n+1))
        #print(s_temp)
        #print(s)
        if abs(s_temp) < 0.0000001:
            return s
            break
        else:
            s = s+s_temp
            print(s)
    return s

x=float(input("Please enter a numerical value for x: "))
print(gsin(x))


def gcos(x):
    return gsin(x+(pi/2))

def gtan(x):
    return gsin(x)/gcos(x)
