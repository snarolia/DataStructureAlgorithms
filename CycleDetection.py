from LinkedList import Node, LinkedList


## The functions returns boolean for cycle exists, length of cycle and meeting point of fast and slow pointers
def hasCycle(list:LinkedList):
    slow=list.head
    fast=list.head

    while(fast is not None and fast.next is not None):
        fast=fast.next.next
        slow=slow.next

        if (slow==fast):
            cycle_length=calculateCycleLength(slow)
            start_of_cycle=startOfCycle(list.head, cycle_length)
            return True, cycle_length, slow, start_of_cycle
    return False, None, None, None

def calculateCycleLength(slow:Node):
    current=slow
    cycle_length=0
    while True:
        current=current.next
        cycle_length+=1
        if current==slow:
            break
    return cycle_length

def startOfCycle(head:Node,cycle_length:int):
    start=head
    mover=head

    for _ in range(cycle_length):
        mover=mover.next
    while start!=mover:
        start=start.next
        mover=mover.next
    return mover



def main():

    ## Creating a cycled linked list
    list=LinkedList()
    for _ in range(5):
        list.appendEnd(_)
    
    list.head.next.next.next.next.next=list.head

    ## Commenting out list printing because it'll run infinetely
    #list.printList()

    cycle, length, meet_node, cycle_start_node = hasCycle(list)

    if cycle:
        print(f"Cycle exists in LinkedList with length: ", end="-->")
        print(length)
        print("meeting node is : "+str(meet_node.data))
        print("Cycle start at node: "+str(cycle_start_node.data))
    else:
        print("No cycle in LinkedList")


if __name__== "__main__":
    main()