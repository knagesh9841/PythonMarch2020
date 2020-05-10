# Function return more than 1 value


def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d


result1, result2 = add_sub(10, 5)

print("Addition", result1)
print("Subtraction", result2)


# Arbitrary Arguments, *args args is of Type Tuple

"""
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, and can access the items accordingly

"""


def arbitary_args(x, *args):
    print(x)
    print(type(args))
    for i in args:
        print(i)


arbitary_args(10, 20, 30)


"""
Keyword Arguments
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter

"""


def keyword_args(name, age, address):
    print("Name = "+name)
    print("Age = ", age)
    print("Address = "+address)


keyword_args(age=30, name="Nagesh", address="Latur")


"""
Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

This way the function will receive a dictionary of arguments, and can access the items accordingly

"""


def arbitary_keyword_args(**args):
    for k, v in args.items():
        print(k+"="+v)


arbitary_keyword_args(name="Nagesh", address="Latur")
arbitary_keyword_args()


"""
Default Parameter Value
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value

"""


def default_args(country="India"):
    print("Country = "+country)


default_args()
default_args("Bharat")


"""
Passing a List as an Argument
You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function

"""


def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# Pass statement in Function


def pass_function():
    pass

# Global Variable


a = 10
b = 20
c = 30


def global_var():
    a = 100
    global b        # We can declare Local variable as Global using global Keyword
    b = 200
    print("Local a = ", a)
    print("Local b= ", b)
    print("Global c= ", c)
    globals()['c'] = 300    # it  is used to access Global Variable
    print("Global c= ", c)


global_var()
print("Global a = ", a)
print("Global b= ", b)
print("Global c= ", c)
