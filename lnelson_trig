import numpy as np

def sin(x, epsilon=0.001):
    """
    Calculates the sine of x (in radians) using a taylor expansion
    :param x: The input of the sine function
    :param epsilon: The maximum allowable proportional error
    :return: The sine of x
    """
    summand = 1
    if x % (2*np.pi) > np.pi:  # If sin x is negative, switch the sign
        summand = -1

    x = x % np.pi  # Remap using the identity sin(n*pi+x) = (+ or -) sin(x)
    x = min(x, np.pi-x)  # Remap using the identity sin(x) = sin(pi - x)
    summand *= x  # The first term in the summation is x (or -x if we're in a region where sin x is negative)
    out = 0
    for n in range(100):
        out += summand
        if out == 0 or abs(summand/out) <= epsilon:  # If the new term added < a certain fraction of the current output, end
            break
        summand *= -x*x/((2*n+3)*(2*n+2))
        # Each term in the sum is the previous term times -x^2 divided by the next two terms in the factorial
    # print(f'Ended after {n} iterations')
    return out

def cos(x, epsilon=0.001):
    """
    Calculates the cosine of x (in radians) using the sin function
    :param x: Input
    :param epsilon: The maximum allowable proportional error
    :return: Cosine of x
    """
    return sin(np.pi/2 - x, epsilon)

def tan(x, epsilon=0.001):
    """
    Calculates the tangent of x (in radians) using the sin and cos functions
    :param x: Input
    :param epsilon: The maximum allowable proportional error in the inputs
    :return: Tangent of x
    """
    return sin(x,epsilon)/cos(x,epsilon)

def cot(x, epsilon=0.001):
    """
    Calculates the cotangent of x (in radians) using the sin and cos functions
    :param x: Input
    :param epsilon: The maximum allowable proportional error in the inputs
    :return: Cotangent of x
    """
    return cos(x,epsilon)/sin(x,epsilon)

def sec(x, epsilon=0.001):
    """
    Calculates the secant of x (in radians) using the cos function
    :param x: Input
    :param epsilon: The maximum allowable proportional error in the inputs
    :return: Secant of x
    """
    return 1/cos(x,epsilon)

def csc(x, epsilon=0.001):
    """
    Calculates the cosecant of x (in radians) using the sin function
    :param x: Input
    :param epsilon: The maximum allowable proportional error in the inputs
    :return: Cosecant of x
    """
    return 1/sin(x,epsilon)

def arcsin(x):
    if x>1 or x<0:
        raise ValueError("Argument of arcsin must be in [-1,1]")

    start, end = -np.pi/2, np.pi/2
    while start != end:
        mid = (start + end)/2
        # print(f'Finding sine of {mid}:')
        curr = sin(mid, 0)
        # print(f'  Returned {curr}')
        if curr == x:
            return mid
        elif curr < x:
            start = mid
        else:
            end = mid


sin_short = lambda x: sum((-1)**n*(x%(2*np.pi))**(2*n+1)/np.prod([i for i in range(1,2*n+2)], dtype=np.longlong) for n in range(20))


if __name__ == "__main__":
    test_in = 1
    print(cos(test_in, epsilon=0))
    print(np.cos(test_in))
    # print(sin(test_in))
    # print(sin(test_in, epsilon=1e-10))
    # print(sin(test_in, epsilon=0))
    # print(sin_short(test_in))
    # print(np.sin(test_in))




