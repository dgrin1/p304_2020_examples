def sin_func(x):
    # import pi
    from math import pi
    from math import factorial

    # make sure number (y) is between 0 and 2pi
    if x <= 2*pi:
        y = x
    else:
        y = x%(2*pi)

    # initialize sin storage variable siny
    siny = 0

    # calculate sin(y) using for loop and Taylor series
    for i in range(0,1000):
        newterm = (-1)**i * (y**(2*i+1))/(factorial(2*i+1))
        if (abs((siny + newterm) - siny) < 0.0001): break
        siny += newterm

    # print output
    print("The sin of",x,"is",siny)

# ------------------------------------------------------------------------------

def cos_func(x):
    # import pi
    from math import pi
    from math import factorial

    # make sure number (y) is between 0 and 2pi
    if x <= 2*pi:
        y = x
    else:
        y = x%(2*pi)

    # initialize cos storage variable siny
    cosy = 0

    # calculate sin(y) using for loop and Taylor series
    for i in range(0,1000):
        newterm = (-1)**i * (y**(2*i))/(factorial(2*i))
        if (abs((cosy + newterm) - cosy) < 0.0001): break
        cosy += newterm

    # print output
    print("The cosine of",x,"is",cosy)
