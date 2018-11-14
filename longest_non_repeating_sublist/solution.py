
# Given a (unsorted) list of ints, return the longest sublist of that list that
# does not contain any repeating/duplicate elements. Sublists must be contiguous
# (i.e. must correspond to an uninterrupted range of the original list).
#
# If there are multiple such sublists that are tied for being the longest, the
# function should return one of them (doesn't matter which one).
#
# Arguments:
# l (type: list of ints): a list that is not necessarily sorted.
#
# Example:
# longest_non_repeating_subarray([1,2,3,2,5,4,2]) should return [3,2,5,4].
def longest_non_repeating_sublist(l):
  # The start/end indices of the "current" sublist. We will try adding more
  # elements to the end of this sublist (i.e. by increasing `end_index`), and
  # will drop elements from the beginning of the sublist (i.e. by increasing
  # `start_index`) to prevent duplicates from appearing in the list.
  #
  # `start_index` is inclusive, and `end_index` is exclusive.
  start_index = 0
  end_index = 0
  # A dictionary, whose keys are the elements in the sublist between `start_index`
  # (inclusive) and `end_index` (exclusive). The values of this dictionary are
  # None.
  elements_in_sublist = {}

  # The start/end indices of the best (i.e. longest) sublist we've seen so far.
  best_start_index_so_far = 0
  best_end_index_so_far = 0

  while end_index < len(l):
    next_element = l[end_index]
    # We are going to add `next_element` to our sublist, so if `next_element`
    # is already in the sublist, we need to increase `start_index` until we've
    # removed the previous occurrence of `next_element` from our sublist.
    #
    # Note that if `next_element` is not already in our sublist (or
    # equivalently, `next_element in elements_in_sublist` is false), this while
    # loop will not run at all.
    while next_element in elements_in_sublist:
      # Increment `start_index`, and update `elements_in_sublist` accordingly.
      #
      # Recall that `del elements_in_sublist[element_to_remove_from_sublist]`
      # will remove the key equal to `element_to_remove_from_sublist` (and its
      # associated value, which in this case is just None) from
      # `elements_in_sublist`.
      element_to_remove_from_sublist = l[start_index]
      del elements_in_sublist[element_to_remove_from_sublist]
      start_index = start_index + 1

    # Include `next_element` in our sublist, and update `elements_in_sublist`
    # accordingly.
    elements_in_sublist[next_element] = None
    end_index = end_index + 1

    # If our current sublist is better (i.e. longer) than anything we've seen so
    # far, update `best_start_index_so_far` and `best_end_index_so_far`
    # accordingly.
    if end_index - start_index > best_end_index_so_far - best_start_index_so_far:
      best_start_index_so_far = start_index
      best_end_index_so_far = end_index

  # Now that we've gone over the whole list, the best (i.e. longest) sublist
  # that we've seen "so far" is in fact the best (i.e. longest) sublist in the
  # entire list, so we'll return that sublist.
  return l[best_start_index_so_far:best_end_index_so_far]


# This should print [3,2,5,4]
print(longest_non_repeating_sublist([1,2,3,2,5,4,2]))
