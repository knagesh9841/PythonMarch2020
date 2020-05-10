
Number = int(input("Enter User Input"))

if Number == 1:
    print("One")
elif Number == 2:
    print("Two")
else:
    print("Wrong Input")


# One line if statement

if Number == 1: print("One")

# One line if else statement

print("One") if Number == 1 else print("Wrong Number")


# Nested If

Number = 41

if Number > 20:
    if Number > 40:
        print("Number is Greater Than 40")
    else:
        print("Number is Greater Than 20 But Less Than 40")


"""
The pass Statement
if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
We can use it in Loop,Function and Method
"""

if Number > 20:
    pass
