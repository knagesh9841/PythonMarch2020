"""
Generator-Function :

If the body of a def contains yield, the function automatically becomes a generator function.

Generator-Object :

Generator functions return a generator object. Generator objects are used either by calling the next method on the
generator object or using the generator object in a “for in” loop.

Yield suspend the execution of function (till next Yield)it won't terminate the execution of function like return

"""


def fibo(limit):
    a, b = 0, 1

    while limit >= 1:
        yield a
        c = a + b
        a = b
        b = c
        limit -= 1


x = fibo(10)

for i in x:
    print(i)
