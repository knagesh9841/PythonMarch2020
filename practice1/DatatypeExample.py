import random

"""
This is Example for DataType in python
None: When Empty variable
Numeric:
int
float
complex
bool:
Str(String):
List(Sequence):
Tuple(Sequence):
Set(Sequence):
Range(Sequence):
Dictionary:

"""

x = 5  # int
print(x)
x = 5.14  # Float
print(x)
x = 5 + 6j  # Complex
print(x)
print(type(x))  # DataType of Variable
x = 'DataType'  # Str
print(x)
x = list(range(1, 10, 2))  # range and list
print(x)
x = True  # bool
print(x)

x = int(5.14)  # This will convert to int
print(x)
x = int(True)
print(x)
x = int(False)
print(x)
x = float(5)    # This will convert to float
print(x)
x = complex(10, 20)     # This will convert to complex
print(x)
x = bool(5)     # This will convert to bool
print(x)
x = bool(0)     # This will convert to bool 0 is for false another is for True
print(x)
x = set((1, 2, 3, 4, 4))    # Set
print(x)
x = frozenset((1, 2, 3, 4, 4, 2))    # FrozenSet
print(x)
x = tuple((1, 2, 3, 3))     # Tuple
print(x)
x = dict({1: 'Nagesh', 2: "Bappa"})  # Dictionary
print(x)
x = str(2)
print(x)
print(type(x))

print(random.randrange(1, 1000))

"""
First a and b will have same value and Address
when we changed value of a  then it's value changed and Address will also change but will not change value and address of b.
same for Float,String
In case of List,Set and Dictionary Value of a changed then value and address of b remain same as a.

"""

a = 10
b = a

print(id(a))
print(id(b))

print(a)
print(b)

a = 20

print(id(a))
print(id(b))

print(a)
print(b)

# String

a = 'Nagesh'
b = a

print(id(a))
print(id(b))

print(a)
print(b)

a = 'Bappa'

print(id(a))
print(id(b))

print(a)
print(b)

# List

a = [1, 2, 3]
b = a

print(id(a))
print(id(b))

print(a)
print(b)

b.append(4)

print(id(a))
print(id(b))

print(a)
print(b)

print(not False)        # This will print True
