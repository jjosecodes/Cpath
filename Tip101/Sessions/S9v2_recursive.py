



class Listnode:
    def __init__(self, val = 0, next = None):
        self.val = val 
        self.next = next

def ReverseLL(head: Listnode) -> Listnode:
    # base 
    if not head or not head.next:
        return head 

    # recurse 
    reverseLL = ReverseLL(head.next)
    # go to next node
    head.next.next = head
    head.next = None 
    # return reverse 
    return ReverseLL
    


