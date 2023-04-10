def delindex(array,index):
    result=[]
    for i in range(len(array)):
        if i != index:
            result.append(array[i])
    return result

arr=[1,2,3,4,5,6,7]
print(delindex(arr,3))

