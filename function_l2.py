# def mylen(seq):
#     c = 0
#     for _ in seq:
#         c = c +1
#     return c
# print(mylen([1,2,3,[1,2,3]]))
#-------------------------------------------------
# def smallest_num(s1, s2, s3):
#     return min(s1, s2, s3)
# #print(smallest_num(5, 8, 6))
# print(smallest_num('arpit', 'aarpit', 'brpit'))  # Will take as ASCII

#------------------------------------------------

# def string_reverse(str1):
#     rstr = ''
#     index = len(str1)
#     while index > 0:
#         rstr += str1[index-1]  # ?
#         index = index - 1
#     return rstr                     # return would be part of while loop.
# print(string_reverse("1234abcd"))
#

# def check(x):
#     if x < 5:
#         x = 5
#     if x%2 == 0:
#         print(x, 'is even')
#     else:
#         print(x, 'is odd')
# x=4
# check(x)

# def print_str(x, y):
#     for i in range(y):
#         print(x)
# z = 3
# print(print_str('Greetings', z))
#---------------------------------------
# def square(x):
#     print('Square is:')
#     return x*x
# def g(y):
#     print('g')
#     return y+3
# print(square(g(2)))
#---------------------------------------
def winner(names):
    temp = names[0]
    names[0] = names[-1]
    names[-1] = temp
    return names
r = ['tom', 'jeery', 'spike']
print(winner(r))