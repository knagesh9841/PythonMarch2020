
"""
Create a dictionary, using the List items as keys. This will automatically remove any duplicates
because dictionaries cannot have duplicate keys.

Then, convert the dictionary back into a list:

"""

MyList = ["a", "b", "a", "c", "c"]
MyList = list(dict.fromkeys(MyList))
print(MyList)

# Convert it into Set

MyList = ["a", "b", "a", "c", "c"]

MyList = set(MyList)

print(MyList)

