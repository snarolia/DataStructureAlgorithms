"""
Operations covered:
1. Reversal of Linked List
2. Merging two sorted arrays
"""

from LinkedList import Node, LinkedList

ll_obj=LinkedList()

"""
1-->2-->3-->4-->5
"""

def ReverseLinkedList(ll, head):

    """

    Curr	next	prev    curr=next	
    1	    2	    1	
    2	    3	    2
    3	    4	    3	
    4	None	    4

    So prev needs to be set to head, for traversal of the linked list

    """
    prev=None
    curr=head

    while curr:
        next=curr.next ## next=2
        curr.next=prev
        prev=curr
        curr=next
    ll.head=prev
## Creating a linked list
for _ in range(10):
    ll_obj.appendEnd(_)

def merge(list1:LinkedList, list2:LinkedList):
    dummy_head=Node(0)
    tail=dummy_head

    curr1, curr2 = list1.head, list2.head

    while curr1 and curr2:
        if curr1.data<curr2.data:
            tail.next=curr1
            curr1=curr1.next
        else:
            tail.next=curr2
            curr2=curr2.next
        tail=tail.next
    tail.next=curr1 if curr1 else curr2
    merged=LinkedList()
    merged.head=dummy_head.next
    return merged
    
def MergeSortedLists(list1:LinkedList, list2:LinkedList):
    return LinkedList() if (list1 is None and list2 is None)\
        else list1 if list2 is None \
            else list2 if list1 is None \
                else merge(list1, list2)


list1=LinkedList()
list2=LinkedList()

for _ in [1,3,5,7]:
    list1.appendEnd(_)
for _ in [2,4,6,8,10]:
    list2.appendEnd(_)

sorted_list = MergeSortedLists(list1, list2)
sorted_list.printList()


# print("Original List")
# ll_obj.printList()

# print("Reversed List")
# ReverseLinkedList(ll_obj, ll_obj.head)
# ll_obj.printList()