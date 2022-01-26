#import numpy as np
#from math import log, sin, cos, pi
from numpy import log, sin, cos, pi

#overkill in python 2 which can read in floats but necessary in python 3 which reads everything as a string initially


#Read in r and theta values
r=float(input("What is the radius?"))
th=float(input("What is the angle in degrees?"))
#convert strings to floats

#convert angle from degrees to radians
th_rad=th *pi/180.

# get x and y values with standard trig formulae
x=r*cos(th_rad)
y=r*sin(th_rad)

#output results to user
print("Cartesian coordinates x=",x,"y=",y)