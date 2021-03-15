import numpy as np 

a = [[1,2],[3,4],[5,6]]

b = [j for i in a for j in i]
c = np.array(a).flatten().tolist()
print(b)
print(c)