#coded by: rakeeb

import numpy as np 

a1 = np.array([[2,1],[1,0],[0,1]])
a2 = np.array([[1,1,0],[1,0,1],[0,1,1]])

U1,S1,V1 = np.linalg.svd(a1)
U2,S2,V2 = np.linalg.svd(a2)

a1_trans = np.transpose(a1)  #taking transpose of a1
a2_trans = np.transpose(a2)  #taking transpose of a2

sq_mat1= np.matmul(a1_trans,a1)  #making the square matrix A(transpose)*A
sq_mat2= np.matmul(a2_trans,a2) 

eig_v1,eig_vec1= np.linalg.eig(sq_mat1)# determining eigen values and eigen vectors
eig_v2,eig_vec2= np.linalg.eig(sq_mat2)

evaluated_s1= np.sqrt(eig_v1) # taking the square root of the eigen values , these are the singular values
evaluated_s2= np.sqrt(eig_v2)

print('evaluated singular values of a1: ',evaluated_s1,'\n')
print('evaluated singular values of a2: ',evaluated_s2,'\n')

print('Singular value decomposition by numpy function for a1: \nU= ',U1,'\nS= ',S1,'\nV= ',V1,'\n')
print('Singular value decomposition by numpy function for a2: \nU= ',U2,'\nS= ',S2,'\nV= ',V2,'\n')
