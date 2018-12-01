
def queue_pop(queue):
  # Don't worry about how this code works; just trust that it does what it's
  # supposed to (removes and return the first element in `queue`, which is a
  # list).
  return queue.pop(0)

def queue_push(queue, element):
  # Unlike `queue_pop`, this one should be understandable; recall that `queue`
  # is a list.
  queue.append(element)

# Given a directed graph, and two nodes in the graph, find the shortest path
# between the two nodes.
#
# Arguments:
# graph (type: dict of int to list of ints): dictionary from an
#   node to that course's prerequisites peers that the actor has collaborated with
# start_node (type: int): node to start at
# end_node (type: int): node to end at
#
# Returns (type: list of ints): a list consisting of the nodes on the path from
# `start_node` to `end_node`.
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
  # Queue of nodes to visit.
  nodes_to_visit = [start_node]
  # Dictionary whose keys are the nodes we've encountered. The value of a key
  # will be the "previous" node (i.e. the node we were visiting when we first
  # encountered the node). In the case of `start_node`, there is no previous
  # node, so we'll just use None.
  encountered = {start_node: None}
  # Note: in this code, we end up doing BFS on the entire graph, but if we
  # wanted to, we could stop as soon as we encounter `end_node`.
  while len(nodes_to_visit) > 0:
    node = queue_pop(nodes_to_visit)
    neighbors = graph[node]
    index = 0
    while index < len(neighbors):
      neighbor = neighbors[index]
      if not(neighbor in encountered):
        encountered[neighbor] = node
        queue_push(nodes_to_visit, neighbor)
      index = index + 1

  if not (end_node in encountered):
    # If we never encountered `end_node`, then there is no path from
    # `start_node` to `end_node`.
    return None

  # Build the path backwards, starting at `end_node` and repeatedly looking at
  # the previous node until we hit the `start_node`.
  reverse_path = []
  current_node = end_node
  while current_node != start_node:
    reverse_path.append(current_node)
    current_node = encountered[current_node]

  # Now build the forwards path, which starts at `start_node` (note that we
  # never actually added `start_node` to `reverse_path`), and then consists of
  # `reverse_path` in reverse order.
  forward_path = [start_node]
  # Since we want traverse reverse_path backwards, we start at the last index
  # (i.e. `len(reverse_path) - 1`), and repeatedly decrement `index`.
  index = len(reverse_path) - 1
  while index >= 0:
    forward_path.append(reverse_path[index])
    index = index - 1

  return forward_path


# This should print [0, 1, 3, 4]
print(shortest_path({
  0:[1,2],
  1:[2,3],
  2:[1],
  3:[4],
  4:[0]
}, 0, 4))
