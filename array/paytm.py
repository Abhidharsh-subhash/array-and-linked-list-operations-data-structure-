def find(array):
    n=len(array)+1
    s=(n*(n+1))/2
    sum=0
    for i in array:
        sum+=i
    return int(s-sum)

arr=[3,1,2,6,4]
print(find(arr))