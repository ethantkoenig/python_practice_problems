
# Returns a list of the numbers between the minimum and maximum value of `l`
# which are not present in `l`.
#
# Arguments:
# l (type: list of ints): list of ints, not necessarily sorted. You may assume
# the list is not empty (i.e. has a length of at least 1).
#
# Example:
# missing_from_range([7,2,8,4]) should return [3,5,6], because the numbers
# between the list's minimum (i.e. 2) and maximum (i.e. 8) which are not in list
# are 3, 5, and 6.
def missing_from_range(l):
  # We will iterate through the list, and keep track of the minimum and maximum
  # element we've encountered so far. Initially, the first element (i.e. the
  # element at index 0) is both the smallest and largest thing we've seen so
  # far.
  min_element = l[0]
  max_element = l[0]
  # We will also keep a hashtable whose keys are the elements of `l` that we've
  # encountered. The values don't matter, so we will just use None (recall that
  # None is a "placeholder" of sorts). Initially, we've only seen the element at
  # index 0.
  elements_of_l = {l[0]: None}

  index = 1
  while index < len(l):
    element = l[index]
    if element < min_element:
      min_element = element
    if element > max_element:
      max_element = element
    elements_of_l[element] = None

    index = index + 1

  # Now that we've gone through the entire list, `min_element` and `max_element`
  # contains the minimum and maximum of the entire list, respectively.
  # Similarly, `elements_of_l` contains every element of `l` as a key.

  # We will check each number between the minimum (i.e. `min_element`) and
  # maximum (i.e. `max_element`), and each number that is not in `l` (or
  # equivalently, is not a key in `elements_of_l`), we will append to a list.
  missing_numbers = []
  # We already know that `min_element` appears in `l`, so we can start with
  # `min_element + 1`.
  number_to_check = min_element + 1
  # Similarly, we know that `max_element` appears in `l`, so we can stop once we
  # reach `max_element`.
  while number_to_check < max_element:
    if not (number_to_check in elements_of_l):
      missing_numbers.append(number_to_check)
    number_to_check = number_to_check + 1

  return missing_numbers


# This should print [3, 5, 6]
print(missing_from_range([7, 2, 8, 4]))

# This should print []
print(missing_from_range([4, 2, 5, 3]))
