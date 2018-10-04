
# Returns the sum of the numbers in the specified list.
#
# Arguments:
# l (type: list of ints): the list of numbers to sum
#
# Example:
# sum_of_list([1,4,3]) should return 8 (i.e. 1 + 4 + 3)
def sum_of_list(l):
  pass # TODO: remove this placeholder, and write the function!


# This should print 8
print(sum_of_list([1, 4, 3]))



# Given a dictionary whose values are lists of ints, return a new dictionary
# whose keys are the same, and whose values are the sums of the corresponding
# values in the original dictionary.
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
  pass # TODO: remove this placeholder, and write the function!


# This should print {"a": 8, "b": 4}
print(sum_dict_values({"a": [1,2,5], "b": [4]}))
