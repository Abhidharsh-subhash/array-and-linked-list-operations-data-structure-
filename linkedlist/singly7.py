class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkedlist():
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
    def deletetell(self,tell):
        if self.head is None:
            print('linked list is empty')
            return #it will come out of the method
        if self.head.data == tell:
            self.head=self.head.ref
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data == tell: 
                    break
                n=n.ref
            if n.ref is None:
                print('no such element found')
            else:
                n.ref=n.ref.ref

l=linkedlist()
l.addnode(0)
l.addnode(5)
l.addnode(4)
l.addnode(2)
l.display()
print('after deleting the specified node')
l.deletetell(5)
l.display()

