# coded by: rakeeb

import numpy as np 
import matplotlib.pyplot as plt

#	As the eqautions are stiff we solve them by applying implicit euler method
# 	we solve for (n+1)th iteration of y1 and y2 in terms of n-th iteraion and we
#	define the two functions as the right hand side of the solved part i.e 
#	y1[n+1] = f1(y1[n],y2[n],x[n],h) and
#	y2[n+1] = f2(y1[n],y2[n],x[n],h) and solve them.

def f1(y1, y2, x, h):
	return((y1 + h*(66*y2 + 2*x/3.0 + 2/3.0))/(1-32*h)) 

def f2(y1, y2, x, h):
	return((y2 - h*(66*y1 + x/3.0 + 1/3.0))/(1+133*h))	

x = np.arange(0,0.501,0.001)
h = x[1]-x[0] #the step size

y1 = np.zeros(x.size)	
y2 = np.zeros(x.size)
# given initial values:
y1[0] = 1/3.0  
y2[0] = 1/3.0

for i in range(x.size-1):  # we keep updating our solution by implicit method
	y1[i+1] = f1(y1[i],y2[i],x[i],h)
	y2[i+1] = f2(y1[i],y2[i],x[i],h)

plt.plot(x,y1, 'red',label='Plot of y1')
plt.plot(x,y2, 'black',label='Plot of y2')
plt.title('Plot of the solutions')
plt.xlabel("x", fontsize=12)
plt.ylabel("y(x)", fontsize=12)
plt.legend()
plt.grid(color='b', linestyle='--', linewidth=0.5)
plt.show()

#	As the equations are stiff they diverges very much even for small values of h, so 
#	if we can prohibit its diverging by changing the Euler method a little bit and 
#   implicitly solving them , then the solutions are determined in such a fashion that 
#	they just feedback to themselves, then the solutons converge even for somewhat
#	'large' values of h. We just applied that technique. 