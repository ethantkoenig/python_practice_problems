# We will want to use BFS (for the same reason we used BFS instead of DFS in
# in the degree_of_separation problem).
#
# We know how to figure out the length of the shortest path between two nodes
# (using BFS), but in this problem we need to figure out what the path is (i.e.
# what nodes are on the path, not just the length of the path).
#
# Suppose we are visiting a node (let's call it N), and notice that one of N's
# neighbors is `end_node`, and that `end_node` has not been encountered yet.
# Then we know that N comes immediately before `end_node` in the shortest path.
# What node will come immediately before N in the shortest path?
