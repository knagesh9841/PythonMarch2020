
# Assignment Operator

x = 5

print(x)

x += 5
print(x)

# Arithmetic Operator

a = 10
b = 6
c = a + b       # Addition
print(c)
c = a - b       # Subtraction
print(c)
c = a * b       # Multiplication
print(c)
c = a / b       # Division
print(c)
c = a // b      # This is called Integer or Floor Division
print(c)
c = a ** b      # This will print a to the Power B
print(c)
c = a % b       # Modulus
print(c)

# Relation and Logical Operator

if a == b:
    print("A is Equal to B")
if a >= b:
    print("A is Greater than B")
if a <= b:
    print("A is Less Than B")
if a != b:
    print("A is Not Equal to B")

if a < 11 and b > 5:
    print("And Operator")

if a < 11 or b < 5:
    print("Or Operator")

if not a > 10:
    print("Not Operator")

"""
Python Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

is 	Returns True if both variables are the same object	x is y
is not	Returns True if both variables are not the same object

"""

x = 10
y = 10

print(x is y)   # This will return True as x and y Point to same memory location as it is having same content

x = 10
y = 11

print(x is not y)   # This will return True

"""
Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:

in 	Returns True if a sequence with the specified value is present in the object
not in	Returns True if a sequence with the specified value is not present in the object

"""


Name = "Nagesh"

print("Nag" in Name)        # Return True
print("Nag" not in Name)    # Return False

"""
Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

& 	AND	Sets each bit to 1 if both bits are 1
|	OR	Sets each bit to 1 if one of two bits is 1
 ^	XOR	Sets each bit to 1 if only one of two bits is 1
~ 	NOT	Inverts all the bits
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

"""

x = 10

print(~10)

