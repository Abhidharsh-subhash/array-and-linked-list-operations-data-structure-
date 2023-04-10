# creating the base for node
class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

#to create a linked list
class linkedlist:
    def __init__(self):
        self.head=None
    #method to traverse the linked list
    def printll(self):
        if self.head is None:
            print('linked list is empty')
        else:
            n=self.head 
            while n is not None:
                print(n.data)
                n=n.ref

    #method for adding new value to the linked list
    def addnode(self,data):
        newnode=Node(data)
        if  self.head is None:
            self.head=newnode
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=newnode

    #method to add the value at the beginning of the linked list
    def addbegin(self,data):
        newnode=Node(data)
        newnode.ref=self.head #newnode's link is set as value in the head
        self.head=newnode

ll1=linkedlist()
ll1.addnode(4)
ll1.addnode(10)
ll1.addnode(28)
ll1.printll()
print('adding value at the beginning of the linked list')
ll1.addbegin(20)
ll1.printll()