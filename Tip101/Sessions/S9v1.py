
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    if not root:
        return True
    def checker( left, right):
        # check for children 
        if not left and not right:
            return True 
        # check for equality 
        if not left or not right or left.val != right.val:
            return False
        # recursively call 
        return checker(left.left , right.right) and checker(left.right, right.left)
    return checker(root.left , root.right) if root else True
# time 
# O(n) i think
# space 
# O(h) - based on height 

# test 
root1 = TreeNode(1)
root1.left = TreeNode(2, TreeNode(3), TreeNode(4))
root1.right = TreeNode(2, TreeNode(4), TreeNode(3))
print(is_symmetric(root1))  # Expected Output: True

root2 = TreeNode(1)
root2.left = TreeNode(2, None, TreeNode(3))
root2.right = TreeNode(2, None, TreeNode(3))

print(is_symmetric(root2))  # Expected Output: False

''' 


Example Tree #1:

       1
     /   \
    /     \
   2       2
  / \     / \
 3   4   4   3
           |
 

Input: root = 1
Expected Output: True
'''






'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def binary_tree_paths(root):
    paths = []
    
    def dfs(node, path):
        if not node.left and not node.right:
            paths.append(path)
            return
        if node.left:
            dfs( node.left , path + "-> " + str(node.left.val))
        if node.right:
            dfs( node.right , path + "-> " + str(node.right.val))

    dfs(root, str(root.val))

    return paths

# ex 
# Example Tree 1
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root1.left.right = TreeNode(5)

# Expected output: ["1->2->5", "1->3"]
print(binary_tree_paths(root1))






'''