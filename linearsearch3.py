arr=[12,9,50,30,29,17,28,14,5]


def find(array,value):
    for i in range(len(array)):
        if array[i]==value:
            return i
    return -1
print(find(arr,12))