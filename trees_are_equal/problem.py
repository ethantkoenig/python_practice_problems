# This defines the TreeNode class, so that we can create TreeNode objects.
#
# Recall that TreeNode objects should have three fields:
# - value: the value associated with this particular node (for simplicity, let's
#          assume it's always an int).
# - left: the left child of this node (or None)
# - right: the right child of this node (or None)
class TreeNode(object):
  pass

# Returns a bool, indicating whether the tree rooted at `root_a` is equal to the
# tree rooted at `root_b`. By equal, we mean that the trees have the same
# structure (i.e. the same shape), and each node in one tree has the same value
# as the corresponding node in the other tree.
#
# Arguments:
# root_a (type: TreeNode): the root node of a binary tree
# root_b (type: TreeNode): the root node of a binary tree
#
# Example: if `root_a` refers to the root of the following tree:
#
#          5
#         /
#        8
#       / \
#      3  10
#
# and `root_b` refers to the root of the following tree:
#
#          5
#         / \
#        8   9
#       / \
#      3  10
#
# trees_are_equal(root_a, root_b) should return False, since the trees have a
# different shape (namely, the root node `root_a` does not have a right child,
# but the root node `root_b` does.
def trees_are_equal(root_a, root_b):
  pass # TODO: remove this placeholder, and write the function!

# Define the trees from the example above.
root_a = TreeNode()
root_a.value = 5
root_a.left = TreeNode()
root_a.right = TreeNode()

root_a.left.value = 8
root_a.left.left = TreeNode()
root_a.left.right = TreeNode()

root_a.left.left.value = 3
root_a.left.left.left = None
root_a.left.left.right = None

root_a.left.right.value = 10
root_a.left.right.left = None
root_a.left.right.right = None

root_b = TreeNode()
root_b.value = 5
root_b.left = TreeNode()
root_b.right = TreeNode()

root_b.left.value = 8
root_b.left.left = TreeNode()
root_b.left.right = TreeNode()

root_b.left.left.value = 3
root_b.left.left.left = None
root_b.left.left.right = None

root_b.left.right.value = 10
root_b.left.right.left = None
root_b.left.right.right = None

root_b.right.value = 9
root_b.right.left = None
root_b.right.right = TreeNode()

# This should print False.
print(trees_are_equal(root_a, root_b))

# This should print True (since a tree is always equal to itself).
print(trees_are_equal(root_a, root_a))
