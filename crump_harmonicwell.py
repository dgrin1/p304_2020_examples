from numpy import array,arange,linspace
import matplotlib.pyplot as plt

# Constants
m = ((16*18)/(18+16))*(1.673e-27)    # Mass of CO kg
hbar = 1.0546e-34  # Planck's constant over 2*pi
e = 1.6022e-19     # Electron charge
L = 112.8e-12   # CO bonda length m
N = 1000
h = L/N
k=1857 #N/m

# Potential function
def V(x):
    V=(k*(x**2)/2)/(6.242e18)
    return V

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

    for x in arange(-L,L,h):
        k1 = h*f(r,x,E)
        k2 = h*f(r+0.5*k1,x+0.5*h,E)
        k3 = h*f(r+0.5*k2,x+0.5*h,E)
        k4 = h*f(r+k3,x+h,E)
        r += (k1+2*k2+2*k3+k4)/6

    return r[0]

Elist=linspace(1e-20,1e-18,100)
roots=[]
for E in Elist:
    root = solve(E)
    roots.append(root)

plt.plot(Elist,roots)
plt.show()

# Main program to find the energy using the secant method
E1 = 0.0
E2 = 1e-100
psi2 = solve(E1)

target = e/1000
while abs(E1-E2)>target:
    psi1,psi2 = psi2,solve(E2)
    E1,E2 = E2,E2-psi2*(E2-E1)/(psi2-psi1)

print("E =",E2/e,"eV")
