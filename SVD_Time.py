import numpy as np
import time

def R_SVD(A,m,n,TOL):
	"""
	Without the loss of generality  we can take m>=n. If m<n then supply Tranpose of input matrix.
	as A=U.S.Trans(V)
	A'=U'.S'.Trans(V)'=Trans(A)=V.Trans(S).Trans(U)
	This program works for any mXn real matrix
	"""
	
	#A=np.array([0,1,1,0,1,0,1,1,0,0,1,0,1,0,1]).reshape(m,n)
	
	#A=U(mxm)S(mxn)V^T(nxn)
	S=np.zeros([m,n])
	
	N=np.transpose(A)@A #nxn matrix
	M=A@np.transpose(A)#mxm matrix

	nevl,nevec = np.linalg.eigh(N)
	mevl,mevec = np.linalg.eigh(M)
	
	mevl=np.flip(mevl)
	nevl=np.flip(nevl)


	for i in range(0,n):
		if(np.abs(nevl[i])>TOL):
			S[i][i]=np.sqrt(nevl[i])
				
	
	V=np.zeros([n,n])
	U=np.zeros([n,n])
	for i in range(0,n):
	 V[:,i]=nevec[:,n-i-1]



	#U=A@V/np.sqrt(nevl)
	U=A@V
	for i in range(0,n):
		if(np.abs(nevl[i])>TOL):
			U[:,i]=U[:,i]/np.sqrt(nevl[i])
		else:
			U[:,i]=U[:,i]/np.sqrt(np.dot(U[:,i],U[:,i]))

	vec=mevec[:,np.arange(0,m-n)]
	U=np.column_stack((U,vec))

		





"""
Timing First Using R_SVD
"""
m=5
n=3
TOL=1e-7
A=np.array([0,1,1,0,1,0,1,1,0,0,1,0,1,0,1]).reshape(m,n)


t1=time.time()
for i in range(0,10000):
 R_SVD(A,m,n,TOL)
t2=time.time()
print("TIme Taken by my function",(t2-t1)/10000,"seconds")



#   by inbuilt
t1=time.time()
for i in range(0,10000):
 u, s, vh = np.linalg.svd(A, full_matrices=True)
t2=time.time()
print("TIme Taken by np.linalg.svd",(t2-t1)/10000,"seconds")
smat = np.zeros((m, n), dtype=complex)

smat[:n, :n] = np.diag(s)
	
#print(u)





