#delete a specific element from an array

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

    def delete(self, data):
        if self.head is None:
            print('empty linked list')
        else:
            # Handle the case where the head node needs to be deleted
            while self.head is not None and self.head.data == data:
                self.head = self.head.ref

            # Traverse the linked list and delete nodes with matching data
            n = self.head
            while n is not None and n.ref is not None:
                if n.ref.data == data:
                    n.ref = n.ref.ref
                else:
                    n = n.ref

            # Handle the case where the last node needs to be deleted
            if self.head is not None and self.head.data == data and self.head.ref is None:
                self.head = None


l=linkedlist()
l.create(45)
l.create(45)
l.create(45)
l.create(4)
l.create(5)
l.create(46)
l.create(45)
l.create(90)
l.create(45)
l.create(0)
l.create(45)
l.create(45)
l.create(45)
l.create(45)
l.delete(45)
l.display()