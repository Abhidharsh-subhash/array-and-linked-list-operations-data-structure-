#insert a node a before the given value

class Node:
     def __init__(self,data):
          self.data=data
          self.ref=None

class linkedlist:
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

    def insbef(self,data,value):
        if self.head is None:
            print('empty linked list')
        else:
            node=Node(value)
            n=self.head
            while n.ref.data != data:
                n=n.ref
            node.ref=n.ref
            n.ref=node

l=linkedlist()
l.insert(0)
l.insert(79)
l.insert(234)
l.insert(23)
l.insert(34)
l.display()
print('new')
l.insbef(23,22)
l.display()

    