import sys

sys.setrecursionlimit(200)          # This will set Recursion limit
print(sys.getrecursionlimit())      # this will print recursion limit


# This will calculate Factorial of Given Number


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


print("Factorial = ", fact(5))
