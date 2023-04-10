class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
    def add(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=newnode
    def display(self):
        if self.head is None:
            print('empty linked list')
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref
    def afterinsert(self,data1,pos):
        if self.head is None:
            print('no linked list found')
        else:
            n=self.head
            while n is not None:
                if n.data == pos:
                    break
                n=n.ref
            if n is None:
                print('item is not present in the list')
            else:
                newnode=Node(data1)
                newnode.ref=n.ref
                n.ref=newnode
                    

ll1=linkedlist()
ll1.add(10)
ll1.add(20)
ll1.add(30)
ll1.add(40)
ll1.add(50)
ll1.display()
ll1.afterinsert(35,30)
print('new linked list')
ll1.display()