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
  pass # TODO: remove this placeholder, and write the function!


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
