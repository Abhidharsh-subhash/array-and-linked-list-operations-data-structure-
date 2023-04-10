#insert a node a after the given value

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

    def dispaly(self):
        if self.head is None:
            print('empty linked list')
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

    def afins(self,data,value):
        if self.head is None:
            print('empty linked list')
        else:
            node=Node(value)
            n=self.head 
            while n.data != data:
                n=n.ref
            node.ref=n.ref
            n.ref=node

l=linkedlist()
l.create(18)
l.create(17)
l.create(89)
l.create(90)
l.dispaly()
print('new')
l.afins(89,76)
l.dispaly()