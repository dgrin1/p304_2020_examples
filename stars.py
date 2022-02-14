
from scipy import constants as sc
from numpy import loadtxt,array,dot,sqrt,cos,sin,linspace,log
import numpy as np
from math import pi

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rc('font',**{'family':'serif','serif':['Times New Roman']})
matplotlib.rc('text', usetex=True)
plt.ion()
data=loadtxt("stars.txt",float)
x=data[:,0]
y=data[:,1]
xbetter=[]
ybetter=[]

nstarsm1=np.size(x)

for i in range(0,nstarsm1):
	if y[i] <= 10:
		xbetter.append(x[i])
		ybetter.append(y[i])

subs=range(0,nstarsm1,5)
xsubs=x[subs]
ysubs=y[subs]

plt.plot(xbetter,ybetter, 'k^')
#plt.errorbar(xbetter,ybetter,xerr=.0001,yerr=.0001, c= 'b')


#sctter needs c=
plt.xlabel("Temperature in K")
plt.ylabel("Magnitude")
plt.xlim(0,13000)
plt.ylim(-5,20)
plt.show(block = True)
