import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

"""

Step 1 : Node class creation for node object
Step 2 : LinkedList Class
Step 3:
    -Append at the end
    -Append at the beginning
    -Append in specified position

    Append at the end
    -----------------
    1. check if list not empty -> else make head=NewNode
    2. Traverse to end of list
    3. LastNode.next --> CurrentNode

    Append at the beginning
    -----------------------
    1. If empty LL :: head=CurrentNode
    2. If not empty :: CurrentNode.next --> Head

"""

class Node:
    def __init__(self, data):
        self.data = data
        logging.info(f"Node created with value :  {data}")
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None # Assuming list is empty
    
    def appendEnd(self, data):
        tempNode = Node(data)

        if self.head==None:
            self.head=tempNode
            return
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next=tempNode
    
    def appendStart(self, data):
        tempNode = Node(data)
        if self.head==None:
            self.head=tempNode
            return
        else:
            current_node=self.head
            self.head=tempNode
            self.head.next=current_node
        
    def appendAfter(self, key, data):
        if self.head==None:
            self.head=Node(data)
        current=self.head
        while current:
            if current.data==key:
                tempNode=Node(data)
                tempNode.next=current.next
                current.next=tempNode
                break
            else:
                current=current.next
        
                
        
    def printList(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
        print("None")

l1 = LinkedList()
for _ in range(5):
    l1.appendEnd(_)
l1.appendStart("Appended at Beignning")
l1.appendAfter(2,"Appended in between")
l1.printList()