# convert an array into linked list

class Node:
     def __init__(self,data):
          self.data=data
          self.ref=None

class linkedlist:
    def __init__(self):
        self.head=None

    def display(self):
        if self.head is None:
            print('empty linked list')
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

    def arrtol(self,array):
        if len(array) < 1:
            print('array is empty')
        elif len(array) == 1:
            node=Node(array[0])
            self.head = node
        else:
            node=Node(array[0])
            self.head=node
            for i in range(1,len(array)):
                newnode=Node(array[i])
                node.ref=newnode
                node=newnode



arr=[1,3,7,2,4,8,0,6]
l=linkedlist()
l.arrtol(arr)
l.display()