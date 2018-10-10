
# Take a look at your solution to the problem of finding the maximum value in a
# binary tree (maxrootnode.py on IncrediblePitifulOutcome).
#
# In that problem, we (potentially) made two recursive calls: one recursive call
# on the left child (if it exists), and one recursive call on the right child
# (if it exists). These recursive calls returned the maximum value in the left
# sub-tree, and the maxium value in the right sub-trees, respectively. Once we
# knew the maximum value in the left and right sub-trees, we were able to figure
# out the maximum value in the original tree.
#
# The approach here is going to be similar; we're going to make recursive calls
# on the left child (if it exists) and right child (if it exists), which will
# tell us how many nodes are in the left sub-tree and how many nodes are in the
# right sub-tree, respectively. Once we know how many nodes are in the left and
# right sub-trees, how can we figure out the number of nodes in the original
# tree?
