# The first thing to notice is the population of actors, together with the
# collaborations between actors, forms a graph. The nodes of this graph are the
# actors, and there is an edge between two actors if those two actors have
# collaborated with each other.
#
# We can perform breadth-first-search on this graph, starting at `a`, and going
# until we reach `b` (or until there's nothing left to search). As we perform
# breadth-first-search, we will need some way of keeping track of the
# degree-of-separation between `a` and the node we're currently visiting.
#
# Recall that when we're doing BFS on an arbitrary graph (as opposed to a tree),
# we need to do an extra check to make sure we don't revisit nodes we've already
# encountered. What data structure should we use for storing the nodes that
# we've already encountered?
#
# If you get stuck, take a look at the BFS-based solution to num_nodes_by_level;
# there are some similarities between this problem and that problem.
