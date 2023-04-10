arr=[18,93,75,12,36,29,30]

def search(array,value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1
    
print(search(arr,90))