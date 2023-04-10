array=[1,2,3,4,5,4,1,7,9,4,6]

def dup(arr):
    result=[]
    for i in arr:
        if i not in result:
            result.append(i)
    return result

print(array)
print(dup(array))