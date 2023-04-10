def sum(array,value):
    result=[]
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]+array[j] == value:
                result.append(i)
                result.append(j)
    return result

arr1=[3,2,4]
print(sum(arr1,7))