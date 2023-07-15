# lists are mutable
# Elements can be add, delete and shift
'''
x = ['a', 'b', 'c', 'd', 'e', 'f']
print(x[2])
print(x[-1])
print(x[1:4])
x[2] = 10
x[-1] = 20
x[1:4] = [1, 2, 3, 4, 5, 6, 7, 8]
print(x[2])
print(x[-1])
print(x)
'''
# How many elements are present in the list post these commands
'''
x = ['a', 'b', 'c', 'd', 'e', 'f']
#x[1] = [1, 2, 3, 4, 5] # will take one element as nested element
print(len(x))
print(x)
x[1:4] = [1, 2, 3, 4, 5] # range will take individual elements 
print(len(x))
print(x)
'''
# Prepending and appending (adding element start and end of my list)

x = ['a', 'b', 'c', 'd', 'e', 'f']
# add new multiple elements
#x += ['j', 'k']
#print(x)
#x = [1, 2] + x
#print(x)
# add new single element
x += 'game'
print(x)
x += [20]  # can not add numeric single object values ex. x = +20, it should be in scalar like list []
print(x)



