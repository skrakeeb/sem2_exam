# coded by: rakeeb

import numpy as np 
import matplotlib.pyplot as plt 

# The given function:
def f(x):
	if abs(x) < 1 :
		return(1)
	else :
		return(0)
x_min = -2
x_max = 2
num_points = np.array([50,200,400]) # taking three values of number of points

for i in range(num_points.size):
	dx = (x_max - x_min)/(num_points[i]-1)
	x = np.arange(x_min,x_max + dx, dx)
	y = np.zeros(x.size)

	for j in range(x.size):
		y[j] = f(x[j])

	ft_y = np.fft.fft(y, n= 2*num_points[i], norm= 'ortho')

	k = np.fft.fftfreq(2*num_points[i] , d= dx)
	k = 2*np.pi*k 
	                                # true k values
	factor=np.exp(-1j* k* x_min)   # factor for taking account of x_min != 0
	ex_ft_y = factor * ft_y        # exact Fourier transform
	
	plt.plot(k,ex_ft_y)  # plotting the Fourier transform

plt.title('Plot of Fourier transform')
plt.grid()
plt.xlabel('k')
plt.ylabel('DFT')
plt.legend(['for num_points= 50','for num_points= 200','for num_points= 400'])
plt.xlim(-60,60)
plt.show()	

# Plotting the function:
plt.plot(x,y,'blue')
plt.title('Plot of the Function')
plt.grid()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()