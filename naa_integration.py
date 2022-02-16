import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

def f(x):
    return x**4 - 2*x + 1

# Conduct Reimann sums with N steps
def problem1(N):
    a = 0
    b = 2
    h = float(b-a)/float(N)

    # non-inclusive of endpoint
    ivec = np.arange(a, b+h, h)
    ys = f(ivec)
    
    left_s = 0
    right_s = 0
    mid_s = 0
    trap_s = (f(a) + f(b))*h/2

    for i in ivec[:-1]:
        left_s += f(i)*h

    for i in ivec[1:]:
        right_s += f(i)*h

    for i in ivec[:-1]:
        mid = i + (h/2)
        mid_s += f(mid)*h

    for i in ivec[:-1]:
        trap_s += f(i)*h

    # Simppson's rule
    s_even = 0
    s_odd = 0
    for i, val in enumerate(ivec):
        if i % 2 == 0:
            s_even += f(val)
        else:
            s_odd += f(val)
    simp_s = (h / 3) * (f(a) + f(b) + 4*s_odd + 2*s_even)

    

    print(f"Reimann sums with {N} steps: ")
    print(f"left sum = {left_s}")
    print(f'right_sum = {right_s}')
    print(f'mid sum = {mid_s}')
    print(f"trap_sum = {trap_s}")
    print(f"simp_sum = {simp_s}")
    py_int_quad = integrate.quad(f, a, b)
    print(f'integrate.quad = {py_int_quad}')
    print(f'Value = {float(22/5)}')

    plt.plot(ivec, ys)
    plt.show()
    
    return

if __name__ == "__main__":
    problem1(N=10)
