class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class arrtoll:
    def __init__(self):
        self.head=None
    
    def arraytoll(self,arr):
        if len(arr)<1:
            print('array is empty')
        elif len(arr)==1:
            newnode=Node(arr[0])
            self.head=newnode
        else:
            newnode=Node(arr[0])
            self.head=newnode
            for i in range(1,len(arr)):
                new_node=Node(arr[i])
                newnode.ref=new_node
                newnode=new_node

    def display(self):
        if self.head is None:
            print('linked list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

array=[10,8,9,3,7,64,75]
e=arrtoll()
e.arraytoll(array)
e.display()