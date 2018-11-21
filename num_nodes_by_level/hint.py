# As we've done for other tree problems, consider the four possible cases:
# - no left nor right child
# - left child, but no right child
# - right child, but no left child
# - both a left and right child
#
# For each case, consider what (if any) recursive calls you would make in that
# case. In cases where you are making recursive calls, recall that each such
# recursive call will return a list of ints; think about how you can use this
# list to produce the list you ultimately want to return.

# If you're feeling ambitious, remember that when we were working on previous
# tree problems (e.g. finding the maximum value in a tree), going case-by-case
# through the four cases (as described above) yielded a perfectly fine
# solution, but there sometimes was a slightly more slick solution, and you
# wanted a methodology for coming up with such solutions (which I was
# unfortunately unable to provide).
#
# There also exists a similar type of solution to this problem (it's the one
# I've written in solution.py), and it could be a good exercise to try to think
# of what the solution would be. If you're stuck, try looking at the solutions
# to the "maximum elements in a tree" and "number of nodes in a tree" problems
# for inspiration.
