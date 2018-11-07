
# You will want to use recursion for this problem. There are four cases to
# consider:
# - `root_node` has neither a left child nor a right child
# - `root_node` has a right child, but no left child
# - `root_node` has a left child, but no right child
# - `root_node` has both a left child and a right child
#
# For each case, think about:
# - which of root_node's children (if any) are only children?
# - what recursive calls (if any) will we need to make?
#
# As with other recursive problems, we are going to be making recursive calls on
# "subproblems" (unless we're in the base case, in which case we won't make any
# recursive calls). This means we are going to be solving the same problem
# (i.e. finding the values of all "only children") for some subtree or subtrees
# of `root_node`.
#
# As a tip, remember that you can use + (i.e. the plus operator) to concatenate
# two lists, e.g. `[1,3] + [6,2,4]` becomes the list `[1,3,6,2,4]`.
