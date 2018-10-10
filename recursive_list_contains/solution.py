
# Returns whether the list contains the specified value.
#
# Arguments:
# l (type: list of ints): list that may or may not be sorted.
# value (type: int): value to check whether the list contains
#
# Example:
# list_contains([8,4,1,3], 1) should return True.
# list_contains([8,4,1,3], 6) should return False.
#
# NOTE: you are NOT allowed to use while-loops or for-loops in your solution
# (which means you'll have to use recursion).
def list_contains(l, value):
  if len(l) == 1:
    # Our base case is when `l` only has one element. In this case, we can
    # just check whether that element is equal to `value`.
    return l[0] == value

  # The idea here is that if `l` contains `value` then either
  # - `value` is at index 0 (i.e. the element at index in `l` is equal to
  #   `value`), or
  # - `value` is at some index in the rest of the list (i.e. indices 1,2,3,...)
  #
  # First, we will check if the first element in `l` (i.e. the element
  # at index 0) is equal to `value`. If so, we can immediately return True
  # (because we have found what we were looking for).
  if l[0] == value:
    return True

  # If the first element in `l` (i.e. the element at index 0) is not equal to
  # `value`, then we need to check whether the rest of the list (i.e. indices 1
  # and on) contains `value`. We can do this with a recursive call.
  return list_contains(l[1:], value)


# This should print True.
print(list_contains([8,4,1,3], 1))

# This should print False.
print(list_contains([8,4,1,3], 6))
