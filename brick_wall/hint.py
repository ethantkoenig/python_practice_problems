
# First, let introduce some conventions for describing the positions of possible
# lines.
#
# In the following example (which would be represented by [[1, 2, 1], [2, 2]]):
#
# positions: 0   1   2   3   4
#            +---+-------+---+
#            | 1 |   2   | 1 |
#            +---+---+---+---+
#            |   2   |   2   |
#            +-------+-------+
#
# Positions 0 and 4 would correspond to drawing a line along the left or right edge
# of the entire wall (respectively), which is not allowed! So in this example,
# the valid, possible lines are at positions 1, 2, and 3.
#
# In general, the position of a valid line has to be (strictly) greater than 0,
# and (strictly) less than the width of the entire wall.

# One possible approach is to consider each possible line, and to figure out how
# many bricks that line crosses. As we consider more possible lines, we will
# keep track of the "best" line we've seen so far (i.e. the one that crossed the
# fewest number of bricks).
#
# This would work, but would be rather inefficient. First, we would consider
# drawing our line at position 1, and would have to look at each row of bricks
# to determine whether a line at position 1 crosses a brick in that row. Then,
# we would consider drawing our line at position 2, and again would have to look
# at each row of bricks to determine whether a line at 2 crosses a brick in that
# rows. And so on...
#
# This means that for each possible line (which is roughly equal to the width of
# the entire wall), we have to iterate over each row. So for any given row, we
# have to look at that row many times. Can you think of way to solve the problem
# where you only need to look at each row only once?
