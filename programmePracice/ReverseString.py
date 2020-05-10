
"""
There is no built-in function to reverse a String in Python.

The fastest (and easiest?) way is to use a slice that steps backwards, -1.

Create a slice that starts at the end of the string, and moves backwards.

In this particular example, the slice statement [::-1] means start at the end of the string and end at position 0,
move with the step -1, negative one, which means one step backwards.

"""

Text = "Nagesh Kadam"

print(Text[::-1])

# We can also Reverse List

MyList = ['Nagesh', 'Mahadev', 'Kadam']

Reversed = MyList[::-1]

print(Reversed)