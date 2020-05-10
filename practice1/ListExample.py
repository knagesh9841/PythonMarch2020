ThisList = []  # Empty List
print(ThisList)
print(bool(ThisList))  # This will return False

ThisList = ["apple", "banana", "cherry"]
print(ThisList)

print(ThisList[0])  # This will print First item in List
print(ThisList[0:2])  # This will print First and second item in List
print(ThisList[-1])  # This will print Last item in List
print(ThisList[::-1])      # This will reverse the content of List


ThisList = ["apple", "banana", "cherry"]
ThisList[1] = "blackcurrant"  # This will update List Item @ Index 1
print(ThisList)

for x in ThisList:  # Loop Through list
    print(x)

print(len(ThisList))  # Length of List

# Check if "apple" is present in the list

if "apple" in ThisList:
    print("'Apple' is present in List")
else:
    print("'apple' is Not present in List")

# Check if "Grapes" is not present in the list

if "Grapes" not in ThisList:
    print("'Grapes' is not present in List")
else:
    print("'Grapes' is present in List")

# Using the append() method to append an item

ThisList.append("Orange")

print(ThisList)

# To add an item at the specified index, use the insert() method

ThisList.insert(1, "Orange")

print(ThisList)

# The remove() method removes the specified item it will remove First Occurance

ThisList.remove("Orange")

print(ThisList)

# The pop() method removes the specified index, (or the last item if index is not specified)

ThisList = ["apple", "banana", "cherry"]
var = ThisList.pop()
print(ThisList)
print(var)

ThisList = ["apple", "banana", "cherry"]
var = ThisList.pop(1)
print(ThisList)
print(var)

# The del keyword removes the specified index

ThisList = ["apple", "banana", "cherry"]
del ThisList[0]
print(ThisList)

# The del keyword can also delete the list completely

del ThisList

# The clear() method empties the list

ThisList = ["apple", "banana", "cherry"]
ThisList.clear()
print(ThisList)

# Make a copy of a list with the copy() method

ThisList = ["apple", "banana", "cherry"]
MyList = ThisList.copy()
print(ThisList)
print(MyList)

# Make a copy of a list with the list() method

ThisList = ["apple", "banana", "cherry"]
MyList = list(ThisList)
print(MyList)

# Join two list using + Operator

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Use the extend() method to add list2 at the end of list1

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

MyList = [1, 2, 3, "Nagesh", "Kadam"]       # List with Mixed data
print(MyList)

MyList = ["Nagesh", "Nagesh", "Mahadev", "Kadam"]
print(MyList.count("Nagesh"))       # Returns the number of elements with the specified value

print(MyList.index("Nagesh"))       # Returns the index of the first element with the specified value

MyList = [10, 15, 9, 6, 30]

print(MyList[0:4:2])        # This will print 0-3rd Element and Increment index by 2

MyList.sort()               # Sorts the list

print(MyList)

MyList.reverse()            # reverse the List

print(MyList)


MyList = ["Nagesh", "Nagesh", "Mahadev", "Kadam"]

MyList.sort()               # Sorts the list

print(MyList)

# Delete multiple values from List and add multiple values to List

del MyList[2:]

print(MyList)

MyList = [10, 15, 9, 6, 30]

MyList.extend([1, 4, 35, 29])

print(MyList)

print(sum(MyList))  # Sum
print(min(MyList))  # Min
print(max(MyList))  # Max

print(MyList.__getitem__(1))  # Return Item @ Index

MyList1 = [1, 2, 3]
MyList2 = ["Nagesh", "Kadam"]

MyList = [MyList1, MyList2]     # List in List

print(MyList)


"""
List comprehension is an elegant way to define and create list in python. 
We can create lists just like mathematical statements and in one line only.
"""

# below list contains square of all odd numbers from
# range 1 to 10
odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
print(odd_square)

"""
odd_square = [] 
for x in range(1, 11): 
    if x % 2 == 1: 
        odd_square.append(x**2) 
print(odd_square)
"""