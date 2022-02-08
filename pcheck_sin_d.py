import matplotlib.pyplot as plt
import numpy as np
#plt.ion only works in interactive mode
plt.ion()

#set fonts
plt.rc('text',usetex=True)
plt.rc('font', **{'family':'sans-serif','sans-serif':['Helvetica']})
plt.rc('font', **{'family':'serif','serif':['Times New Roman']})

#create arrays
x=np.linspace(0,2*np.pi,100)
y=np.sin(x)
x2=np.linspace(0,2*np.pi,15)
y2=np.sin(x2)
y3=np.sin(x2+.4)

#make multiple plots on one panel
al=plt.plot(x,y,'k')

ble=0.1*y2
plt.errorbar(x2,y2,yerr=ble,fmt='c^')

#formatting and size of symbols

#linewidth
plt.setp(al,linewidth=2)

#limits
plt.ylim([-1.1,1.1])

#labels in latex
plt.ylabel(r'$\Gamma$',fontsize=24)
plt.xlabel(r'$\omega t$',fontsize=16)

plt.show()

#nice output with set resolution
plt.savefig('ocean.pdf',format='pdf',dpi=1000)
