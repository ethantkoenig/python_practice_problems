
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
  if root_node.left == None and root_node.right == None:
    # If the root node has neither a right child nor a left child, then there
    # are no only children at all, and we can just return the empty list.
    return []

  if root_node.left == None and root_node.right != None:
    # If the root node has a right child, but no left child, then the right
    # child is an "only child". In addition, there might be some more "only
    # children" deeper in the right subtree.
    #
    # By making a recursive call on the right child (i.e. by calling
    # `values_of_only_children(root_node.right)`), we can get the values of the
    # all of "only children" in the right subtree. We then append
    # `root_node.right.value` (i.e. the value of the right child) to this list,
    # because the right child is itself an only child.
    right_subtree_only_children_values = values_of_only_children(root_node.right)
    right_subtree_only_children_values.append(root_node.right.value)
    return right_subtree_only_children_values

  if root_node.left != None and root_node.right == None:
    # Similarly, if there is a left child, but no right child...
    left_subtree_only_children_values = values_of_only_children(root_node.left)
    left_subtree_only_children_values.append(root_node.left.value)
    return left_subtree_only_children_values

  # Otherwise, the root_node has both a left child and a right child; therefore
  # neither the left child nor the right child is an "only child", since they
  # are each other's "siblings".
  #
  # We make recursive calls the get the values of the "only children" in the
  # left and right subtrees, respectively.
  left_subtree_only_children_values = values_of_only_children(root_node.left)
  right_subtree_only_children_values = values_of_only_children(root_node.right)

  # We want to return the values of all the "only children" in the left subtree,
  # and the values of all the "only children" in the right subtree.
  #
  # Recall that we can use + (i.e. the plus operator) to concatenate two lists.
  return left_subtree_only_children_values + right_subtree_only_children_values


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
