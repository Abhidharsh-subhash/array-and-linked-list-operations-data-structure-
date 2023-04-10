class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkedlist():
    def __init__(self):
        self.head=None
    def create(self,data):
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
            print('empty linked list')
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def addbeg(self,value):
        if self.head is None:
            print('linked list is empty')
        else:
            newnode=Node(value)
            newnode.ref=self.head
            self.head =newnode
    def addend(self,value):
        if self.head is None:
            print('empty linked list')
        else:
            newnode=Node(value)
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=newnode
    def delnode(self,value):
        if self.head is None:
            print('empty linkedlist')
        elif self.head.data == value:
            self.head = self.head.ref 
        else:
            n=self.head
            while n.ref is not None:
                if n.ref.data == value:
                    n.ref=n.ref.ref
                n=n.ref
    def insafter(self,value,pos):
        if self.head is None:
            print('empty linked list')
        else:
            newnode=Node(value)
            n=self.head
            while n is not None:
                if n.data == pos:
                    newnode.ref=n.ref
                    n.ref=newnode
                n=n.ref
    def inbefore(self,value,pos):
        if self.head is None:
            print('empty linked list')
        elif self.head.data == pos:
            newnode=Node(value)
            newnode.ref=self.head
            self.head=newnode
        else:
            newnode=Node(value)
            n=self.head
            while n.ref is not None:
                if n.ref.data == pos:
                    newnode.ref=n.ref
                    n.ref=newnode
                n=n.ref



l=linkedlist()
l.create(4)
l.create(6)
l.create(10)
l.create(1)
l.display()
l.inbefore(17,6)
print('new')
l.display()
        