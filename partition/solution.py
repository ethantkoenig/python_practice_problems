# Swaps the elements at indices `i` and `j` in the list `l`. This swap is
# in-place (i.e. modifying the existing list instead of returning a new list).
#
# Arguments:
# l (type: list of ints): list whose elements will be swapped.
# i (type: int): one index to swap
# j (type: int): the other index to swap
def swap(l, i, j):
  element_that_was_previously_at_index_i = l[i]
  element_that_was_previously_at_index_j = l[j]
  l[i] = element_that_was_previously_at_index_j
  l[j] = element_that_was_previously_at_index_i


# Partitions the given list in-place (i.e. modifying the existing list instead
# of returning a new list).
#
# Arguments:
# l (type: list of ints): the list to partition. You may assume it is non-empty
# (i.e. has a length of at least 1).
#
# Example: in the following code
#
# l = [4,3,7,1,5]
# partition(l)
#
# `l` is now partitioned with a pivot of 4, and might equal [3,1,4,7,5]
# (although the order of the "less-than-4" and "greater-than-4" sections may
# vary).
def partition(l):
  pivot = l[0]

  # At any given point in the below while loop, the list will contain the
  # following:
  # - index 0: the pivot
  # - indices 1 (inclusive) to greater_than_start_index (exclusive):
  # "less-than-pivot" elements
  # - indices greater_than_start_index (inclusive) to unknown_start_index
  # (exclusive): "greater-than-pivot" elements
  # - indices unknown_start_index (inclusive) to len(l) (exclusive): unexamined
  # elements
  #
  #                                  unknown_start_index
  #                                       |
  #             greater_than_start_index  |                    len(l)
  #                     |                 |                     |
  #                     |                 |                     |
  #  0     1            v                 v                     v
  # +-----+------------+-----------------+---------------------+
  # |     |            |                 |                     |
  # |     |elements    |elements         |unexamined           |
  # |pivot|less than   |greater          |elements             |
  # |     |pivot       |than pivot       |                     |
  # |     |            |                 |                     |
  # +-----+------------+-----------------+---------------------+
  greater_than_start_index = 1
  unknown_start_index = 1

  while unknown_start_index < len(l):
    # Look at the next unexamined element.
    element = l[unknown_start_index]
    if element < pivot:
      # If `element` is less than the pivot, then we swap the first (i.e.
      # leftmost) "greater-than-element" with the current element.
      swap(l, greater_than_start_index, unknown_start_index)
      # The element we just swapped into index `greater_than_start_index`
      # (i.e. the variable `element`) is less than the pivot, so we need to
      # increment `greater_than_start_index` so that the "greater-than-pivot"
      # region starts immediately to the right of this just-swapped element.
      greater_than_start_index = greater_than_start_index + 1

    # Otherwise, if `element` is greater than the pivot, we don't have to do any
    # swapping at all! This is because `element` is already next to the "right
    # border" of the "greater-than-pivot" region, so after we increment
    # `unknown_start_index` below (which moves the "right border" of the
    # "greatern-than-pivot" region to the right), this element will be in the
    # "greater-than-pivot" region.

    # Now that we have handled the element that was at index
    # `unknown_start_index`, we can increment the variable for the next
    # iteration of the while loop.
    unknown_start_index = unknown_start_index + 1

  # The while loop ends once `unknown_start_index` reaches len(l), at which
  # point the are no remaining unexamined elements (i.e. the "unexamined
  # elements" region in the diagram above has a "width" of zero).
  #
  # The only thing left to do at this point is to swap the pivot (which is still
  # at index 0) with the very last (i.e. rightmost) element in the
  # "less-than-pivot" section, so that the pivot appears between the
  # "less-than-pivot" and "greater-than-pivot" sections.
  #
  # Since the first (i.e. leftmost) element of the "greater-than-pivot" section
  # is at index `greater_than_start_index, and last (i.e. right) element of the
  # "less-than-pivot" section is at index `greater_than_start_index - 1`.
  swap(l, 0, greater_than_start_index - 1)


l = [4,3,7,1,5]
partition(l)
# l should now be partitioned with a pivot of 4 (e.g. possibly [3,1,4,7,5])
print(l)
