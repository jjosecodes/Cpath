''' 
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_univalued(root):
    if root is None:
        return True 
    if root.left and root.left.val != root.val:
        return False
    if root.right and root.right.val != root.val:
        return False
    return is_univalued(root.left) and is_univalued(root.right)

# node = TreeNode(1,TreeNode(1,TreeNode(1), TreeNode(1)),
#                TreeNode(1,TreeNode(19), TreeNode(1)))

# is_univalued(node)
#print(is_univalued(node))

'''
'''
# iterate through the left branch and find height
#
# d nac ew tfel rehtruf on si ereht ecno dnuof eb lliw thgie
#iterate through the right branch and find  height
#compare both the heights that are stored in variables and return the largest one


class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def height(root):
    hleft = 0
    hright = 0

    # left height 
    node = root 
    while node:
        hleft += 1
        node = node.left 

    # r height 
    node = root 
    while node:
        hright += 1 
        node = node.right
    
    return max(hleft, hright)

node = TreeNode(1)


print(height(node))

''' 




'''
class TreeNode():
    def __init__(self, key, value, left=None, right=None):
            self.key = key
            self.val = value
            self.left = left
            self.right = right

def insert(root, key, value):
    if root is None:
        return TreeNode(key, value)
    if key < root.key: 
        root.left = insert(root.left, key, value )
    
    elif key > root.key:
        root.right = insert(root.right, key, value )
    # go right  
    
    else: 
        root.val = value 

    return root



#chat test 
root = TreeNode(10, "root",
        TreeNode(5, "left",
            TreeNode(1, "left.left"),
            TreeNode(6, "left.right")),
        TreeNode(15, "right"))

# Insert new key 9 with value "Naruto"
insert(root, 9, "Naruto")
def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(f"{root.key}: {root.val}")
    inorder(root.right)

inorder(root)

''' 



class TreeNode():
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right

def remove_bst(root, key):
	# Locate the node to be removed
	# If the node is a leaf node:
    if key < root.key:
        root.left = remove_bst(root.left, key)

    elif key > root.key:
        root.right = remove_bst(root.right, key)

    else:
        if root.left is None and root.right is None:
            # change 

            return None
        

		# Remove the node by redirecting the appropriate child reference of its parent to None
	# If the node has one parent:
    if root.left is None:
        return root.right
    elif root.right is None:
        return root.left
    
		# Replace the node with its child, updating its parent's nodes child reference appropriately
	# If the node has two children:

		# Find the node's inorder successor (smallest node in right subtree)
		# Swap the value of the node and its inorder successor
		# Recursively remove the successor (which now has the current node's value)
	# Return the root of the updated tree



