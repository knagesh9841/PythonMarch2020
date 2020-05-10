import os

"""
The join() method is a string method and returns a string in which
the elements of sequence have been joined by str separator.

string_name.join(iterable)

string_name: It is the name of string in which
             joined elements of iterable will be
             stored.

Parameters: The join() method takes iterable – objects capable of returning its members one at a time. Some examples are List, Tuple, String, Dictionary and Set



Return Value: The join() method returns a string concatenated with the elements of iterable.

"""

if os.path.exists("abc.txt"):
    os.remove("abc.txt")  # Delete File
    print("File Deleted")

FileObj = open("abc.txt", "x")
FileObj = open("abc.txt", "w")
FileObj.write("Nagesh Mahadev Kadam\n")

FileObj = open("abc.txt", "r")

MyLine = FileObj.readline()

MyLine.strip()
MyWord = MyLine.split()     # This will Split into Word

Reversed = " ".join(MyWord[::-1])

print("reversed ", Reversed)

# reversed  Kadam Mahadev Nagesh
