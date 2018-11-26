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
# either a (male) actor or a (female) actress.
#
# In a population of actors, each of whom is given a unique (int) identifier,
# each actor has collaborated with some of their peers.
#
# You are given a dictionary, whose keys are the (identifiers of) the
# actors, and the value associated with a particular key is the list
# of (identifiers of) peers the actor has collaborated with.
#
# Given (the identifiers of) two actors, find the minimum degree of separation
# between them.
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
  # We will perform breadth-first-search on the graph, keeping track of the
  # degree-of-separation of the node (i.e. actor) we're visiting. Recall that
  # the main difference between doing BFS on a graph vs. on a tree is that the
  # graph may contain cycles, so we need to keep track of which nodes we've
  # already encountered (so we don't accidentally revisit them).

  # `encountered` is a dictionary whose keys are the ids of the actors we've
  # encountered so far. The values don't matter, so we'll just use None.
  encountered = {a: None}
  # `actors_to_visit` is a queue of actors that we have to visit.
  # However, instead of just storing the actor's id in the queue, we
  # will also store the actor's degree-of-separation from `a` in the
  # queue. This means that each element in the queue will itself be a list of
  # length 2, with the actor's id at index 0, and the actor's
  # degree-of-separation at index 1.
  actors_to_visit = []
  # Initially, `actors_to_visit` should contain `a`, who has a
  # degree-of-separation of 0.
  queue_push(actors_to_visit, [a, 0])

  while len(actors_to_visit) > 0:
    # Pop the next actor to visit. Recall that popped_list is a list containing
    # the actor's id, and the actor's degree-of-separation.
    popped_list = queue_pop(actors_to_visit)
    current_actor_id = popped_list[0]
    current_actor_degree_of_separation = popped_list[1]

    if current_actor_id == b:
      # If the current actor is `b`, then we are done searching, and can return
      # the current actor's degree-of-separation.
      return current_actor_degree_of_separation

    # Recall that `collaborators_for_current_actor` is a list of the ids of the
    # actors that `current_actor` has collaborated with.
    collaborators_for_current_actor = collaborators[current_actor_id]

    # For each collaborator of the current actor, add that collaborator to
    # `actors_to_visit`, unless we've already encountered the collaborator
    # before
    collaborator_index = 0
    while collaborator_index < len(collaborators_for_current_actor):
      collaborator_id = collaborators_for_current_actor[collaborator_index]
      if not (collaborator_id in encountered):
        # If we have not encoutered a collaborator yet, then that collaborator's
        # degree-of-separation is 1 greater than the current actor's
        # degree-of-separation.
        queue_push(actors_to_visit, [collaborator_id, current_actor_degree_of_separation + 1])
        # Mark the collaborator as encountered, so that we don't accidentally
        # add it to `actors_to_visit` again.
        encountered[collaborator_id] = None
      collaborator_index = collaborator_index + 1

  # If we reach this point, `actors_to_visit` is empty, and there's nothing left
  # to search. While doing BFS, we never visited `b`, so `a` and `b` are not
  # connected, in which case we should return None.
  return None


# This should print 3
print(degree_of_separation({
  0:[1],
  1:[0,2,3],
  2:[1,3],
  3:[1,2,4],
  4:[3]
}, 0, 4))
