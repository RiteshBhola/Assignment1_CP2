import numpy as np
import scipy as sp

TOL=0.01
W=1.25
a=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
b=np.array([1,2,3,4,5])
x0=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])
x1=np.zeros(5)
n=0
while True:
	for i in range(0,5):
		x1[i]=(W*b[i])/a[i][i] + (1-W)*x1[i]
		for j in range(0,5):
			if(i==j):
				continue
			x1[i]+=(-a[i][j]*x1[j]*W)/a[i][i]
	n=n+1
	if(np.sqrt(np.dot(x1-x0,x1-x0))<TOL):
		break

	

print("The Solution vector is")
print(x1)
print("and Relaxation method took",n," iterations")
