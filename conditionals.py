# conditionals and booleans

language = "Java"

if language == "Python":
    print("Langauge is Python")
elif language == "Java":
    print("Langauge is Java")
elif language == "C++":
    print("Langauge is C++")
else:
    print("No Match")


# Boolean operations
# AND
# OR
# NOT


####-----AND-----###
user = "Admin"
logged_in = False

if user == 'Admin' and logged_in:
    print("Admin Page")
else:
    print("Access denied")

####-----OR-----###
if user =="Admin" or logged_in:
    print("Admin Page")
else:
    print("Access denied") 

####-----NOT-----###
if not logged_in:
    print("Please, Login")
else:
    print("Welcome to Admin Page")


a = [1, 2, 3]
b = [1, 2, 3]

# print(a == b) it is true because 


print(a is b) #this returns False because in memory these are two different objects
# i.e. thier location is different
print(id(a))
print(id(b))
# so, basically "a is b" means "id(a) = id(b)"