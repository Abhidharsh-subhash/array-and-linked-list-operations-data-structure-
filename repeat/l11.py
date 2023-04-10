class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,data):
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

    def deldup(self):
        if self.head is None:
            print('empty linked list')
        else:
            seen=set()
            n=self.head
            previous=None
            while n is not None:
                if n.data in seen:
                    previous.ref=n.ref
                else:
                    seen.add(n.data)
                    previous=n
                n=n.ref            

l=linkedlist()
l.insert(17)
l.insert(15)
l.insert(23)
l.insert(45)
l.insert(15)
l.dispaly()
print('new')
l.deldup()
l.dispaly()