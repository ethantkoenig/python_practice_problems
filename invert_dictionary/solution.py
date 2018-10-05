
# Given a dictionary, return a new dictionary whose keys are the values of the
# original dictionary, and the values (in the new dictionary) of those keys are
# a list of keys (from the original dictionary) that were associated with that
# value. (See the example below if this explanation wasn't clear).
#
# Arguments:
# d (type: dict of int to int): the dictionary to invert
#
# Example:
# invert_dictionary({10:0, 11:1, 12:0}) should return {0: [10, 12], 1:[11]}. The keys
# of the returned dictionary (0 and 1) match the values of the original
# dictionary, and for each key in the returned dictionary (e.g. 0), the
# corresponding value is the list of keys in the original dictionary that were
# associated with that value (e.g. 10 and 12 were the keys in the original
# dictionary that had an associated value of 0).
def invert_dictionary(original_dictionary):
  # new_dictionary is a variable for the new dictionary we will be building.
  # Right now, it's empty.
  new_dictionary = {}

  # Iterate over the keys in `original_dictionary`, and for each key+value in
  # the original dictionary, update `new_dictionary` accordingly.
  for original_key in original_dictionary:
    # Get the value associated with `original_key` in the original_dictionary.
    original_value = original_dictionary[original_key]

    if not(original_value in new_dictionary):
      # If `original_value` is not currently a key in `new_dictionary`, we add
      # it as a key, and set the corresponding value to a list containing
      # `original_key`.
      new_dictionary[original_value] = [original_key]
    else:
      # Otherwise, if `original_value` is already a key in `new_dictionary`,
      # then its corresponding value is a list of keys from the original
      # dictionary. In this case, we want to append `original_key` to that list.
      new_dictionary[original_value].append(original_key)

  # Now that we've iterated over every key in `original_dictionary`,
  # `new_dictionary` is complete, and we can return it.
  return new_dictionary


# This should print {0: [10, 12], 1:[11]}
print(invert_dictionary({10:0, 11:1, 12:0}))
