from numpy import *

# array is used to create Only single Dimensional Array but numpy is used to create Multi Dimensional Array

MyArray = array([1, 2, 3, 4])

for cnt in MyArray:
    print(cnt)

MyArray = MyArray + 5       # Add 5 to each Value of Array

for cnt in MyArray:
    print(cnt)

MyArray = MyArray * 5        # Multiply 5 to each value of array

for cnt in MyArray:
    print(cnt)

print(sum(MyArray))         # Sum of array similarly we can use min, max, avg function


"""
Arr1 = Arr2
Then it will Assign to same memory Location
"""

MyArray = array(['Nagesh', 'Mahadev', 'Kadam'])

"""
This is Shallowcopy when we changed Element of one array then it will affect other Array and memory location is different
"""

ShallowCopy = MyArray.view()

ShallowCopy[0] = "Bappa"


for cnt in MyArray:
    print(cnt)

for cnt in ShallowCopy:
    print(cnt)

print(id(MyArray))
print(id(ShallowCopy))

"""
copy Method is used for Deep Copy.
Memory Location is different.
When Element of One Array changed then it won't affect Other Array 
"""
MyArray = array(['Nagesh', 'Mahadev', 'Kadam'])

DeepCopy = MyArray.copy()

DeepCopy[0] = "Bappa"


for cnt in MyArray:
    print(cnt)

for cnt in DeepCopy:
    print(cnt)

print(id(MyArray))
print(id(DeepCopy))


# Matrix

MyArray = array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(MyArray.ndim)     # This will print no of Dimension
print(MyArray.shape)    # No OF Dimension and size of each Array
print(MyArray.size)     # Size of Array

i = 0

while i < len(MyArray):
    j = 0
    while j < len(MyArray[i]):
        print(MyArray[i][j], end=" ")
        j += 1
    print()
    i += 1

