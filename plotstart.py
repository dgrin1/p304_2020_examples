from __future__ import division,print_function
import matplotlib.pyplot as plt
import numpy as np

#go into interactive mode
plt.ion()

#Use Latex fonts
plt.rc('text',usetex=True)

#dense x grid for theory curve
x=np.linspace(0,2*3.14159,1000)

#y values for sin good theory
y=np.sin(x)

#y values list for bad sin theory
ybad=np.cos(x)

#two panel subplots
plt.subplot(211)

#coarsely gridded "data"
xdata=np.linspace(0,2*3.14159,10)

#make data points obey sin curve
ydata=np.sin(xdata)

#Add label
plt.plot(x,y,label='theory')


#plot "data"
plt.plot(xdata,ydata,'bo',label='data')

#Plot title
plt.title('Climate change is a bummer')

#axis labels
#plt.xlabel('Time')
plt.ylabel('Height of ocean in meters')

#limits
plt.xlim([0,6])
plt.ylim([-1.3,1.3])

#put down a legend
plt.legend(loc=1)

#move to next panel
plt.subplot(212)

#axis labels
plt.xlabel(r'\omega t',fontsize=24)
plt.ylabel('Height of ocean in meters')

#limits again
plt.xlim([0,6])
plt.ylim([-1.3,1.3])

#plot bad cosine fit
plt.plot(x,ybad,label='bad theory')

#plot additional data points
plt.plot(xdata,ydata,'bo',label='data')
plt.grid()




plt.show()
plt.savefig('test.pdf',format='pdf')

