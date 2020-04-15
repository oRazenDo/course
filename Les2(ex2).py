import numpy as np
x=np.array(range(100))
print('1: ',np.sum(x))
c=int(input())
x2=np.array(range(0,c))
print('2: ',np.sum(x2))
x3=np.random.randint(0,1000,100)
print('3: ', x3.mean())
