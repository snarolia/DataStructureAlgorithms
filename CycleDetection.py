from LinkedList import Node, LinkedList

def hasCycle(list:LinkedList):
    slow=list.head
    fast=list.head

    while(fast is not None and fast.next is not None):
        print(fast.data)
        fast=fast.next.next
        slow=slow.next

        if (slow==fast):
            return True
        else:
            return False


def main():

    ## Creating a cycled linked list
    list=LinkedList()
    tail=Node()
    for _ in range(10):
        list.appendEnd(_)
        
    tail=list.head
    

if __name__== "__main__":
    main()