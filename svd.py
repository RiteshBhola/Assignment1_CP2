import numpy as np
m=4
n=3
"""
Without the loss of generality  we can take m>=n. If m<n then supply Tranpose of input matrix.
as A=U.S.Trans(V)
A'=U'.S'.Trans(V)'=Trans(A)=V.Trans(S).Trans(U)
This program works for any mXn real matrix
"""
TOL=1e-7
#A=np.array([0,1,1,0,1,0,1,1,0,0,1,0,1,0,1]).reshape(m,n)
A=np.array([1,0,1,1,0,1,0,0,0,1,1,0]).reshape(m,n)
#A=U(mxm)S(mxn)V^T(nxn)
S=np.zeros([m,n])
print("Input matrix A is\n",A)
N=np.transpose(A)@A #nxn matrix
M=A@np.transpose(A)#mxm matrix

nevl,nevec = np.linalg.eigh(N)
mevl,mevec = np.linalg.eigh(M)
print(mevl)
#print(nevl)
mevl=np.flip(mevl)
nevl=np.flip(nevl)


for i in range(0,n):
	if(np.abs(nevl[i])>TOL):
		S[i][i]=np.sqrt(nevl[i])
			
print("The S matrix:\n",S)
V=np.zeros([n,n])
U=np.zeros([n,n])
for i in range(0,n):
 V[:,i]=nevec[:,n-i-1]

print(A)

#U=A@V/np.sqrt(nevl)
U=A@V
for i in range(0,n):
	if(np.abs(nevl[i])>TOL):
		U[:,i]=U[:,i]/np.sqrt(nevl[i])
	else:
		U[:,i]=U[:,i]/np.sqrt(np.dot(U[:,i],U[:,i]))

vec=mevec[:,np.arange(0,m-n)]
U=np.column_stack((U,vec))

	
print("V transpose is\n",np.transpose(V))
print("U is \n",U)
print("U.S.Trans(V)\n",U@S@np.transpose(V))

######################################
#   by inbuilt
u, s, vh = np.linalg.svd(A, full_matrices=True)


smat = np.zeros((m, n), dtype=complex)

smat[:n, :n] = np.diag(s)
	

#print(smat)
print(u)
#print(vh)
