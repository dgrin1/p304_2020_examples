import math


def sin(x):
    x = x% (2*math.pi)
    y=0
    sum =0.0
    for i in range(0,20):
        sum =y+sum
        y = y+  (x**(2*i+1)*(-1)**i)/math.factorial(2*i+1)
    return y

def cos(x):
    x = x% (2*math.pi)

    if x > math.pi/2 and x< 3*math.pi/2 :
        return -1* math.sqrt(1- sin(x)**2)
    else:
        return math.sqrt(1- sin(x)**2)


def tan(x):
    if cos(x)==0:
        print("Tan is undefined")
        return
    return sin(x)/cos(x)

def cotan(x):
    if sin(x)==0:
        print("Cotan is undefined")
        return
    return cos(x)/sin(x)

def cosec(x):
    if sin(x)== 0:
        print("Cosec is undefined")
        return

    return 1/sin(x)

def sec(x):
    if cos(x)==0:
        print("Sec is undefined")
        return
    return 1/cos(x)
