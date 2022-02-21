# Noah, Anthony and Nate integration class work

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

def f(x):
    return x**4 - 2*x + 1

def simpson(a, b, f, N):
    # Simppson's rule
    h = float(b-a)/float(N)
    ivec = np.arange(a, b+h, h)
    s_even = 0
    s_odd = 0
    for i, val in enumerate(ivec):
        if i % 2 == 0:
            s_even += f(val)
        else:
            s_odd += f(val)
    simp_s = (h / 3) * (f(a) + f(b) + 4*s_odd + 2*s_even)
    return simp_s

# Trapezoidal rule
def trape(a, b, f, N):

    h = float(b-a)/float(N)
    ivec = np.arange(a, b+h, h)

    trap_s = (f(a)+f(b))*h/2
    for i in ivec[:-1]:
        trap_s += f(i)*h
    return trap_s

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

def make_convergence_plot():
    a = 0
    b = 2
    N_list = np.arange(10, 1001, 1)
    trap_list = np.array([trape(a, b, f, N) for N in N_list])    # values of the integral
    simp_list = np.array([simpson(a, b, f, N) for N in N_list])
    error_trap = np.abs((trap_list - 4.4) / 4.4)
    error_simp = np.abs((simp_list - 4.4) / 4.4)
    plt.plot(N_list, error_trap, label="Trapezoidal Error")
    plt.plot(N_list, error_simp, label="Simpson's Error")
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel("N slices in integral")
    plt.ylabel("Relative Difference from Analytical value")
    plt.legend()
    plt.show()
    return 0

if __name__ == "__main__":
    make_convergence_plot()
    # problem1(N=100)
