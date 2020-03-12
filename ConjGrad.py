import numpy as np
import scipy as sp

TOL=0.01
a=np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
b=np.array([1,2,3,4,5])
x0=np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])
x=np.zeros(5)
n=1
v=b-a@x
r=b-a@x
alpha=np.dot(v,v)
while True:
	if(np.dot(v,v)<TOL):
	 break
	 
	u=a@v
	t=alpha/np.dot(v,u)
	x = x + t*v
	r=r-t*u
	beta=np.dot(r,r)
	
	if(np.sqrt(beta)<TOL):
		break
	
	s=beta/alpha
	v=r+s*v
	alpha=beta
	n+=1
		
print("The Solution vector is")
print(x)
print("and Conjugate Gradient method took",n," iterations")
