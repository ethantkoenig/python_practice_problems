
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
  # root_of_subtree_to_search will refer to the root node of the subtree that we
  # currently need to search (or None if there is nothing left to search).
  # Initially, we need to search the entire tree, so we set it to root_node.
  root_of_subtree_to_search = root_node

  while root_of_subtree_to_search != None:
    # if the root of the subtree we are currently searching has the value we are
    # looking for, then we are done, and can return True immediately.
    if root_of_subtree_to_search.value == value:
      return True
    if root_of_subtree_to_search.value < value:
      # if the root's value is less than what we are looking for, we need to
      # search in the root's right sub-tree. We'll update the
      # root_of_subtree_to_search variable to the current root's right child, so
      # that we will begin searching the right subtree in the next iteration of
      # this while loop.
      #
      # There's a chance that the root does not have a right child (and thus has
      # no right sub-tree); in this case, we will be setting
      # root_of_subtree_to_search to None, and the while loop will stop after
      # this iteration.
      root_of_subtree_to_search = root_of_subtree_to_search.right
    else:
      # Similarly, if the root's value is greater than what we are looking for,
      # we need to search in the root's left sub-tree.
      root_of_subtree_to_search = root_of_subtree_to_search.left
  # If we've reached this point, then `root_of_subtree_to_search` is None, and
  # there's nothing left to search. We've haven't found what we were looking
  # for, so we return False.
  return False


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
