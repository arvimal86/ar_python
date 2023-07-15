# list and tuples
# ===============
# list is a collection of arbitrary objects, which can hold multiple data types and more flexible.
# Mutable
#  Enclosed a comma separated,  sequence of object in Square brackets - []
# Tuples:
# Tuples are identical to lists in all respects, except for the following properties
# parenthesis ()
# Tuples are immutable.
#=========================================
'''
a = ['abc', 'def', 'ghi']
print(a)                            # To view the element of list
'''

# Important characteristics of lists
# 1. lists are ordered
# 2. lists can contain any arbitrary objects (string, function, integer etc )
# 3. List can be accessed by its index
# 4. List can be Nested to arbitrary depth (nested in nested)
# 5. Lists are mutable
# 6. Lists are dynamic.

# Lists are ordered : having particular sequence
'''
a = ['abc', 'def', 'ghi', 'jkl']
b = ['ghi', 'abc', 'jkl', 'def']

print(a[0])
print(b[0])
# Since elements are same both list but not same list.
'''
# 2. Any arbitrary value : integer, string , boolean , string etc
'''
a = [1, 2, 3, 4]
print(a)
a = ['a', 'b', 'c', 'd']
print(a)
a = ['rohit', 5.2, 3, True]
print(a)
'''
# Accessed by index
# left to right : start from 0
# right to left : start from -1
# [start:end:step]
'''
a = ['a', 'b', 'c', 'd', 'e', 'f']
print(a[-5])
print(a[0:3]) #  in slicing, boundry codition will be -1
print(a[:3])
print(a[-4:-1])
# alternate number to be printed
print(a[:-1:2])
# reverse
print(a[::-1])
'''
# Nested list
# a list can contain sub lists, which in turn ca contain sub list themselves , and so on to arbitrary depth

x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']
print(x[0])
print(x[1])
print(x[1][1][0])
print(x[3])
print(x[3][0])
print(x[1][1:3])
print(x[3][::-1])
print(x[1][::-1][2][::-1][0])
print(x[1][1][-2])

# Mutable





