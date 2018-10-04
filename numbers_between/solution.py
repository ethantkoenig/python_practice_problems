
# Returns a list of ints containing the numbers between the specified
# (inclusive) start and (exclusive) end.
#
# Arguments:
# inclusive_start (type: int): the inclusive start of the sequence
# exclusive_end (type: int): the exclusive upper-bound of the sequence
#
# Example:
# numbers_between(3, 7) should return [3, 4, 5, 6]; note that the
# inclusive_start argument (3) is included, and the exclusive_end argument (7)
# is excluded.
def numbers_between(inclusive_start, exclusive_end):
  # This list will contain the numbers we have added so far, right now it's
  # empty because we haven't added anything yet.
  numbers_so_far = []
  # This is the next number we will add to the list. It is initially inclusive_start.
  next_number_to_append = inclusive_start

  # We want to keep going until the next number we are about to add to our the
  # list (i.e. next_number_to_append) has reached exclusive end. Equivalently,
  # we want to keep going while next_number_to_append is less than
  # exclusive_end.
  while next_number_to_append < exclusive_end:
    # Append next_number_to_append to our list.
    numbers_so_far.append(next_number_to_append)
    # Now that we've appended next_number_to_append, we update the variable to be
    # one greater than its previous value.
    next_number_to_append = next_number_to_append + 1

  # At this point, we've appended all of the numbers we need to append to
  # numbers_so_far, so numbers_so_far contains the final result, and we can
  # return it.
  return numbers_so_far


# This should print [3, 4, 5, 6]
print(numbers_between(3, 7))
