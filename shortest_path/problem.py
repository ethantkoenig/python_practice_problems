# Given a directed graph, and two nodes in the graph, find the shortest path
# between the two nodes.
#
# Arguments:
# graph (type: dict of int to list of ints): dictionary from an
#   node to that course's prerequisites peers that the actor has collaborated with
# start_node (type: int): node to start at
# end_node (type: int): node to end at
#
# Returns (type: list of ints): a list consisting of the nodes on the shortest
# path from `start_node` to `end_node`. Return None if there is no such path
# (i.e. if `start_node` and `end_node` are not connected).
#
# Example:
# shortest_path({
#   0:[1],
#   1:[2,3],
#   2:[1,3],
#   3:[4],
#   4:[0]
#  }, 0, 4) should return [0,1,3,4].
def shortest_path(graph, start_node, end_node):
  pass # TODO: remove this placeholder, and write the function!


# This should print [0, 1, 3, 4]
print(shortest_path({
  0:[1,2],
  1:[2,3],
  2:[1],
  3:[4],
  4:[0]
}, 0, 4))
