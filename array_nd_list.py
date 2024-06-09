from array import array  # for Array

import numpy as np  # for Lists

# Array

a1 = array('i', [23, 56, 106])
print(type(a1))
print(a1)

for x in a1:
    print(x)  # array finished
for i in range(3):
    print(a1[i], end=' ')  # array with for loop
while (i < len(a1)):
    print(a1[i])
    i += 1  # array with whilw loop
#  Array applying mehtods such as append,count,insert,remove,index,etc
a1.append(27)
print(a1)
print(a1.count(56))
print(a1.pop())  # delete the last the value when given no index
print(a1.pop(2))  # delete the value of given index
print(a1)  # in remove we provide value, in pop we provide index

# List

a = np.array([4, 5, 6])  # 1-D list
print(a)

b = np.array([[4, 5, 6], [7, 8, 9]])  # 2-D list
print(b)

c = np.array([[1, 2, 3], [10, 20]])
print(c)
