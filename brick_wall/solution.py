

# See https://leetcode.com/problems/brick-wall/description/.
#
# Returns the numbers of bricks "crossed" by the vertical that crosses the
# fewest number of bricks.
#
# Arguments:
# bricks: (type: list of list of ints): each element in `bricks` (which is
# itself a list of ints) represents the widths of the bricks in one row of our
# hypothetical brick wall.
#
# Example:
# See the example at https://leetcode.com/problems/brick-wall/description/.
def brick_wall(bricks):
  # The key insight here is that finding the line that crosses the fewest number
  # of bricks is equivalent to finding the line that goes along the most number
  # of brick edges. This is because when any vertical line passes through a row
  # of bricks, the line with either cross a brick, or pass along a brick edge.
  #
  # It is easier (and more efficient) to keep track of where the brick edges
  # occur than to keep track of where they don't occur (i.e. where
  # "brick-crossings" happen).

  # `numbers_of_edges` will be a dictionary, whose keys will be the position of
  # a prospective line, and the corresponding value will be the number of rows
  # for which that line goes along the edge of a brick (as opposed to crossing a
  # brick).
  number_of_edges = {}

  # Iterate over each row of bricks.
  row_index = 0
  while row_index < len(bricks):
    # Recall that `row_of_bricks` is itself a list of ints.
    row_of_bricks = bricks[row_index]
    # For each brick in this row, we will figure where the position at which the
    # "right" edge of that brick lies, and will update `numbers_of_edges`.
    #
    # However, we ignore the rightmost brick (i.e. the last element in
    # `row_of_bricks`), because the right edge of the rightmost brick is the
    # right edge of the entire wall.
    brick_index = 0
    # `right_edge_position` stores the position of the right edge of the current
    # brick.
    right_edge_position = 0
    while brick_index < len(row_of_bricks) - 1:
      brick_width = row_of_bricks[brick_index]
      # Add `brick_width` to `right_edge_position`, to account for the width of
      # the current brick.
      right_edge_position = right_edge_position + brick_width
      if not (right_edge_position in number_of_edges):
        number_of_edges[right_edge_position] = 1
      else:
        number_of_edges[right_edge_position] = number_of_edges[right_edge_position] + 1

      # Increment `brick_index`, so that we move onto the next brick in this row.
      brick_index = brick_index + 1

    # Increment `row_index`, so that we move onto the next row of bricks.
    row_index = row_index + 1

  # Now, we will figure out how many edges the "best" vertical line goes along.
  # We will use `most_edges` to keep track of the best line we've found so far.
  most_edges = 0
  # Recall that this will iterate over each key in `numbers_of_edges` (in no
  # particuar order). Each iteration, the `position` variable will be set to one
  # of the keys in `numbers_of_edges`
  for position in number_of_edges:
    # If the number of edges at this position is better than anything we've seen
    # so far, update `most_edges` accordingly.
    if number_of_edges[position] > most_edges:
      most_edges = number_of_edges[position]

  # Now that we've iterated through `numbers_of_edges`, we know that the "best"
  # line goes along `most_edges` edges. Equivalently, the "best" line crosses
  # `len(bricks) - most_edges` bricks, since the total number of rows is
  # `len(bricks)`.
  return len(bricks) - most_edges


# This should print 2. I've added extra spaces to the list so that the "bricks" are
# aligned.
print(brick_wall([[1,2  ,2  ,1],
                  [3    ,1,2  ],
                  [1,3    ,2  ],
                  [2  ,4      ],
                  [3    ,1,2  ],
                  [1,3    ,1,1]]))
