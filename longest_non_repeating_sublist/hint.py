## HINT 0

# For this problem, we'll need an efficient way of storing what elements are
# contained in a sublist, and checking whether adding another element to the
# sublist will introduce a duplicate (i.e. whether the to-be-added element is
# already contained in the sublist). What data structure would be a good choice
# here?


## HINT 1

# One possible (albeit inefficient) solution would be the following:
#
# - For each possible starting index (i.e. 0, 1, ...), consider a sublist that
# starts at that index. Figure out how long a sublist starting at the index can
# go until increasing the end index any further would introduce a duplicate
# element. As you go along, keep track of the "best" (i.e.  longest) sublist
# you've seen so far.
#
# The inefficient solution for described above is similar to the inefficient
# solution we saw to the "sublist whose sum is target" problem we worked on
# in-person.
#
# Compare the efficient solution to the "sublist-with-sum" problem to the
# inefficient solution to the "sublist-with-sum" problem. Is there something
# similar we could do for this problem?
