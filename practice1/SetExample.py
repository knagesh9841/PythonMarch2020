MySet = {}          # Empty Dictionary it is not Empty set
print(MySet)
print(type(MySet))

MySet = {"apple", "banana", "cherry"}
print(MySet)

# Loop for Set element access

for x in MySet:
    print(x)

if "apple" in MySet:
    print("Yes, 'apple' is in the fruits Set")

if "Grapes" not in MySet:
    print("'Grapes' is not Fruit Set")

"""
Change Items
Once a set is created, you cannot change its items, but you can add new items

"""

MySet.add("Orange")     # To add one item to a set use the add() method
print(MySet)

MySet.update(["Orange", "mango", "grapes"])     # To add more than 1 Item

print(MySet)

print(len(MySet))       # Length of Set

"""
Remove Item
To remove an item in a set, use the remove(), or the discard() method
Note: If the item to remove does not exist, remove() will raise an error
Note: If the item to remove does not exist, discard() will NOT raise an error.
"""

MySet.remove("banana")
print(MySet)

MySet.discard("banana")
print(MySet)

var = MySet.pop()   # This will remove Last item from Set
print(var)
print(MySet)

MySet.clear()       # Clear The Sets
print(MySet)

del MySet           # Delete the Set

MySet = {1, 2, 3}
CopySet = MySet.copy()
print(CopySet)


# Frozenset

# Since frozenset object are immutable they are mainly used as key in dictionary or elements of other sets

MyList = [1, 2, 3]
FrozenSet = frozenset(MyList)
print(FrozenSet)

for x in FrozenSet:
    print(x)


# Set Comprehensions:
# Set comprehensions are pretty similar to list comprehensions.
# The only difference between them is that set comprehensions use curly brackets { }

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]

set_using_comp = {var for var in input_list if var % 2 == 0}

print("Output Set using set comprehensions:",
      set_using_comp)
