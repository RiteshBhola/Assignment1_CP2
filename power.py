import numpy as np

TOL=0.01
a=np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])
e_val,e_vec=np.linalg.eigh(a)

print(f"Eigen values are {e_val[0]},\n{e_val[1]} and\n{e_val[2]}")

maxe = e_val.max()
print("Dominant Eigenvalue",maxe)
x=np.array([1,0,0])
#power method
counter=0
while True:
		d=np.dot(x,a@x)/np.dot(x,x)
		x=a@x/np.dot(a@x,a@x)
		counter+=1
		if(np.abs((d-maxe)/d)<TOL):
			break
	
print(f"Dominant eigenvalue from power method is {d:0.4f} within 1 percent error and power method took {counter} iterations starting with vector [1,0,0]")

