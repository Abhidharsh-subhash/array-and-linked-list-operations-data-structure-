arr1=[1,2,3,4,5,6,7]
arr12=[11,12,13,14,15,16,17]

def sum(array1,array2):
    result=[]
    for i in range(len(array1)):
        for j in range(len(array2)):
            if i==j:
                s=array1[i]+array2[j]
                result.append(s)
    return result

print(sum(arr1,arr12))