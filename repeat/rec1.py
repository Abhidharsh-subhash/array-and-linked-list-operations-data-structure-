# binary search using recursion

def binrec(array,target,start,end):
    if start > end:
        return -1
    
    mid=(start+end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binrec(array,target,start,mid-1)
    else:
        return binrec(array,target,mid+1,end)
    
arr=[1,2,3,4,5,6,7,8,9]
n=len(arr)
print(binrec(arr,9,0,n))