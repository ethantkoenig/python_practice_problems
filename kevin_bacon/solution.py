# Inspired by https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon.
#
# In a population of actors/actresses, each of whom is given a unique (int)
# identifier, each actor/actress has collaborated with some of their peers.
#
# You are given a dictionary, whose keys are the (identifiers of) the
# actors/actresses, and the value associated with a particular key is the list
# of (identifiers of) peers the actor/actresses has collaborated.
#
# Given (the identifiers of) two actors/actresses, find the minimum degree of
# separation between them.
#
# Arguments:
# collaborators (type: dict of int to list of ints): dictionary from an
#   actor/actress to the peers that the actor/actress has collaborated with
# a (type: int): the identifier of an actor/actress
# b (type: int): the identifier of another actor/actress
#
# Returns (type: int): the degree of separation between `a` and `b`.
#
# Example:
# degree_of_separation({
#   0:[1],
#   1:[0,2,3],
#   2:[1,3],
#   3:[1,2,4],
#   4:[3]
# }, 0, 4) should return 3 (0 has collaborated with 1, who has collaborated
# with 3, who has collaborated with 4).
def degree_of_separation(collaborators, a, b):
  # `encountered` is a dictionary whose keys are the actors/actresses we've
  # encountered so far. The values don't matter, so we'll just use None.
  encountered = {a: None}
  degree = 0
  frontier = [a]
  while len(frontier) > 0:
    next_frontier = []
    frontier_index = 0
    while frontier_index < len(frontier):
      actor = frontier[frontier_index]
      if actor == b:
        return degree
      peers = collaborators[actor]
      peer_index = 0
      while peer_index < len(peers):
        peer = peers[peer_index]
        if not (peer in encountered):
          next_frontier.append(peer)
          encountered[peer] = None
        peer_index = peer_index + 1
      frontier_index = frontier_index + 1
    frontier = next_frontier
    degree = degree + 1
  return None


# This should print 3
print(degree_of_separation({
  0:[1],
  1:[0,2,3],
  2:[1,3],
  3:[1,2,4],
  4:[3]
}, 0, 4))
