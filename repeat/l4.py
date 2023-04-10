# delete value from the beginning of the linked list

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

    def delstart(self):
        if self.head is None:
            print('empty linked list')
        else:
            self.head=self.head.ref

l=linkedlist()
l.insert(26)
l.insert(95)
l.insert(100)
l.display()
print('new')
l.delstart()
l.display()
