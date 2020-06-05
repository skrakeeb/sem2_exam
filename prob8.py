#coded by rakeeb

import numpy as np 
import matplotlib.pyplot as plt 
from scipy.integrate import solve_bvp

# given boundary conditions:
x_min = 0 
x_max = 1
y_in = 0
y_fi = 2

def f(x,y):
    return np.array([y[1], 4*(y[0]-x)])

def bc(ya, yb):
    return np.array([ya[0] - y_in , yb[0] - y_fi ])

x = np.linspace(x_min , x_max , 10)
y = np.zeros((2 , x.size)) + 1

soln = solve_bvp(f, bc, x, y)

x_sol = np.linspace(x_min , x_max , 100)
y_sol = soln.sol(x_sol)[0]   # solution by solve_bvp function

def y_exact(x):  # exact solution as given
	e = np.e
	ex2 = np.exp(2*x) 
	return( e**2 * (ex2 - (1/ex2) )/(e**4 - 1) + x )

y_exact_val = np.zeros(x_sol.size) 
for i in range(x_sol.size):   # exact values at the specified points
	y_exact_val[i] = y_exact(x_sol[i])

abs_err = abs( y_exact_val - y_sol) #absolute error
rel_err = np.zeros(abs_err.size)

print('Percentage relatve Errors:\n')
for i in range(abs_err.size):  # relative errors in each points
	if y_exact_val[i] != 0 :
		rel_err[i] = abs_err[i]/y_exact_val[i]
	print(rel_err[i] * 100)	


plt.plot(x_sol, y_sol, 'black', label = "Numerical solution")
plt.plot(x_sol,y_exact_val,'red', label='Exact solution')
plt.title('Plot of the solution')
plt.xlabel("x", fontsize=12)
plt.ylabel("y(x)", fontsize=12)
plt.legend()
plt.show()
