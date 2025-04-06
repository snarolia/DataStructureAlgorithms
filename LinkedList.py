class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None ## Assuming list is empty
    
    def appendEnd(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node
    
    def printList(self):
        current = self.head
        while current:
            print(current.data)
            current=current.next
        print("None")

myList = LinkedList()
myList.append(10)
myList.append(20)

myList.printList()