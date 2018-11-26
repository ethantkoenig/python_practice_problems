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
  if root_a.value != root_b.value:
    # If the two root nodes have different values, then the trees cannot be
    # equal, so return False.
    return False

  if root_a.left == None and root_a.right == None:
    # If `root_a` has neither a left child nor a right child, then if `root_b`
    # has either a left child or a right child, the two trees are not equal.
    if root_b.left != None or root_b.right != None:
      return False
    # If `root_b` also has neither a left child nor a right child, then the two
    # trees are equal (since we've already check that the root nodes' values are
    # equal).
    return True

  if root_a.left != None and root_a.right == None:
    # If `root_a` has a left child but not a right child, then if `root_b`
    # either does not have a left child or has a right child, the two trees are
    # not equal.
    if root_b.left == None or root_b.right != None:
      return False
    # If `root_b` also has a left child but not a right child, then the two
    # trees are equal if the left subtrees are equal.
    return trees_are_equal(root_a.left, root_b.left)

  if root_a.left == None and root_a.right != None:
    # If `root_a` has a right child but not a left child, then if `root_b`
    # either does not have a right child or has a left child, the two trees are
    # not equal.
    if root_b.left != None or root_b.right == None:
      return False
    # If `root_b` also has a right child but not a left child, then the two
    # trees are equal if the right subtrees are equal.
    return trees_are_equal(root_a.right, root_b.right)

  # If we reach this point, it means that `root_a` has both a left child and
  # right child. If `root_b` either doesn't have a left child or doesn't have a
  # right child, then the two trees are not equal.
  if root_b.left == None or root_b.right == None:
    return False
  # If `root_b` also has both a left child and right child, thn the two trees
  # are equals if the left subtrees are equal AND the right subtrees are equal.
  return trees_are_equal(root_a.left, root_b.left) and trees_are_equal(root_a.right, root_b.right)

# Define the trees from the example above.
root_a = TreeNode()
root_a.value = 5
root_a.left = TreeNode()
root_a.right = None

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
root_b.right.right = None

# This should print False.
print(trees_are_equal(root_a, root_b))

# This should print True (since a tree is always equal to itself).
print(trees_are_equal(root_a, root_a))
