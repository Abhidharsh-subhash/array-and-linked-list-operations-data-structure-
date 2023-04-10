

import math

arr1=[10,20,30,40,50,60,70,80,90]

def binary(array,value):
    start=0
    end=len(array)-1
    middle=math.floor((start+end)/2)
    while array[middle] != value and start<=end:
        if value>array[middle]:
            start=middle+1
        else:
            end=middle-1
        middle=math.floor((start+end)/2)
    if array[middle]==value:
        return middle
    else:
        return -1

print(binary(arr1,70))