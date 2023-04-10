

def twoSum(array,target):
        result=[]
        for i in range(len(array)):
            for j in range(i,len(array)):
                if array[i]+array[j] == target:
                    result.append(i)
                    result.append(j)

array=[12,17,22,37,58]
print(twoSum(array,49))