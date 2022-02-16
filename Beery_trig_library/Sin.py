import math

def mySin(x):
    tolerance = 10**(-12)
    x = x%(2*math.pi)
    sum = x
    n = 1
    err = abs(sum - math.sin(x)/sum)#math.sin(x)

    #print(err)
    #print(tolerance)

    while (err >= tolerance):

        if n % 2 == 0:
            numerator = 1
        else:
            numerator = -1
        denominator = math.factorial(2*n+1)

        sum += (numerator/denominator)*x**(2*n+1)

        err = (abs(math.sin(x) - sum)/sum)#math.sin(x)
        n += 1
        #print(err)
        #print(err)
    return sum
print(mySin(math.pi*16.5))
print(math.sin(math.pi*16.5))
