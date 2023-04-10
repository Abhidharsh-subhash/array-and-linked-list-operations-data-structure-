#add value at the beginning of the linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkelist:
    def __init__(self):
        self.head=None

    def insert(self,data):
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
    def begin(self,value):
        if self.head is None:
            print('empty linked list')
        else:
            node=Node(value)
            node.ref=self.head
            self.head =node

l=linkelist()
l.insert(10)
l.insert(99)
l.insert(26)
l.display()
print('new')
l.begin(86)
l.display()
