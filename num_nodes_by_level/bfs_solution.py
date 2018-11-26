# This defines the TreeNode class, so that we can create TreeNode objects.
#
# Recall that TreeNode objects should have three fields:
# - value: the value associated with this particular node (for simplicity, let's
#          assume it's always an int).
# - left: the left child of this node (or None)
# - right: the right child of this node (or None)
class TreeNode(object):
  pass

# As we discussed, we'll just use lists to implement the queues that we'll use
# for BFS (even though it's not very efficient, it should make PythonTutor
# easier to follow).

def queue_pop(queue):
  # Don't worry about how this code works; just trust that it does what it's
  # supposed to (removes and return the first element in `queue`, which is a
  # list).
  return queue.pop(0)

def queue_push(queue, element):
  # Unlike `queue_pop`, this one should be understandable; recall the `queue`
  # is a list.
  queue.append(element)

# Given a binary tree, returns a list of ints, where the elements in the
# returned list correspond to the number of nodes in each "level" (i.e.
# horizontal row) of the tree.
#
# Arguments:
# root_node (type: TreeNode): the root node of a binary tree (NOTE: not
#                             necessarily a binary search tree!)
#
# Example: if the variable root_node refers to the root of the following tree:
#
#          5
#         / \
#        8   9
#       / \   \
#      3  10   6
#
# num_nodes_in_tree(root_node) should return [1, 2, 3], since the levels/rows
# of the tree are:
# row 0: 5        (1 node)
# row 1: 8, 9     (2 nodes)
# row 2: 3, 10, 6 (3 nodes)
def num_nodes_by_level(root_node):
  # List of number of nodes in each. We will append more values to this list as
  # we conduct BFS; at any given point, it will contain the number of nodes for
  # the levels that we've finished, and the level we're currently working on.
  # Initially, we're working on level-0, which has 1 node (just the root node).
  num_nodes = [1]
  # This is the queue of nodes we need to visit (recall that we are
  # implementing queues using lists in this problem, so we just create a new
  # list). Initially, we need to visit `root_node`.
  nodes_to_visit = [root_node]
  # The number of yet-to-be-visited nodes remaining in the current level. Right
  # now, we're visiting level-0, and there is 1 to-be-visited node (the root
  # node).
  num_nodes_remaining_in_current_level = 1

  while len(nodes_to_visit) > 0:
    if num_nodes_remaining_in_current_level == 0:
      # If `num_nodes_remaining_in_current_level` is 0, then there are no more
      # remaining nodes to be visited on the current level, and we are about to
      # move onto the next level.  At this point, we know that the
      # `nodes_to_visit` queue contains all of the nodes in the next level (and
      # nothing else). Thus, the length of the queue equals the number of nodes
      # in the next level.
      #
      # We therefore both append the queue's length to `num_nodes`, and set
      # `num_nodes_remaining_in_current_level` to the queue's length (we have
      # not yet visited any of the nodes in the next level, so all of the nodes
      # in the next level are yet-to-be-visited at this point).
      num_nodes.append(len(nodes_to_visit))
      num_nodes_remaining_in_current_level = len(nodes_to_visit)

    # Typical BFS; pop the next node to visit from the queue, and push its
    # children (if any) to the queue.
    node = queue_pop(nodes_to_visit)
    if node.left != None:
      queue_push(nodes_to_visit, node.left)
    if node.right != None:
      queue_push(nodes_to_visit, node.right)

    # We've finished visiting `node`, so we decrease
    # `num_nodes_remaining_in_current_level` by 1.
    num_nodes_remaining_in_current_level = num_nodes_remaining_in_current_level - 1

  # `nodes_to_visit` is empty, thus we've finished visiting all of the nodes.
  # At this point, we can return `num_nodes`.
  return num_nodes


# Define the tree from the example above.
root_node = TreeNode()
root_node.value = 5
root_node.left = TreeNode()
root_node.right = TreeNode()

root_node.left.value = 8
root_node.left.left = TreeNode()
root_node.left.right = TreeNode()

root_node.left.left.value = 3
root_node.left.left.left = None
root_node.left.left.right = None

root_node.left.right.value = 10
root_node.left.right.left = None
root_node.left.right.right = None

root_node.right.value = 9
root_node.right.left = None
root_node.right.right = TreeNode()

root_node.right.right.value = 6
root_node.right.right.left = None
root_node.right.right.right = None

# This should print [1, 2, 3].
print(num_nodes_by_level(root_node))
