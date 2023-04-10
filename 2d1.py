import numpy as np 

arr1=np.array([[11,15,10,6],[10,4,11,5],[12,17,12,8],[15,18,14,19]])

for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        print(arr1[i][j],end=" ")
    print()