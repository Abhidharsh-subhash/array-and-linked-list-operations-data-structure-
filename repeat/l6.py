#delete a node with of particular value

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkedlist:
    def __init__(self):
        self.head=None

    def create(self,data):
        node=Node(data)
        if self.head is None:
            self.head = node
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

    def delete(self,data):
        if self.head is None:
            print('empty linked list')
        else:
            n=self.head
            while n.ref.data == data:
                n.ref=n.ref.ref
            n=n.ref

l=linkedlist()
l.create(19)
l.create(18)
l.create(17)
l.create(12)
l.display()
print('new')
l.delete(18)
l.display()