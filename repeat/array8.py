import array

def find(arra,target):
    for i in range(len(arra)):
        if arra[i] == target:
            return i
    arra.append(target)
    arr1=array.array('i',sorted(arra))
    for i in range(len(arr1)):
        if arr1[i] == target:
            return i

arr=array.array('i',[1,3,5,6])
print(find(arr,3))
        
        
