
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
  # currently need to search. Initially, we need to search the entire tree, so
  # we set it to root_node.
  root_of_subtree_to_search = root_node

  # Recall that while loops run until the corresponding condition becomes False.
  # True will never be False, so this means that this loop will never stop
  # looping! Luckily, we can still include return statements inside the loop
  # body, and the function will stop executing once we hit a return statement.
  while True:
    # if the root of the subtree we are currently searching has the value we are
    # looking for, then we are done, and can return True immediately.
    if root_of_subtree_to_search.value == value:
      return True
    if root_of_subtree_to_search.value < value:
      # if the root's value is less than what we are looking for, we need to
      # check the root's right sub-tree. However, there's a chance that the root
      # does not have a right child (and thus has no right sub-tree); in this
      # case, there are no more places the sought-after value could possibly be,
      # and we can immediately return False.
      if root_of_subtree_to_search.right == None:
        return False
      # In the next iteration of this while-loop, we want to search the right
      # subtree of root_of_subtree_to_search, so we update the
      # root_of_subtree_to_search variable accordingly.
      root_of_subtree_to_search = root_of_subtree_to_search.right
    else:
      # similarly, if the root's value is greater than what we are looking for, we need to
      # check the root's left sub-tree. However, there's a chance that the root
      # does not have a left child (and thus has no left sub-tree); in this
      # case, there are no more places the sought-after value could possibly be,
      # and we can immediately return False.
      if root_of_subtree_to_search.left == None:
        return False
      # In the next iteration of this while-loop, we want to search the left
      # subtree of root_of_subtree_to_search, so we update the
      # root_of_subtree_to_search variable accordingly.
      root_of_subtree_to_search = root_of_subtree_to_search.left


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
