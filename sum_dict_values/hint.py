# Hints for sum_of_list:
# Try to do the following:
# - keep a variable for the "running total" of the elements you've seen so far.
# - iterate over each element of l, and update your "running total" variable
#   accordingly
# - once you've iterated over every of element of l, return your "running
#   total".

# Hints for sum_dict_values:
# Since the keys of the new dictionary (i.e. the dictionary you'll return) are
# the same as the key of the original dictionary, we'll probably need to
# iterate over the (keys of the) original dictionary.
#
# Try to do the following:
# - start with an empty dictionary; we will build this dictionary to eventually
#   become the "new" dictionary we return
# - iterate over the keys of the original dictionary (i.e. d)
#   - for each key in the original dictionary, figure out what the corresponding
#   value in the original dictionary is for that key, then use that original
#   value to figure out what the corresponding value in the new dictionary
#   should be for that key.
#   - add the key and corresponding new-value to the "new" dictionary
# - return the "new" dictionary
