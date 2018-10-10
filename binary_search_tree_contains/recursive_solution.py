
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
  # if the root of the tree has the sought-after value, then we are done, and
  # can return True immediately.
  if root_node.value == value:
    return True

  if root_node.value < value:
    # if the root's value is less than the sought-after value, we need to search
    # in the root's right sub-tree. However, there's a chance that the root does
    # not have a right child (and thus has no right sub-tree); in this case,
    # there are no more places the sought-after value could possibly be, and we
    # can immediately return False.
    if root_node.right == None:
      return False
    # if the root does have a right sub-tree, recursively search for the
    # sought-after value there.
    return binary_search_tree_contains(root_node.right, value)
  else:
    # in this case, the root's value is greater than the sought-after value, so
    # we need to search to root's left sub-tree. Similar to before, there's a
    # chance the root does not have a left child (and thus has no left
    # sub-tree), in which case there are no more places to look, and we can
    # immediately return False.
    if root_node.left == None:
      return False
    # if the root does have a left sub-tree, recursively search for the
    # sought-after value there.
    return binary_search_tree_contains(root_node.left, value)


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
