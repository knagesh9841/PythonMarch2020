ThisTuple = ()      # Empty Tuple
print(ThisTuple)
print(type(ThisTuple))

ThisTuple = ("apple", "banana", "cherry")
print(ThisTuple)

print(ThisTuple[0])  # This will print First item in Tuple
print(ThisTuple[0:2])  # This will print First and second item in Tuple
print(ThisTuple[-1])  # This will print Last item in Tuple

"""
Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

Example
Convert the tuple into a list to be able to change it

"""

ThisTuple = (1, 2, 3)
ThisList = list(ThisTuple)
ThisList.append(4)
ThisTuple = tuple(ThisList)
print(ThisTuple)

# Loop Through a Tuple

for x in ThisTuple:
    print(x)

"""
Check if Item Exists
To determine if a specified item is present in a tuple use the in keyword:

Example
Check if "apple" is present in the tuple

"""

ThisTuple = ("apple", "banana", "cherry")
if "apple" in ThisTuple:
    print("Yes, 'apple' is in the fruits tuple")

if "Grapes" not in ThisTuple:
    print("'Grapes' is not Tuple")

print(len(ThisTuple))   # Length of tuple

"""
Create Tuple With One Item
To create a tuple with only one item, you have to add a comma after the item, unless Python will not recognize the variable as a tuple.
It will treat it as str
"""

ThisTuple = ("apple",)      # This tuple
print(type(ThisTuple))

ThisTuple = ("apple")      # This str
print(type(ThisTuple))

"""
 Tuples are unchangeable, so you cannot remove items from it or add into it, but you can delete the tuple completely
 """

ThisTuple = ("apple", "banana", "cherry")
del ThisTuple


# Join Two Tuples

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

print(tuple3.count(1))      # Returns the number of times a specified value occurs in a tuple
print(tuple3.index(1))      # Searches the tuple for a specified value and returns the position of where it was found
