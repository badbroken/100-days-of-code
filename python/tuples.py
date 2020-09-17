# What are Tuples? A tuple is a data structure allows us to store multiple types of datas inside of it. a lot like a
# list, but tuple is immutable

my_info = ('Mike', 24, 'Programmer')
print(my_info)

# extracting information

print(my_info[0])
print(my_info[-1])

# error in the code below, tuple doesnt support assignment, re-order ; in short any sort of mutation
# my_info[0] = 'Miachel'

# Unpacking a tuple.
name, age, occupation = my_info
print(name)
print(age)
print(occupation)

# creating one element tuple
one_element_tuple = (4,)
print(one_element_tuple)

# Where tuples come in handy?
# Storing different types of data where it's meant to be together and not get changed.
