# we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.

def fact(x):
    if x == 1:
        return 1
    else:
        return (x * fact(x-1))

x = 3
print('Factorial of' x 'is' fact(x-1))




