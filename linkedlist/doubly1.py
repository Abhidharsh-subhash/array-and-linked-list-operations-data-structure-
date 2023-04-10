class Node:
    def __init__(self,data):
        self.data=data
        self.nref=None
        self.pref=None

class doublylinkedlist:
    def __init__(self):
        self.head=None

    def insert(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            if n.nref is not None:
                n=n.nref
            n.nref=newnode
            newnode.pref=n

    def display(self):
        if self.head is not None:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.nref

