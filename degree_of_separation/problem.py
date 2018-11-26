# You might want to use a queue to solve this problem. Let's just use lists to
# implements queues (even though it's not very efficient, it should make
# PythonTutor easier to follow).

def queue_pop(queue):
  # Don't worry about how this code works; just trust that it does what it's
  # supposed to (removes and return the first element in `queue`, which is a
  # list).
  return queue.pop(0)

def queue_push(queue, element):
  # Unlike `queue_pop`, this one should be understandable; recall that `queue`
  # is a list.
  queue.append(element)

# Inspired by https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon.
#
# NOTE: For the sake of conciseness, I will use the term "actor" to refer to
# either a (male) actor or a (female) actress. I apologize for the patriarchal
# nomenclature :P
#
# In a population of actors, each of whom is given a unique (int) identifier,
# each actor has collaborated with some of their peers.
#
# You are given a dictionary, whose keys are the (identifiers of) the
# actors, and the value associated with a particular key is the list
# of (identifiers of) peers the actor has collaborated with.
#
# Given (the identifiers of) two actors, find the degree-of-separation between
# them.
#
# Arguments:
# collaborators (type: dict of int to list of ints): dictionary from an
#   actor to the peers that the actor has collaborated with
# a (type: int): the identifier of an actor
# b (type: int): the identifier of another actor
#
# Returns (type: int): the degree of separation between `a` and `b`. Returns
# None if `a` and `b` are not connected at all.
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
