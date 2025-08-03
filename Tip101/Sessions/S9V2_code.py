'''
#Max is in
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

from collections import deque

def level_order(root):
    # If the tree is empty:
    # return an empty list
    if root is None:
        return []
    # Create an empty queue using deque & Add the root to the queue
    queue = deque([root])

    # Create an empty list to store the explored nodes
    result = []

    # While the queue is not empty:
    while queue:
    # Pop the next node off the queue (pop from the left side!)
        node = queue.popleft()
        
    # Add the popped node to the list of explored nodes
        result.append(node.val)
    # Add each of the popped node's children to the end of the queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    # Return the list of visited nodes
    return result 




# Sample Input Tree:
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

print(level_order(root))  # Expected Output: [1, 2, 3, 4, 5]

''' 
from collections import deque


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
        
        
def min_depth(root):
	#define an empty queue
    pass





