from array import *

arr=[[1,10,9,8],[4,8,29,28],[10,37,29,47]]
print(arr)
print(len(arr)) #no.of rows in the array
print(len(arr[0])) #no.of columns in the array of row 1
for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j],end=' ')
    print()