
# This defines the TreeNode class, so that we can create TreeNode objects.
#
# Recall that TreeNode objects should have three fields:
# - value: the value associated with this particular node (for simplicity, let's
#          assume it's always an int).
# - left: the left child of this node (or None)
# - right: the right child of this node (or None)
class TreeNode(object):
  pass

# Returns the values of the "sibling-less" nodes in a binary tree. The return
# value will be a list of ints, and doesn't have to be in any particular order.
#
# Arguments:
# root_node (type: TreeNode): the root node of a binary tree (NOTE: not
#                             necessarily a binary search tree!)
#
# Example: if the variable root_node refers to the root of the following tree:
#
#      5
#      |
#      +------>10
#               |
#           4<--+-->12
#           |
#        8<-+
#
# values_of_only_children(root_node) should return [8, 10], since the
# "only-child" nodes of this tree are the nodes with values 8 and 10. It's okay
# if the return value is in a different order (e.g. [10, 8]), so long as it's a
# list containing 8 and 10.
def values_of_only_children(root_node):
  pass # TODO: remove this placeholder, and write the function!


# Define the tree from the example above.
root_node = TreeNode()
root_node.value = 5
root_node.left = None
root_node.right = TreeNode()

root_node.right.value = 10
root_node.right.left = TreeNode()
root_node.right.right = TreeNode()

root_node.right.left.value = 4
root_node.right.left.left = TreeNode()
root_node.right.left.right = None

root_node.right.left.left.value = 8
root_node.right.left.left.left = None
root_node.right.left.left.right = None

root_node.right.right.value = 12
root_node.right.right.left = None
root_node.right.right.right = None

# This should print [8, 10] (or [10, 8]).
print(values_of_only_children(root_node))
