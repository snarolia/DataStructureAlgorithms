import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

"""
Doubly LinkedList

node: data, next, prev

AppendEnd:
    - lastNode.next-->Newnode
    - NewNode.prev --> lastNode
AppendStart:
    - NewNode.next --> self.head
    - NewNode.prev == None
    - self.head.prev ==> NewNode
"""

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None
        #logging.INFO("New node object Created")

class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.first=None
        self.last=None
    
    def appendEnd(self, data):
        tempNode=Node(data)
        if self.head is None:
            self.head=tempNode
            self.first=tempNode
            self.last=tempNode
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=tempNode
            tempNode.prev=current
            self.last=tempNode

    def appendStart(self, data):
        tempNode=Node(data)
        if self.head is None:
            self.head=tempNode
            self.first=tempNode
            self.last=tempNode
            return
        else:
            tempNode.next=self.head
            self.head.prev=tempNode
            self.head=tempNode
            self.first=tempNode
    
    def appendAfter(self,key ,data):
        tempNode=Node(data)
        if self.head is None:
            self.head=tempNode
            return
        else:
            current=self.head
            while current:
                if current.data==key:
                    tempNode.next=current.next
                    tempNode.prev=current
                    current.next=tempNode
                    if current.next is None:
                        self.last=tempNode
                    break
                else:
                    current=current.next
    
    def printListAsc(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
        print("None")

    def getFirstLast(self):
        first, last = self.first, self.last
        return first, last



dll=DoublyLinkedList()
for _ in range(8):
    dll.appendEnd(_)

dll.appendStart("appended at beginning")
dll.appendAfter(3,"Appended after 3")

dll.printListAsc()
first,last=dll.getFirstLast()
print(f"The first Element is : {first.data}")
print(f"The last Element is : {last.data}")