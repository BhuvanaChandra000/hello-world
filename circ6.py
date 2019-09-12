import numpy as np
import math
import matplotlib.pyplot as plt
from coeffs import *

#if using termux
import subprocess
import shlex
P=np.array([-2,4])
Q=np.array([0,2])
K=np.array([-4,2])
L=np.array([0,1])
M=np.array([1,-1])
A=np.array([0,10/3])
B=np.array([-5,0])
S=np.vstack((M,L))
O=np.matmul(np.linalg.inv(S),K)
print(O)
d=np.linalg.norm(P-Q)
print(d)
r=np.linalg.norm(O-Q)
print(r)
x_AB=line_gen(A,B)
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(A[0],A[1],'go')
plt.text(A[0]*(1+0.1),A[1]*(1-0.1),'A')
plt.plot(B[0],B[1],'go')
plt.text(B[0]*(1-0.2),B[1]*(1),'B')
x_PO=line_gen(P,O)
plt.plot(x_PO[0,:],x_PO[1,:],label='$PO$')
plt.plot(P[0],P[1],'go')
plt.text(P[0]*(1+0.02),P[1]*(1-0.1),'P')
plt.plot(O[0],O[1],'go')
plt.text(O[0]*(1-0.03),O[1]*(1),'O')

len = 100
theta = np.linspace(0,2*np.pi,len)
x_circ = np.zeros((2,len))
x_circ[0,:] = r*np.cos(theta)
x_circ[1,:] = r*np.sin(theta)
x_circ = (x_circ.T + O).T
plt.plot(x_circ[0,:],x_circ[1,:],label='$circle$')
plt.axis('equal')
plt.grid()
plt.show()
