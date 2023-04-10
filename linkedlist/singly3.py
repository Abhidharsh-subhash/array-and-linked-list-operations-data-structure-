class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkedlist:
    def __init__(self):
        self.head=None
    def addnew(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=newnode
    def printll(self):
        if self.head is None:
            print('empty linked list')
        else:
            n=self.head
            while n is not None:
                print(n.data,'-->',end='')
                n=n.ref
    def addend(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=newnode

ll1=linkedlist()
ll1.addnew(5)
ll1.addnew(10)
ll1.printll()
print('new value at the end of the linked list')
ll1.addend(30)
ll1.printll()