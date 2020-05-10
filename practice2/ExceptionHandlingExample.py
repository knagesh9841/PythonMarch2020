"""
Compile time error
Logical error
Run time error

The try block lets you test a block of code for errors.

The except block lets you handle the error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

In python, you can also use else clause on try-except block which must be present after all the except clauses.
The code enters the else block only if the try clause does not raise an exception.

"""

# it won't Throw Error when we call Exception first and then Other Exception

try:
    a = 2
    b = int(input("Enter Value of B "))
    c = a/b
except Exception as e:
    print("Exception is Occurred ", e)
except ZeroDivisionError as e:
    print("Exception is Occurred 'ZeroDivisionError' ", e)
except ValueError as e:
    print("Exception is Occurred 'ValueError' ", e)
else:
    print("Else Block is Called")
finally:
    print("Finally Block is called")


# Program to handle multiple errors with one except statement

try:
    a = 2
    b = 0
    c = a/b
except(ZeroDivisionError, NameError, IndexError):
    print("Exception Occurred")
finally:
    print("Finally block Is called")


"""
Raising Exception:
The raise statement allows the programmer to force a specific exception to occur. The sole argument in raise indicates 
the exception to be raised. This must be either an exception instance or an exception class 
(a class that derives from Exception).
"""


try:
    raise Exception("Sorry, no numbers below zero")
except Exception as e:
    print("User Raised Exception Occurred", e)


# User-defined Exceptions in Python with Examples

"""
Programmers may name their own exceptions by creating a new exception class. Exceptions need to be derived from the 
Exception class, either directly or indirectly. Although not mandatory, most of the exceptions are named as names that 
end in “Error” similar to naming of the standard exceptions in python
"""


# A python program to create user-defined exception

# class MyError is derived from super class Exception

class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise(MyError(3*2))

# Value of Exception is stored in error
except MyError as error:
    print('A New Exception occurred: ', error.value)
