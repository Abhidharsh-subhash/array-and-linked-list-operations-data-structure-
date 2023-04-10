from array import *

nums = [0,0,1,1,1,2,2,3,3,4]

def dup(array):
    result=[]
    for i in array:
        if i not in result:
            result.append(i)
    print(len(result))
    return result

print(dup(nums))