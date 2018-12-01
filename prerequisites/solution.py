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

# There are a collection of courses, each of which is given a unique (int)
# identifier. Each course has some number (possibly zero) of prerequisite
# courses. Students are not allowed to take a course until they have completed
# all of the course's prerequisites (i.e. you can not take a course and it's
# prerequisite during the same semester).
#
# Your are an incoming freshman, and there is a particular course which sounds
# interesting, and you want to plan your schedule for the upcoming semesters so
# that you can take that course as soon as possible (without breaking the
# prerequisite rule). You can't be bothered to take any course that don't
# (directly or indirectly) help you complete the prerequisites for the
# interesting course.
#
# You are given a dictionary, whose keys are the (identifiers of) the
# courses, and the value associated with a particular key is the list
# of (identifiers of) courses that are prerequisites for that course. If a
# course has no prerequisities, then the corresponding list will be empty.
#
# Given (the identifiers of) this particularly interesting course, return a
# lists with the courses you should take your first semester.
#
# Arguments:
# prereqs (type: dict of int to list of ints): dictionary from an
#   courses to that course's prerequisites peers that the actor has collaborated with
# interesting_course (type: int): the course you want to take
#
# Returns (type: list of ints): the courses you should take your first semester
# (this list can be in any order).
#
# Example:
# first_semester_courses({
#   0:[],
#   1:[],
#   2:[],
#   3:[0],
#   4:[2,3],
#   5:[3]
# }, 4) should return [0,2], since you should take courses 0 and 2 your first
# semester. You can't take courses 3 or 4, since you don't have the prereqs, and
# you don't bother taking courses 1 or 5, since they don't help you to eventually take
# course 4 (the interesting course).
def first_semester_courses(prereqs, interesting_course):
  # Queue of courses to visit. We could just as well use a stack here (i.e. use
  # DFS instead of BFS).
  courses_to_visit = [interesting_course]
  # Dictionary whose keys are the courses we've encountered so far (values are
  # just None).
  encountered_courses = {interesting_course: None}
  courses_to_take_first_semester = []
  while len(courses_to_visit) > 0:
    course = queue_pop(courses_to_visit)
    course_prereqs = prereqs[course]
    if len(course_prereqs) == 0:
      # The course we're currently visiting does not have any prerequisites, so
      # we can take it in our first semester. The course is also useful in
      # helping us ultimately take the interesting course (because uninteresting
      # courses will never be visited).
      courses_to_take_first_semester.append(course)
    index = 0
    while index < len(course_prereqs):
      prereq = course_prereqs[index]
      if not (prereq in encountered_courses):
        encountered_courses[prereq] = None
        queue_push(courses_to_visit, prereq)
      index = index + 1

  return courses_to_take_first_semester


# This should print [0, 2] (order doesn't matter))
print(first_semester_courses({
  0:[],
  1:[],
  2:[],
  3:[0,2],
  4:[2,3],
  5:[3]
}, 4))
