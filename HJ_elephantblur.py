#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')


# 
# # Simple image blur by convolution with a Gaussian kernel
# 
# 
# Blur an an image (:download:`../../../../data/elephant.png`) using a
# Gaussian kernel.
# 
# Convolution is easy to perform with FFT: convolving two signals boils
# down to multiplying their FFTs (and performing an inverse FFT).
# 
# 
# 

# In[38]:


import numpy as np
from scipy import fftpack
import matplotlib.pyplot as plt


# The original image
# ####################################################################
# 
# 

# In[93]:


# read image
img = plt.imread('elephant.png')
plt.figure()
plt.imshow(img)


# Prepare an Gaussian convolution kernel
# ####################################################################
# 
# 

# In[94]:


# First a 1-D  Gaussian
t = np.linspace(-10, -10, 100)
bump = np.exp(-t*t/(2*(0.5**2)))
bump /= np.trapz(bump) # normalize the integral to 1

# make a 2-D kernel out of it
kernel = bump[:, np.newaxis] * bump[np.newaxis, :]


# Implement convolution via FFT
# ####################################################################
# 
# 

# In[109]:


# Padded fourier transform, with the same shape as the image
# We use :func:`scipy.signal.fftpack.fft2` to have a 2D FFT
kernel_ft = fftpack.fft2(kernel, shape=img.shape[:2], axes=(0, 1))

# convolve
img_ft = fftpack.fft2(img, axes=(0, 1))
# the 'newaxis' is to match to color direction
img2_ft = kernel_ft[:, :, np.newaxis] * img_ft
img2 = fftpack.ifft2(img2_ft, axes=(0, 1)).real

# clip values to range
img2 = np.clip(img2, 0, 1)

# plot output
plt.figure()
plt.imshow(img2)
#plt.imshow(kernel)
img.shape[:3]


# Further exercise (only if you are familiar with this stuff):
# 
# A "wrapped border" appears in the upper left and top edges of the
# image. This is because the padding is not done correctly, and does
# not take the kernel size into account (so the convolution "flows out
# of bounds of the image").  Try to remove this artifact.
# 
# 

# A function to do it: :func:`scipy.signal.fftconvolve`
# ####################################################################
# 
#  The above exercise was only for didactic reasons: there exists a
#  function in scipy that will do this for us, and probably do a better
#  job: :func:`scipy.signal.fftconvolve`
# 
# 

# In[110]:


from scipy import signal
# mode='same' is there to enforce the same output shape as input arrays
# (ie avoid border effects)
img3 = signal.fftconvolve(img, kernel[:, :, np.newaxis], mode='same')
plt.figure()
plt.imshow(img3)


# Note that we still have a decay to zero at the border of the image.
# Using :func:`scipy.ndimage.gaussian_filter` would get rid of this
# artifact
# 
# 

# In[111]:


plt.imshow(img[:, :, 0])


# In[112]:


plt.imshow(img[:, :, 1])


# In[113]:


plt.imshow(img[:, :, 2])


# In[114]:


plt.imshow(img[:, :, 3])


# In[47]:


kernel_ft.shape


# In[ ]:




