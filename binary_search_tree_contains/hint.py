# Try to do the following:
# - start at the root_node, and compare that node's value with the sought after
#   value. There are 3 cases:
#   - root node's value == sought-after value
#   - root node's value < sought-after value
#   - root node's value > sought-after value
#   The equality is easy to handle, we've just found what we were looking for!
#
#   In the two inequality cases (less-than, greater-than), we will be able to
#   focus our search of one of the root node's subtrees, and will be able to
#   ignore the other subtree. Think about which subtree (i.e. left vs. right) we
#   should subsequently search for each of the two inequality cases (less-than,
#   greater-than).
#
#   Also, what should happen if the subtree we should continue our search in
#   (e.g.  the right subtree) does not exist (e.g. because the node does not
#   have a right child)?
