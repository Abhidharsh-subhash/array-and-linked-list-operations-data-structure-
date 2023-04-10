from array import *


class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None 

class linkedlist:
    def __init__(self):
        self.head=None

    def arrtoll(self,array):
        if len(array)<1:
            print('no array elements')
        if len(array)==1:
            newnode=Node(array[0])
            self.head=newnode
        else:
            newnode=Node(array[0])
            self.head=newnode
            for i in range(1,len(array)):
                new_node=Node(array[i])
                newnode.ref=new_node
                newnode=new_node


    def display(self):
        if self.head is None:
            print('linked list is empty')
        else:
            n=self.head
            if n.ref is not None:
                print(n.data)
                n=n.ref

arr1=[11,12,13,14,14,15,16]

l=linkedlist()
l.arrtoll(arr1)
l.display()






