# See https://leetcode.com/problems/island-perimeter/. Note that when it says
# "two-dimensional integer grid", it just means a list of list of ints (where
# each "inner" list has the same length).
#
# Arguments:
# l (type: list of list of ints): As described in the link above. To reiterate,
#   each element of `l` (which is itself a list of ints) has the same length as
#   the other elements of `l` (which are also lists of ints).
#
# Example: see the link above.
def island_perimeter(l):
  num_rows = len(l)
  # Since each element of `l` has the same length, we'll just use the length of
  # the first (i.e. at index 0) element.
  num_columns = len(l[0])

  # First, figure out the number of vertical edges in the island's perimeter.
  # We will move (horizontally) across each row, and when we notice that the
  # "terrain" (i.e. water vs. land) changes, we know that the edge between
  # those to square is part of the perimeter.
  num_vertical_edges = 0
  row_index = 0
  while row_index < num_rows:
    # The index of the column we are currently at in the row we are moving
    # through.
    column_index = 0
    # `previous_terrain` stores the terrain (i.e. 0 for water, 1 for land) of
    # the previous square we visited. We initialize it 0, because the island is
    # "surrounded by water" (conceptually, there is only water past the left
    # edge of the grid).
    previous_terrain = 0
    while column_index < num_columns:
      current_terrain = l[row_index][column_index]
      # If the terrain has switched between the previous and current square,
      # the edge between those squares is part of the island's perimeter, so
      # increment `num_veritcal_edges` accordingly.
      if current_terrain != previous_terrain:
        num_vertical_edges = num_vertical_edges + 1

      # Update `column_index` and `previous_terrain` for the next iteration of
      # the loop.
      column_index = column_index + 1
      previous_terrain = current_terrain

    # If the last (i.e. rightmost) square of a row is land (i.e. 1), then the
    # right edge of that square is part of the island's perimeter, so we
    # increment `num_vertical_edges` to account for this edge.
    if previous_terrain == 1:
      num_vertical_edges = num_vertical_edges + 1

    # Increment `row_index`, so that we move onto the next row.
    row_index = row_index + 1

  # We can do something similar to figure out the number of horizontal edges in
  # the island's perimeter; we'll move (vertically) along each column, and keep
  # track of when the terrain changes.
  num_horizontal_edges = 0
  column_index = 0
  while column_index < num_columns:
    # The index of the row we are currently at in the column we are moving
    # through.
    row_index = 0
    previous_terrain = 0
    while row_index < num_rows:
      current_terrain = l[row_index][column_index]
      if current_terrain != previous_terrain:
        num_horizontal_edges = num_horizontal_edges + 1
      # Update `row_index` and `previous_terrain` for the next iteration of
      # the loop.
      row_index = row_index + 1
      previous_terrain = current_terrain

    # If the last (i.e. bottom) square of a column is land (i.e. 1), then the
    # bottom edge of the square is part of the island's perimeter, so we
    # increment `num_horizontal_edges` to account for this edge.
    if previous_terrain == 1:
      num_horizontal_edges = num_horizontal_edges + 1

    # Increment `column_index`, so that we move onto the next column.
    column_index = column_index + 1

  # Since every edge in the island's perimeter is either vertical or
  # horizontal, we can add the number of vertical and horizontal edges to get
  # the total number of edges.
  return num_vertical_edges + num_horizontal_edges


l = [[0,1,0,0],
     [1,1,1,0],
     [0,1,0,0],
     [1,1,0,0]]
# This should print 16
print(island_perimeter(l))
