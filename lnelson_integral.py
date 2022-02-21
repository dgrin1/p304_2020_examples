import numpy as np
import scipy.integrate as sint
import matplotlib.pyplot as plt

# f = lambda x: x**4 - 2*x + 1

def l_riemann(a,b,f,n):
    domain = np.linspace(a,b,n+1)
    out = f(domain)
    sum = np.sum(out[:-1])
    return sum*(b-a)/n


def trape(a,b,f,n):
    domain = np.linspace(a,b,n+1)
    out = f(domain)
    sum = np.sum(out[1:-1]) + (out[0]+out[-1])/2
    return sum*(b-a)/n


def simps(a,b,f,n):
    domain = np.linspace(a, b, n//2+1)
    alt_d = (domain[:-1] + domain[1:])/2
    out = f(domain)
    alt_out = f(alt_d)
    sum = out[0] + out[-1] + 4*np.sum(alt_out) + 2*np.sum(out[1:-1])
    return sum*(b-a)/(6*(n//2))



if __name__=="__main__":
    a, b = 0, 3*np.pi/2
    n = 10
    func = np.sin
    true_val = 1
    print(f'The left Riemann sum from {a} to {b} with {n} intervals is {trape(a,b, func,n)}')
    print(f'The trapezoid sum from {a} to {b} with {n} intervals is {trape(a,b, func,n)}')
    print(f'The Simpson integral from {a} to {b} with {n} intervals is {simps(a,b, func,n)}')
    print(f'The Romberg integral from {a} to {b} is {sint.romberg(func,a,b)}')

    testgrid = np.logspace(1, 3, 50)
    abs_plot, abs_ax = plt.subplots()
    rel_plot, rel_ax = plt.subplots()

    for method, label in ((l_riemann, 'Riemann'), (trape, 'Trapezoid'), (simps, 'Simpson')):
        output = np.array([method(a, b, func, int(N)) for N in testgrid])
        double_output = np.array([method(a, b, func, int(2*N)) for N in testgrid])
        print(label, abs(output-true_val))
        # print('Testgrid:', testgrid)
        abs_ax.plot(testgrid, abs(output-true_val)/true_val, label=label)
        rel_ax.plot(testgrid, abs(double_output-output)/double_output, label=label)
    abs_ax.set(xscale="log", yscale="log", ylabel="Fractional Error", xlabel="Number of points",
               title="Error Relative to True Value")
    abs_ax.legend()

    rel_ax.set(xscale="log", yscale="log", ylabel="Fractional error", xlabel="Number of points",
               title="Error Relative to 2N")
    rel_ax.legend()

    plt.show()
