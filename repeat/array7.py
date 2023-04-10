from array import * 

def delete(array,value):
    result=[]
    for i in array:
        if i != value:
            result.append(i)
    print(len(result))
    return result

arr=[3,2,2,3]
print(delete(arr,3))
