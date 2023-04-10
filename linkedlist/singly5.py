class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
    
class linkedlist:
    def __init__(self):
        self.head=None
    def add(self,data):
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
            print('Linked list is empty')
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

    def deletefirst(self):
        if self.head is None:
            print('linked list is empty')
        else:
            self.head=self.head.ref

l=linkedlist()
l.add(3)
l.add(5)
l.add(6)
l.display()
print('after deleting first node')
l.deletefirst()
l.display()