# coded by: rakeeb

import numpy as np 
import matplotlib.pyplot as plt 

numpoints = 1024
x = np.random.rand(numpoints)  # 1024 uniformy distributed random numbers
dx = 1 # there is actually no dx so we assume just 1

ft_x = np.fft.fft(x, norm='ortho') # fourier transform
k  = 2*np.pi*np.fft.fftfreq(numpoints)  # k values
min_k = np.amin(k)
print('Minimum k value:',min_k)

conv = np.convolve(x,x,'same')/(2*numpoints) # convolution with self
P_xx = np.abs(dx*np.sqrt(numpoints/(2.0*np.pi))*np.fft.fft(conv,norm='ortho')) # the power spectrum

#plotting of power spectrum
plt.plot(k,P_xx,'black')
plt.title('Plot of the Power Spectrum ')
plt.xlabel('k',fontsize=12)
plt.ylabel('Power spectrum',fontsize=12)
plt.xlim(-2,2)
plt.ylim(0,8)
plt.grid(color='b', linestyle='--', linewidth=0.5)
plt.show()

#plotting the histogarm of power spectrum
plt.hist(P_xx ,bins=5) 
plt.title('Histogram of Power Spectrum ')
plt.xlabel('Power spectrum',fontsize=12)
plt.ylabel('n',fontsize=12)
plt.xlim(0,10)
plt.show()

# I am actually not sure about the last part and the graph!!