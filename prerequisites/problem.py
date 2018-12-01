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
# of (identifiers of) courses that are prerequisites for that course.
#
# Given (the identifier of) this particularly interesting course, return a lists
# with the courses you should take your first semester.
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
  pass # TODO: remove this placeholder, and write the function!


# This should print [0, 2] (order doesn't matter))
print(first_semester_courses({
  0:[],
  1:[],
  2:[],
  3:[0,2],
  4:[2,3],
  5:[3]
}, 4))
