
# This defines the TreeNode class, so that we can create TreeNode objects.
#
# Recall that TreeNode objects should have three fields:
# - value: the value associated with this particular node (for simplicity, let's
#          assume it's always an int).
# - left: the left child of this node (or None)
# - right: the right child of this node (or None)
class TreeNode(object):
  pass

# Returns the number of nodes in a binary tree.
#
# Arguments:
# root_node (type: TreeNode): the root node of a binary tree (NOTE: not
#                             necessarily a binary search tree!)
#
# Example: if the variable root_node refers to the root of the following tree:
#
#          5
#          |
#     8<---+--->10
#     |         |
# 3<--+     9<--+-->12
#
# num_nodes_in_tree(root_node) should return 6, since the tree has 6 nodes.
def num_nodes_in_tree(root_node):
  pass # TODO: remove this placeholder, and write the function!

# Define the tree from the example above.
root_node = TreeNode()
root_node.value = 5
root_node.left = TreeNode()
root_node.right = TreeNode()

root_node.left.value = 8
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

# This should print 6.
print(num_nodes_in_tree(root_node))
