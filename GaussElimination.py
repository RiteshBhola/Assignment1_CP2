import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

a=np.array([[1,0.67,0.33],[0.45,1,0.55],[0.67,0.33,1]])
b=np.array([2,2,2])
x=np.linalg.solve(a,b)
print(x)
