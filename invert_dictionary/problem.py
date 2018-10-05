
# Given a dictionary, return a new dictionary whose keys are the values of the
# original dictionary, and the values (in the new dictionary) of those keys are
# a list of keys (from the original dictionary) that were associated with that
# value. (See the example below if this explanation wasn't clear).
#
# Arguments:
# original_dictionary (type: dict of int to int): the dictionary to invert
#
# Example:
# invert_dictionary({10:0, 11:1, 12:0}) should return {0: [10, 12], 1:[11]}. The keys
# of the returned dictionary (0 and 1) match the values of the original
# dictionary, and for each key in the returned dictionary (e.g. 0), the
# corresponding value is the list of keys in the original dictionary that were
# associated with that value (e.g. 10 and 12 were the keys in the original
# dictionary that had an associated value of 0).
def invert_dictionary(original_dictionary):
  pass # TODO: remove this placeholder, and write the function!


# This should print {0: [10, 12], 1:[11]}
print(invert_dictionary({10:0, 11:1, 12:0}))
