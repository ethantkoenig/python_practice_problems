
# Since your solution is going to involve recursion, first think about what your
# base case should be. Once you figure out the base case (both the condition for
# checking whether you are in the base case, and what you need to do if you are
# in fact in the base case), then think about the recursive (i.e. non-base) case.
#
# Since several of the list-related recursion problems we've covered so far
# (e.g. merge sort) have involved making recursive calls on the first and second
# halves of the original list, that might have been your first instinct. That
# approach will work here, but instead of thinking about splitting the original
# list into two equal halves, let's think about splitting it into the first
# element (i.e. the element at index 0) and everything else (i.e. indices 1 and
# on).
#
# The "first piece" (i.e. just the element at index 0) is easy enough to handle;
# we can check whether the element at index 0 is equal to the sought-after
# value.
#
# The "second piece" (i.e. everything in the original list from index 1 onwards)
# is itself a list, and it's (strictly) shorter than the original list (because
# it has one less element). Suppose we knew whether this "second piece" contains
# the sought-after value or not (along with the result of the check we did for
# the "first piece"); how could we use this info to determine whether the
# original list contains the sought-after value?
#
# As you may have guessed, we will need to make a recursive call to figure out
# whether the "second piece" contains the sought-after value or not.
