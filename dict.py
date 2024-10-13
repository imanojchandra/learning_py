# dictionaries allow us to work with key-value pairs

# key-value pair means these are two different likned values
# where the KEY is a unique identifier where we can find our data
# and the VALUE is that data. 

the_uk = {'name': 'Jessica', 'age': 24, 'qualifications': ['Bachelor in Event Management', 'Masters in Data Science'], 'place': 'Richmond, UK'}

print(the_uk)
print(the_uk['name']) #passes the value of the 'name' key
print(the_uk['qualifications']) 


# get method
print(the_uk.get('place'))
print(the_uk.get('amino'))
print(the_uk.get('Relationship Status', 'No Info'))

the_uk['phone'] = '+44 20 XXXX XXXX'
the_uk['name'] = 'Jess Bean'
print(the_uk)
print(len(the_uk))
print(the_uk.keys())
print(the_uk.values())
print(the_uk.items())
the_uk.update({'name':'Jess', 'phone': '+44 X0 XXXX XXX0'})
print(the_uk)

# del the_uk['phone']
phn = the_uk.pop('phone')
print(phn)
print(the_uk)

# loop through the dict

for key in the_uk:
    print(key) #this is not we want in dict

# we want both keys and values 
for key, value in the_uk.items():
    print(key, value)
    # print(key,":", value)