
# This defines the TreeNode class, so that we can create TreeNode objects.
#
# Recall that TreeNode objects should have three fields:
# - value: the value associated with this particular node (for simplicity, let's
#          assume it's always an int).
# - left: the left child of this node (or None)
# - right: the right child of this node (or None)
class TreeNode(object):
  pass


# Returns a bool indicating whether a binary search tree contains a node with
# the specified value.
#
# Arguments:
# root_node (type: TreeNode): the root node of a binary search tree
# value (type: int): the value to look for in the tree
#
# Example: if the variable root_node refers to the root of the following tree:
#
#          8
#          |
#     4<---+--->10
#     |         |
# 3<--+     9<--+-->12
#
# binary_search_tree_contains(root_node, 4) should return True.
# binary_search_tree_contains(root_node, 11) should return False.
def binary_search_tree_contains(root_node, value):
  pass # TODO: remove this placeholder, and write the function!


# Define the tree from the example above.
root_node = TreeNode()
root_node.value = 8
root_node.left = TreeNode()
root_node.right = TreeNode()

root_node.left.value = 4
root_node.left.left = TreeNode()
root_node.left.right = None

root_node.left.left.value = 3
root_node.left.left.left = None
root_node.left.left.right = None

root_node.right.value = 10
root_node.right.left = TreeNode()
root_node.right.right = TreeNode()

root_node.right.left.value = 9
root_node.right.left.left = None
root_node.right.left.right = None

root_node.right.right.value = 12
root_node.right.right.left = None
root_node.right.right.right = None

# This should print True.
print(binary_search_tree_contains(root_node, 4))

# This should print False.
print(binary_search_tree_contains(root_node, 11))
