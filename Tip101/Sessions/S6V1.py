
# 1


'''  
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
head = Node(1, Node(2))
'''
''' 
# 2
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def count_element(head, val):
    count = 0 
    current = head
	
    while current:
        if current.value == val:
            count += 1
        current = current.next
    return count

# Input List: 3 -> 1 -> 2 -> 1
# Input: head = 3, val = 1
head = Node(3, Node(1, Node(2, Node(1)) ))

print(count_element(head, 1))
'''

''' 
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
        
# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 
		
	# Start from the head and find the second-to-last node
    current = head
    while current.next.next: 
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head
head = Node(1, Node(2, Node(3, Node(4)) ))

print_list(head)

head = remove_tail(head)
# shortened list 
print_list(head)


'''


# 4
''' 
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def find_middle_element(head):
    slow = head 
    fast = head 

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
    return slow.value
'''
# 5 
#head = Node(1, Node(2, Node(3, Node(4)) ))
#print(find_middle_element(head))


# 6 
''' 
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_palindrome(head):
    slow = head 
    fast = head 
    prev = None

    # reverse 
    while fast and fast.next:
        fast = fast.next.next 
        nextNode = slow.next

        slow.next = prev
        prev = slow 
        slow = nextNode
# compare left vs right 
    if fast:
        slow = slow.next 
        
    while slow:
        if slow.value != prev.value:
            return False
        slow = slow.next
        prev = prev.next
    return True
    

head = Node(1, Node(1, Node(41, Node(1, Node(1)))))
print(is_palindrome(head))
'''
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse(head):
    curr = head 
    prev = None
    while curr:
        next_node = curr.next  # store
        curr.next = prev  # reverse pointer 
        prev = curr         # moves prev to current node
        curr = next_node    # increment  to next node
    return prev 

def print_nodes(head):
    while head:
        print(head.value )
        head = head.next 
    


head = Node(1, Node(1, Node(41, Node(1, Node(3)))))
print_nodes(reverse(head))
''' 
# https://leetcode.com/problems/reverse-linked-list/description/

# neetcode 150  -> linked list 
#     https://neetcode.io/practice?tab=neetcode150

#    https://www.linkedin.com/in/jose-jobins/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head 

        while curr:
            next_node = curr.next  # store
            curr.next = prev  # reverse pointer 
            prev = curr         # moves prev to current node
            curr = next_node
        return prev
    


