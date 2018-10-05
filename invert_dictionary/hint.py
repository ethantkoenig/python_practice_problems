# This might be a little tricky to follow, because the values in the original
# dictionary are the same as the keys of the new dictionary. I have annotated
# the below hints with examples corresponding to the invert_dictionary({10:0,
# 11:1, 12:0}) example.

# Try to do the following:
#   - start with an empty dictionary; we will build this dictionary to
#   eventually become the "new" dictionary we return
#   - iterate over the keys of the original dictionary (i.e. d)
#     - for each key in the original dictionary (e.g. 10), figure out what the
#     associated value in the original dictionary is for that key (e.g. 0).
#     - we will want to add the original value (e.g. 0) as a key to our new
#     dictionary; there are two cases to consider:
#       - Case 0: The original value (e.g. 0) is not currently a key of the
#       new dictionary.  In this case, we will need to add the original value
#       (e.g. 0) as key in the new dictionary; what should the associated
#       value (in the new dictionary) be for this key (e.g. 0)? Recall that
#       values (in the new dictionary) are lists of keys (from the original
#       dictionary).
#       -  Case 1: The original value (e.g. 0) is already a key of the new
#       dictionary In this case, we will need to update the value (in the new
#       dictionary) associated with this key (e.g. 0). Recall that values (in
#       the new dictionary) are lists of keys (from the original dictionary).
