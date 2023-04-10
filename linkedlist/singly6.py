class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkedlist:
    def __init__(self):
        self.head=None
    
    def addnode(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=newnode
    
    def display(self):
        if self.head is None:
            print('linked list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    
    def deleteend(self):
        if self.head is None:
            print('empty linked list')
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None


l=linkedlist()
l.addnode(4)
l.addnode(7)
l.addnode(9)
l.display()
print('after deleting the end node')
l.deleteend()
l.display()