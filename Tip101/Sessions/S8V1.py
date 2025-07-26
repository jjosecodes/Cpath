

'''
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)
 '''

# 2 
''' 
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    return root.val == root.left.val + root.right.val
	

TestRoot = TreeNode(10, TreeNode(5), TreeNode(6))
print( check_tree(TestRoot))
\
Example Input Tree #1: 
  10
 /  \
4    6 
Input: root = 10
Expected Output: True



class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    left_node = root.left.val if root.left else 0
    right_node = root.right.val if root.right else 0
    
    return root.val == left_node + right_node
    
TestRoot = TreeNode(5, TreeNode(3), TreeNode(2))
TestRoot1 = TreeNode(5, TreeNode(900000), TreeNode(2))
print( check_tree(TestRoot))
print( check_tree(TestRoot1))


# 4

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    if not root:
        return None
    current = root
    while current.left:
        current = current.left
    return current.val

tree1 = TreeNode(1,
         TreeNode(2, TreeNode(4), TreeNode(3)),
         TreeNode(5))
print(left_most(tree1)) 

tree2 = TreeNode(1, None,
         TreeNode(2, TreeNode(3)))
print(left_most(tree2)) 


    if not root:
        return None
 '''


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    if not root.left:
        return root.val
    return left_most(root.left)















