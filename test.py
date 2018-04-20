import numpy as np

a = [i for i in range(12)]
print(a)
a = np.asarray(a)
print(a)
a = np.reshape(a, (-1,1))
print(a)
a = np.reshape(a,(-1,4))
print(a)
