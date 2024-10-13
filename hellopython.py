#this is a single line comment

'''
This is multi-line comment
Use either triple double quotes or triple single quotes for multi-line comments in Python.

In this program, I'm learning to use Python for arithmatic calculations, and how to
work with texts and lists.
'''

print("Hello Python!")

print(5 + 6)
print((50 - 5*6) / 4)
print(17 / 3)  # classic division returns a float/floating-point number
print(17 // 3)  # floor division discards the fractional part
print(17%3) # the % operator returns the remainder of the division
print(5 ** 2, 2**7) # sqaure of 5, 2 to the power of 7
print(8 > 9)
print(round(9.1))
print(round(5.4567, 2))
print(round(5.4567, 1))

n1 = '100'
n2 = "200"

n1 = int(n1)
n2 = int(n2)
print (n1 + n2)


#variables
# area of rectangle
width = 20
height = 5
area = width * height
print(area)

# In python, operators with mixed type operands convert the integer operand to floating point:

#area of circle
r = 20 # you must assign a value to a var, in this r, if but you r undefined, you get error 
#  _ is also a variable in python
# _ = 3.14 * r ** 2
# print(_)
circle_area = 3.14 * r ** 2
print (circle_area)
areaofCircle = 3.14 * r * r
print (areaofCircle)

print("Text")
double_quote = "This is a string using double quote."
single_quote = 'This is a single quote string.'
print(double_quote, single_quote)

#how to write "I am" as I'm 

in_dble = "It's double quote"
in_single = 'It\'s in single quote' #you add a back-slash before ' to use it in single quote

print(in_dble)
print(in_single)

print('Didn\'t they say that?')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')

new_line = 'First line.\nSecond line.'  # \n means newline

print(new_line)

# raw string
# If you don’t want characters prefaced by \ to be interpreted as special characters, 
# you can use raw strings by adding an r before the first quote

print('C:\some\name') # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

# Strings can be concatenated with the + operator, and repeated with *:
str1 = "hell"
str2 = 'o'
str3 = "Python"

hello_python = str1 + 5 * str2 + " " + str3
print(hello_python)

text = ('Put several strings within parentheses ''to have them joined together.')
print(text)


word = "indexingANDslising"
at_position_0 = word[0]
at_index_8 = word[8]
print(at_position_0)
print(at_index_8)
print(word[-1])

print(word[0:5])
print(word[:11])
print(word[-10:-7])



slice1 = word[0:5]
slice2 = word[5:8]
slice3 = word[8:11]
slice4 = word[-7:]


the_word = slice1 + slice2 + slice3 + slice4
print(the_word)

t = '%s has %d melons.' % ('Maria', 2)
print(t)


# instead of adding them like this. you can actually use f-string method

name = 'Manoj'

intr = f"He said his name is {name}"
intr1 = f"\nHe said his name is {name!r} or {repr(name)}"
print(intr, intr1)

a = 2
print(f"abc {a} xyz")

greeting = "Hello"
name = "Python"
msg1 = "{}, {}. Welcome to Programming!".format(greeting, name)
print(msg1)

msg2 = f"{greeting} {name}. Welcome to Programming!"
print(msg2)

msg = f"{greeting.lower()} {name.upper()}. Welcome to Programming!"
print(msg)


# 
# 


