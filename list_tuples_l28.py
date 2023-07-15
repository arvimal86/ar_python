# Difference in + and append on iterable objets
'''
x = ['a', 'b']
y = [1, 2, 3]
print(len(x + y))
#x.append(y)
#print(x)
#y.append(x)
#print(y)
x.extend(y)
print(x)
'''

# Append - Adds a single element
# Extend - expand individual elements
# insert - insert whole element at the position of first index.

# Tuples
# Immutables and enclosed in ()
'''
t = ('a', 'b', 'c', 'd', 'e', 'f')
print(t)
print(t[::-1])
print(t)
'''
# Default response as tuple
'''
a = 'Arpit'
b = 10
c = [1,2,3]
print(a,b,c)
'''
# Assignment & Packaging
'''
(s1, s2, s3, s4) = ('a', 'b', 'c', 'd')
print(s1)
print(s2)
print(s3)
print(s4)
'''

# Magic Swap
'''
a = 1
b = 2
a, b = b, a
print(a)
print(b)
'''

# Why we use tuple instead of a list
# 1. Program execution is faster when manipulating
# 2. Safeguard accidental changes when not intended.
'''
a = 20
b = 5.5
c = 3 + 2j
d = 'Hello'
l = [a, b, c, d]
print(l)   # 3+2j will be marked as tuple
# problem

print(l.append(100).insert(2, [1, 'India', [25, [min, 'Apple']]]).extend([1, 2, 3]))
len(l)

'''

# it will none type of object.

# insert() Parameters
# The insert() method takes two parameters:
# index - the index where the element needs to be inserted
# element - this is the element to be inserted in the list
'''
vowel = ['a', 'e', 'i', 'u']
vowel.insert(3, 'o')
print(vowel)

'''


# How to access Apple
'''
l = [20,
    5.5,
    [1, 'India', [25, [min, 'Apple']]],
    (3 + 2j),
    'Hello',
    100,
    1,
    2,
    3]
print(l[2][2][1])
'''




