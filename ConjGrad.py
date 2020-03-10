import numpy as np
import scipy as sp

TOL=0.01
a=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
b=np.array([1,2,3,4,5])
x0=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])
x=np.zeros(5)
n=0
while True:
	v=b-a@x
	t=np.dot(v,b-a@x)/np.dot(v,a@v)
	x = x + t*v
	n+=1
	if(np.sqrt(np.dot(x-x0,x-x0))<TOL):
		break
		
print("The Solution vector is")
print(x)
print("and Conjugate Gradient method took",n," iterations")
