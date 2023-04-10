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
            self.head = newnode
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

p=linkedlist()
p.addnode(5)
p.addnode(0)
p.addnode(2)
p.display()