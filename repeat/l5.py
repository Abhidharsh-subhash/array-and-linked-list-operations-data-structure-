#delete node from the end of the linked list

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

    def delend(self):
        if self.head is None:
            print('empty linked list')
        else:
            n=self.head
            while n.ref.ref is not None:
                n=n.ref
            n.ref=None

l=linkedlist()
l.insert(27)
l.insert(11)
l.insert(17)
l.display()
print('new')
l.delend()
l.display()