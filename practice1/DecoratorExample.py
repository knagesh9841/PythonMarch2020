from practice2.ModuleExample import div

# Decorator is used to change the Behavior of Existing Function written by Other user


def outer_decorator(func):

    def inner_decorator(a, b):
        if a < b:                       # This will do Modification and call func i.e . div Function
            a, b = b, a
        func(a, b)

    return inner_decorator      # Second It will Return inner_decorator


div = outer_decorator(div)    # It will Execute First and it will call outer_decorator function

div(2, 4)                   # This will call inner_decorator Function
