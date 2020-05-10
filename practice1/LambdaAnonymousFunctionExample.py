
# It is Function without Name

"""
lambda arguments : expression
The expression is executed and the result is returned

"""

x = lambda a: a + 10

print(x(5))

# Lambda functions can take any number of arguments

x = lambda a, b: a * b

print(x(5, 6))


"""
The power of lambda is better shown when you use them as an anonymous function inside another function.

Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number

"""


def my_function(n):
    return lambda a: a * n


mydoubler = my_function(2)

print(mydoubler(11))
