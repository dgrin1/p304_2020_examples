import math

def myCos(x):
    tolerance = 10**(-12)
    sum = 1
    n = 1
    err = abs((sum - math.cos(x))/sum)

    while (err >= tolerance):

        if n % 2 == 0:
            numerator = 1
        else:
            numerator = -1
        denominator = math.factorial(2*n)

        sum += (numerator/denominator)*x**(2*n)

        err = abs((abs(math.cos(x)) - sum)/sum)#/math.cos(x))
        n += 1

    return sum
#print(myCos(math.pi/4))
#print(math.cos(math.pi/4))
