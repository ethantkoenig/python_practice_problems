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
# TODO: return None if not connected
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
  pass # TODO: remove this placeholder, and write the function!


# This should print 3
print(degree_of_separation({
  0:[1],
  1:[0,2,3],
  2:[1,3],
  3:[1,2,4],
  4:[3]
}, 0, 4))
