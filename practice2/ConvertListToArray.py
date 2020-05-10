import numpy

# Convert Python List to numpy Arrays

MyList = ['Nagesh', 'Mahadev', 'Kadam']
arr = numpy.array(MyList)
print("List: ", MyList)
print("Array: ", arr)

MyList = ['Nagesh', 'Mahadev', 'Kadam']
arr = numpy.asarray(MyList)
print("List: ", MyList)
print("Array: ", arr)

"""
The vital difference between the above two methods is that numpy.array() will make a duplicate of the original object 
and numpy.asarray() would mirror the changes in the original object.

"""