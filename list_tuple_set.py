# List, Tuples and Sets


# 
#
# ---------------------list[]---------------------
# 
# 

sem1_courses = ['C programming', 'Matheamtical Statistics', 'Discrete Mathematics', 'ODE', 'Group Thoery', 'Real Analysis']
print(sem1_courses)
print(sem1_courses[1])
print(sem1_courses[-1])
print(len(sem1_courses))
#add an element in the list
# sem1_courses.append("SPSS Statistics")
# print(sem1_courses)
# add items from another list to this list
stats_lab = ['SPSS Statistics']
sem1_courses.append(stats_lab) #this will add the list itself but this is not we want
print(sem1_courses)
sem1_courses.pop()
print(sem1_courses)
print('Communicative English' in sem1_courses)
sem1_courses.append("Communicative English")
print(sem1_courses)
# we want to add the elements of another list
# we use extend method for that
sem1_courses.extend(stats_lab)
print(sem1_courses) 
# remove an element from the list
sem1_courses.remove("SPSS Statistics")
print(sem1_courses)
# add an element at a specific index in the list, we use insert method
sem1_courses.insert(2, "SPSS Statistics")
print(sem1_courses)
sem1_courses.reverse()
print(sem1_courses)
# sorting alphabetically
sem1_courses.sort()
print(sem1_courses)
# sem1_courses.sort(reverse = True)
# print(sem1_courses)
# without altering the list, we can use the sorted function to get a sorted vrsion of the list
sem1_sorted = sorted(sem1_courses)
print(sem1_sorted)
course_codes = [111, 109, 107, 105, 101, 103, 113]
print(course_codes)
# without altering the list, we can use the sorted function to get a sorted vrsion of the list
sorted_codes = sorted(course_codes)
print(sorted_codes)
course_codes.sort(reverse = True)
print(course_codes)
print(min(course_codes))
print(max(course_codes))
print(sum(course_codes))
print(113 in course_codes)


# 
#
# ---------------------tuple()---------------------
# 
# 

#tuples are immutable unlike lists which are mutable, it means that
#we can't remove, insert, append etc in tuple

courses_sem1 = ('C programming', 'Matheamtical Statistics', 'Discrete Mathematics', 'ODE', 'Group Thoery', 'Real Analysis')

semester1 = courses_sem1

print(courses_sem1)
print(semester1)

# courses_sem1[3] = "Ordinary Differential Eqn"

# print(courses_sem1)
# print(semester1)
#so, you see we can't replace items in tuple


# 
#
# ---------------------sets{}---------------------
# 
# 

#all set operations
core_courses = {'Mathematics Statistics', 'Discrete Mathematics', 'ODE', 'Group Thoery', 'Real Analysis'}
print(core_courses) #set does not care about order

print("Mathematics Statistics" in core_courses)

technical_courses = {'C programming', 'SPSS Statistics'}

sem1 = core_courses.union(technical_courses)
print(sem1)
print(core_courses.intersection(technical_courses))
print(core_courses.difference(technical_courses))



# Empty sets, tuples, and sets

# lists
empty_list = [] # or
empt_list = list()

#tuples
empty_tuple = ()
empt_tuple = tuple()

# but we cannot do the same for sets

#sets

empty_set = {} #this is not correct! It is a dict. 
# we use built-in set class for empty set
empt_set = set()