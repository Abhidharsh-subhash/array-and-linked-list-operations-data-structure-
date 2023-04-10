#add value at the end of the linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkeslit:
    def __init__(self):
        self.head=None

    def insert(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=node

    def display(self):
        if self.head is None:
            print('empty linked list')
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

    def end(self,data):
        if self.head is None:
            print('empty linked list')
        else:
            node=Node(data)
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=node

l=linkeslit()
l.insert(29)
l.insert(38)
l.insert(28)
l.display()
print('new')
l.end(22)
l.display()
