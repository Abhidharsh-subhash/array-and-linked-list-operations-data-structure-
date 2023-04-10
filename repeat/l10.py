#convert a linked list into an array

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

    def ltoarr(self):
        if self.head is None:
            print('empty linked list')
        else:
            result=[]
            n=self.head
            while n is not None:
                result.append(n.data)
                n=n.ref
            return result

l=linkedlist()
l.insert(10)
l.insert(23)
l.insert(45)
l.display()
print('new')
print(l.ltoarr())