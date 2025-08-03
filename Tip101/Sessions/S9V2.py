


# u 
# reverse without new list 
# M - pointers and LL 
# P 
'''
get current node
store node 
reverse the pointer 
move to next node 
: 1 → 3 → 5 → 7 → 9 # head = [1, 3, 5, 7, 9]
9 → 7 → 5 → 3 → 1 # [9, 7, 5, 3, 1]
'''

class Listnode:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next

def ReverseLL(head: Listnode) -> Listnode:
    prev = None 
    curr = head
    next_node = 0 


    while curr:
        next_node = curr.next
        curr.next = prev 
        prev = curr
        curr = next_node
    return prev



''' 
    # base 
    if not head or head.next:
        return head 

    # recurse 
    reverseLL = ReverseLL(head.next)
    # go to next node
    head.next.next = head
    head.next = None 
    # return reverse 
    return ReverseLL
    

    # answer 
    def reverseList(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    reversed_head = reverseList(head.next)
    head.next.next = head
    head.next = None
    return reversed_head

    
'''