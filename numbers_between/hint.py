
# Try to do the following:
# - start with an empty list
# - repeatedly append numbers to this list, starting at inclusive_start and
#   stopping once you reach exclusive_end
# - return the list
#
# As you can (hopefully) guess, this will involve some sort of loop. Ask
# yourself whether while or for is the better choice here.
#
# In the example when inclusive_start=3 and exclusive_end=7, we would start with
# an empty list. We would append 3 to this list, then 4, then 5, then 6. At this
# point, the list is [3, 4, 5, 6]. We would not append 7 (or anything after 7),
# because we reached exclusive_end. Now that we're done appending things to our
# list, we can return it.
