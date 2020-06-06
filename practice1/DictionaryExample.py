from collections import defaultdict

MyDict = {}  # Empty Dictionary
print(MyDict)
print(type(MyDict))

MyDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

# Access the value of Dictionary

print(MyDict["brand"])
print(MyDict["model"])

print(MyDict.get("brand"))  # get method with Key return value associated with it
print(MyDict.get("model"))

# Update value of Dictionary

MyDict["year"] = "2020"

print(MyDict)

"""
Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well

"""

for x in MyDict:
    print("Key:- " + x + " Values:- " + MyDict.get(x))

# You can also use the values() function to return values of a dictionary

for x in MyDict.values():
    print(x)

# Loop through both keys and values, by using the items() function

for x, y in MyDict.items():
    print(x + " " + y)

# Keys method return keys

for x in MyDict.keys():
    print(x)

# We can set Different type of key and values in dictionary

diifkeydict = {"brand": "Ford", 1: "Bappa"}

for x in diifkeydict:
    print("Values:- ", diifkeydict.get(x))

# Check if Key Exists

if "brand" in MyDict:
    print("'brand' key is in Dictionary")

if "Brand" not in MyDict:
    print("'Brand' Key is Not present in Dictionary")

print(len(MyDict))  # Length of Dictionary

# Adding an item to the dictionary is done by using a new index key and assigning a value to it

MyDict["Name"] = "Nagesh"
print(MyDict)

# The pop() method removes the item with the specified key name

MyDict.pop("Name")  # Removed specified Key and associated value from Dictionary
print(MyDict)

MyDict.popitem()  # The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead)
print(MyDict)

# The del keyword removes the item with the specified key name

del MyDict["brand"]
print(MyDict)

del MyDict  # The del keyword can also delete the dictionary completely

MyDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

# The clear() method empties the dictionary

MyDict.clear()
print(MyDict)

# Copy Dictionary

MyDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

CopyDict = MyDict.copy()
print(CopyDict)

# Dictionary will return None when Key is not present
# We can change Message

var = CopyDict.get(1, "Not Found")
print(var)

# Create Dictionary from List

KeysList = [1, 2, 3]
ValuesList = ["Nagesh", "Mahadev", "Kadam"]

MyDict = dict(zip(KeysList, ValuesList))

print(MyDict)

# Create a dictionary that contain three dictionaries

MyDict = myfamily = {
    "child1": {
        "name": "Emil",
        "year": "2004"
    },
    "child2": {
        "name": "Tobias",
        "year": "2007"
    },
    "child3": {
        "name": "Linus",
        "year": "2011"
    }
}

for keys, values in MyDict.items():
    for x in values:
        print(keys+" "+x+" "+values.get(x))


"""
Defaultdict is a container like dictionaries present in the module collections. Defaultdict is a sub-class of the 
dict class that returns a dictionary-like object. The functionality of both dictionaries and defualtdict are almost same 
except for the fact that defualtdict never raises a KeyError. It provides a default value for the key that does not 
exists
"""


def def_value():
    return "Not Present"


# Defining the dict
d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])


"""
Merging Two Dictionary
Using the method update()
By using the method update() in Python, one list can be merged into another. 
But in this, the second list is merged into the first list and no new list is created. It returns None.
Example:
"""

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

# This return None
print(dict2.update(dict1))

# changes made in dict2
print(dict2)


"""
Merging Two Dictionary 
Using ** in Python
"""

dict1 = {'a': 10, 'b': 8}
dict2 = {'d': 6, 'c': 4}

dict3 = {**dict1, **dict2}

print(dict3)


# Dictionary Comprehensions

input_list = [1, 2, 3, 4, 5, 6, 7]

dict_using_comp = {var: var ** 3 for var in input_list if var % 2 != 0}

print("Output Dictionary using dictionary comprehensions:",
      dict_using_comp)

state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']

output_dict = {}

state = ['Gujarat', 'Maharashtra', 'Rajasthan']
capital = ['Gandhinagar', 'Mumbai', 'Jaipur']

dict_using_comp = {key: value for (key, value) in zip(state, capital)}

print("Output Dictionary using dictionary comprehensions:",
      dict_using_comp)

