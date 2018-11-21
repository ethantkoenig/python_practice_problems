# This defines the TreeNode class, so that we can create TreeNode objects.
#
# Recall that TreeNode objects should have three fields:
# - value: the value associated with this particular node (for simplicity, let's
#          assume it's always an int).
# - left: the left child of this node (or None)
# - right: the right child of this node (or None)
class TreeNode(object):
  pass

# Given a binary tree, returns a list of ints, where the elements in the
# returned list correspond to the number of nodes in each "level" (i.e.
# horizontal row) of the tree.
#
# Arguments:
# root_node (type: TreeNode): the root node of a binary tree (NOTE: not
#                             necessarily a binary search tree!)
#
# Example: if the variable root_node refers to the root of the following tree:
#
#          5
#         / \
#        8   9
#       / \   \
#      3  10   6
#
# num_nodes_in_tree(root_node) should return [1, 2, 3], since the levels/rows
# of the tree are:
# row 0: 5        (1 node)
# row 1: 8, 9     (2 nodes)
# row 2: 3, 10, 6 (3 nodes)
def num_nodes_by_level(root_node):
  # `left_subtree_levels` will store the number of nodes at each level in the
  # left subtree. We will leave it as the empty list in the case where there is
  # no left subtree at all.
  left_subtree_levels = []
  if root_node.left != None:
    left_subtree_levels = num_nodes_by_level(root_node.left)

  # Similarly, ...
  right_subtree_levels = []
  if root_node.right != None:
    right_subtree_levels = num_nodes_by_level(root_node.right)

  # The first level consists only of the root node, so there's always going to
  # be 1 node in that level.
  levels = [1]

  # For each subsequent level, the number of nodes in that level will be the
  # number of nodes at that level in the left subtree (assuming there is a left
  # subtree, and it has any nodes at that level), plus the number of nodes at
  # that level in the right subtree (similarly, assuming ...).
  #
  # However, it's possible that one subtree is deeper than the other (i.e.
  # `left_subtree_levels` and `right_subtree_levels` might have different
  # lengths), so we need to account for that possibility.
  #
  # We can stop once we passed the "bottom" of both the left and right
  # subtrees, or equivalently, once we reached the end of both the
  # `left_subtree_levels` and `right_subtree_levels` lists.
  index = 0
  while index < len(left_subtree_levels) or index < len(right_subtree_levels):
    num_nodes_at_current_level = 0

    # If there are any nodes in the left subtree at the current level, include
    # them.
    if index < len(left_subtree_levels):
      num_nodes_at_current_level = num_nodes_at_current_level + left_subtree_levels[index]

    # If there are any nodes in the right subtree at the current level, include
    # them.
    if index < len(right_subtree_levels):
      num_nodes_at_current_level = num_nodes_at_current_level + right_subtree_levels[index]

    levels.append(num_nodes_at_current_level)
    index = index + 1

  return levels


# Define the tree from the example above.
root_node = TreeNode()
root_node.value = 5
root_node.left = TreeNode()
root_node.right = TreeNode()

root_node.left.value = 8
root_node.left.left = TreeNode()
root_node.left.right = TreeNode()

root_node.left.left.value = 3
root_node.left.left.left = None
root_node.left.left.right = None

root_node.left.right.value = 10
root_node.left.right.left = None
root_node.left.right.right = None

root_node.right.value = 9
root_node.right.left = None
root_node.right.right = TreeNode()

root_node.right.right.value = 6
root_node.right.right.left = None
root_node.right.right.right = None

# This should print [1, 2, 3].
print(num_nodes_by_level(root_node))
