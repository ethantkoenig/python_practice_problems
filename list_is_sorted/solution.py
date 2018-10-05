
# Returns a bool indicating whether the list is sorted (i.e. is non-decreasing,
# it is okay to have adjacent elements which are equal).
#
# Arguments:
# l (type: list of ints): list that may or may not be sorted.
#
# Example:
# list_is_sorted([1,2,2,8,9]) should return True.
# list_is_sorted([1,2,2,8,6]) should return False.
def list_is_sorted(l):
  # We will iterate through the elements of the list, and compare each element
  # with the next element (except for the last element of the list, which
  # does not have a next element).
  #
  # This variable tracks the index we are currently at. We initially set it to 0
  # because we want to start at the beginning of the list.
  index = 0

  # Once index reaches len(l)-1, there is no longer a "next" element to compare
  # to, so we can stop the while loop.
  while index < len(l) - 1:
    # If the element at index is strictly larger than the next element, then l
    # is not sorted. In this case, we can immediately return False.
    if l[index] > l[index + 1]:
      return False

    # Update index to one larger than its previous value.
    index = index + 1

  # We have iterated through the entire list, and every element is
  # less-than-or-equal-to the next element (expect for the last element, for
  # which there is no next element), so the list is sorted, and we can return
  # True.
  return True


# This should print True
print(list_is_sorted([1,2,2,8,9]))

# This should print False
print(list_is_sorted([1,2,2,8,6]))
