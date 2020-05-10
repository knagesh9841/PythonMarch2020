from array import *

MyArray = array('i', [1, 2, 3, 4, 5])

for cnt in MyArray:
    print(cnt)


MyArray.append(6)       # Append The value to Array

for cnt in MyArray:
    print(cnt)

print(MyArray.index(5))        # Return the Index of Given Value

MyArray.remove(4)       # remove the Given Value

for cnt in MyArray:
    print(cnt)

CopyArray = MyArray.__copy__()      # Copy Array

for cnt in CopyArray:
    print(cnt)

print(len(MyArray))     # Return Length of Array



