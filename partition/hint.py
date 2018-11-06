
# First, try to write the following helper function.

# Swaps the elements at indices `i` and `j` in the list `l`. This swap is
# in-place (i.e. modifying the existing list instead of returning a new list).
#
# Arguments:
# l (type: list of ints): list whose elements will be swapped.
# i (type: int): one index to swap
# j (type: int): the other index to swap
def swap(l, i, j):
  pass # TODO: remove this placeholder, and write the function!


# Recall that as we were working through the example on the whiteboard, at any
# given point our list looked something like:
#
# +-----+------------+-----------------+---------------------+
# |     |            |                 |                     |
# |     |elements    |elements         |unexamined           |
# |pivot|less than   |greater          |elements             |
# |     |pivot       |than pivot       |                     |
# |     |            |                 |                     |
# +-----+------------+-----------------+---------------------+
#
# We will need to introduce some variables to keep track of the "borders" between one region
# (i.e. "less-than-pivot" elements) and the next (i.e. "greater-than-pivot"
# elements).
#
# Each element that we consider will either be less than the pivot, or greater
# than the pivot. In each of these two cases, think about
# - what swaps (if any) do we need to perform, and
# - how should our "border" variables be updated
