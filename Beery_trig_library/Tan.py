from Cos import myCos
from Sin import mySin
import math

def myTan(x):
    return mySin(x)/myCos(x)

print(myTan(math.pi/4))
