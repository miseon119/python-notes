import numpy as np

a = np.array([[1,2],[3,4]])

# solution 1: multi-dementional to 1D  (not copy)
b=a.ravel()   

# solution 2: multi-dementional to 1D   (not copy)
c=a.reshape(-1)

# solution 3: multi-dementional to 1D   (copy a)
d=a.flatten()
