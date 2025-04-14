from LinkedList import Node, LinkedList

def hasCycle(list:LinkedList):
    slow=list.head
    fast=list.head

    while(fast is not None and fast.next is not None):
        fast=fast.next.next
        slow=slow.next

        if (slow==fast):
            return True
    return False


def main():

    ## Creating a cycled linked list
    list=LinkedList()
    for _ in range(5):
        list.appendEnd(_)
    
    list.head.next.next.next.next.next=list.head

    ## Commenting out list printing because it'll run infinetely
    #list.printList()

    cycle = hasCycle(list)
    print(cycle)
if __name__== "__main__":
    main()