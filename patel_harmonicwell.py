from numpy import array,arange
import numpy as np
import matplotlib.pyplot as plt
# Constants
m = 9.1094e-31     # Mass of electron
hbar = 1.0546e-34  # Planck's constant over 2*pi
e = 1.6022e-19     # Electron charge
L = 5.2918e-11     # Bohr radius
N = 1000
h = L/N
k = 1857 # N/m

# Potential function
def V(x):
    return ( (k * x) / 2 ) * (6.242e18)

def f(r,x,E):
    psi = r[0]
    phi = r[1]
    fpsi = phi
    fphi = (2*m/hbar**2)*(V(x)-E)*psi
    return array([fpsi,fphi],float)

# Calculate the wavefunction for a particular energy
#vaue of the wave function Psi(L)
def solve(E):
    psi = 0.0
    phi = 1.0
    r = array([psi,phi],float)
    x_list = np.arange(0,L,h)
    for x in x_list:
        k1 = h*f(r,x,E)
        k2 = h*f(r+0.5*k1,x+0.5*h,E)
        k3 = h*f(r+0.5*k2,x+0.5*h,E)
        k4 = h*f(r+k3,x+h,E)
        r += (k1+2*k2+2*k3+k4)/6

    return r[0]

# Main program to find the energy using the secant method
E_list = np.linspace(0,e,1000)
root = np.linspace(0, e,1000)
roots = [solve(r) for r in root]
print(roots)
E1 = 0
E2 = e
psi2 = solve(E1)
#print(len(psi2))
x_list = np.arange(0,L,h)
# x = np.linspace(0,L, 1000)
plt.plot(E_list,roots)
plt.show()

target = e/1000
while abs(E1-E2)>target:
    psi1,psi2 = psi2, solve(E2)
    E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)

print("E =",E2/e,"eV")
