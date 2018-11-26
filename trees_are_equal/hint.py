# You're should use recursion for this problem. However, this problem is a
# little different than other recursive tree problems we've seen so far, since
# there are two trees in this problem.
#
# Normally, we consider the four possible cases for the root node of a binary
# tree:
# - no left nor right child
# - left child, but no right child
# - right child, but no left child
# - both a left and right child
#
# Since there are two trees, `root_a` will fall into one of the four possible
# cases above, and `root_b` will also fall into one of the four possible cases.
# However, if the trees fall into different cases (e.g. `root_a` has both a left
# and right child, `root_b` has a left child but no right child), then the two
# trees are not equal, since they don't have the same "shape".
#
# If `root_a` and `root_b` fall into the same case, then the trees might be
# equal (but aren't guaranteed to be). Suppose both `root_a` and `root_b` have a
# left child but no right child. What condition(s) should we check for in the
# left subtrees of `root_a` and `root_b` to determine whether `root_a` and
# `root_b` are equal?
