import numpy as np

TOL=0.0001
a=np.array([[5,-2],[-2,8]])
e_val,e_vec=np.linalg.eigh(a)

print(f"Eigen values are {e_val[0]} and {e_val[1]} and corresponding eigenvectors are {e_vec[:,0]} and {e_vec[:,1]}\nobtained using numpy.linalg.eigh function")
while True:
	q, r = np.linalg.qr(a)
	a=np.matmul(r,q)
	if(np.abs(a[0][1])<TOL):
		break
	
print(f"Eigenvalues from QR algorithm are {a[0][0]:0.4f} and {a[1][1]:0.4f} with tolerance {TOL:0.4f}")

