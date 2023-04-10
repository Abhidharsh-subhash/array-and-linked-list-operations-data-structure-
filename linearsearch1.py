arr1=[10,20,30,40,50,60,70,80,90]

def linear(array,value):
    for i in range(len(array)):
        if array[i]==value:
            return i
    return -1


print(linear(arr1,600))