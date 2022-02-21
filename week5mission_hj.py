#!/usr/bin/env python
# coding: utf-8

# In[29]:


#trapezoid method for a more fun integral
#part 1
from matplotlib.pyplot import *
import matplotlib.pyplot as plt
from __future__ import print_function,division
import numpy as np
N=100
a=0
b=2

ivec=range(0,N+1)
s=0
x=0
h=float(b-a)/float(N)

def f(x):
    f=np.power((x-1),5.e0)-5.*x*(np.sin(5*x))
    return f

def inte(x):
    inte = 1/6*(-1+x)**6-x*np.cos(5*x)-1/5*np.sin(5*x)
    return inte 

#reiman sum integral
def reiman(a,b,f,N):
    x=0
    s=0
    h=float(b-a)/float(N)
    for i in ivec:
        s+=f(x)*h
        x=a+i*h
    return s 

#trapezoid integral    
def trape(a,b,f,N):
    h=(b-a)/N
    s=(f(a)+f(b))*h
    for i in range(1,N):
        s+=2.*f(a+i*h)*h
    s/=2.0
    return s

trape(a,b,f,N)

print(reiman(a,b,f,N),trape(a,b,f,N))


# In[32]:


#part 3

Nlist = []
valueN =[]
error = []

for N in range (10,1000,10):
    num = trape(a,b,f,N)
    exa = inte(N)
    errornumber = exa/num - 1
    
    
    
    Nlist.append(N)
    valueN.append(exa)
    error.append(errornumber)

y=np.abs(error)
x=range(10,1000,10)

    
        
plt.loglog(x,y)

    


# In[ ]:




