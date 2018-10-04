
# Returns the sum of the numbers in the specified list.
#
# Arguments:
# l (type: list of ints): the list of numbers to sum
#
# Example:
# sum_of_list([1,4,3]) should return 8 (i.e. 1 + 4 + 3)
def sum_of_list(l):
  # This variable will keep track of the sum of the elements we have seen so
  # far. Right now, we have not seen any elements at all yet, so we set it to 0.
  sum_so_far = 0

  for element_of_l in l:
    # Recall that for each iteration of this for loop, the element_of_l variable
    # will be set to a particular element of l.
    #
    # Note: I chose to call the loop variable element_of_l solely to make the
    # code easier for humans to read and understand. The fact that element_of_l
    # will be set to the elements of l has everything to do with the fact that
    # this is a for loop (and that's what for loops do), and nothing to do with
    # the particular name I chose for the loop variable (Python does not know
    # English!).
    #
    # Update sum_so_far to account for the current element
    sum_so_far = sum_so_far + element_of_l

  # Now that we've gone over all of the elements of l, the sum_so_far is the sum
  # of all elements of l, and therefore we can return it.
  return sum_so_far


# This should print 8
print(sum_of_list([1, 4, 3]))



# Given a dictionary whose values are lists of ints, return a new dictionary
# whose keys are the same, and whose values are the sums of the corresponding
# values in the original dictionary. (If this isn't clear, hopefully the example
# below will help.)
#
# Arguments:
# d (type: dictionary whose values are lists of ints): dictionary
#
# Example:
# sum_dict_values({"a": [1,2,5], "b": [4]}) should return {"a": 8, "b": 4}. Note
# that the keys in the returned dictionary are the same as the keys in the
# original dictionary, and that the new value for a particular key (e.g. "a") is
# the sum of the elements in the original value for that key (e.g. the new
# value for "a" is 8, which is the sum of [1, 2, 5], the original value for "a").
#
# Hint: use the sum_of_list function you wrote above!
def sum_dict_values(d):
  # new_dictionary is a variable for the new dictionary we will be building.
  # Right now, it's empty.
  new_dictionary = {}

  # Iterate over the keys in the original dictionary (i.e. d), and for each key,
  # figure out what the corresponding value for that key should be in the new
  # dictionary, and add the respective key+value entry to the new dictionary.
  for key in d:
    # Recall that the values of the original dictionary (i.e. d) are lists of
    # ints, so the original_value variable will refer to a list of ints.
    original_value = d[key]

    # Fortunately, we already have a convenient way for getting the sum of a
    # list of ints, so we might as well reuse the sum_of_list function we wrote
    # above!
    new_dictionary[key] = sum_of_list(original_value)

  # Now that we've iterated over every key in the original dictionary, we've
  # added every key+value entry to the new dictionary, and we can return
  # new_dictionary.
  return new_dictionary


# This should print {"a": 8, "b": 4}
print(sum_dict_values({"a": [1,2,5], "b": [4]}))
