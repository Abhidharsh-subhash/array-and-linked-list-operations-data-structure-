arr=[1,2,3,5,7,5,5,3]

def dup(array):
    result=[]
    for i in array:
        if i not in result:
            result.append(i)
    return result

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkedlist:
    def __init__(self):
        self.head=None

    def insert(self,data):
        node=Node(data)
        if self.head is None:
            self.head = node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=node

    def arrtol(self,array):
        if len(array) < 1:
            print('array is empty')
        elif len(array) == 1:
            node=Node(array[0])
            self.head=node
        else:
            node=Node(array[0])
            self.head=node
            
            for i in range(1,len(array)):
                newnode=Node(array[i])
                node.ref=newnode
                node=newnode

    def display(self):
        if self.head is None:
            print('empty linked list')
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref


l=linkedlist()
l.arrtol(dup(arr))
l.display()

