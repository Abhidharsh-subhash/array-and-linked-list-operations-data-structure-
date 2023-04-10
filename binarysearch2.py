import math

array=[100,90,80,70,60,50,40,30,20,10]
array.sort()

def find(arr,value):
    start=0
    end=len(arr)-1
    middle=math.floor((start+end)/2)
    while arr[middle]!=value and start<=end:
        if arr[middle]<value:
            start=middle+1
        else:
            end=middle-1
        middle=math.floor((start+end)/2)
    if arr[middle]==value:
        return middle
    else:
        return -1
    
print(find(array,20))

