import os

"""
We use open () function in Python to open a file in read or write mode

“ r “, Read - Default value. Opens a file for reading, error if the file does not exist.
“ w “, Write - Opens a file for writing, creates the file if it does not exist.
“ a “, Append - Opens a file for appending, creates the file if it does not exist.
“ r+ “, for both reading and writing
" x ", Create - Creates the specified file, returns an error if the file exists
" t " - Text - Default value. Text mode
" b " - Binary - Binary mode (e.g. images)
" rb ", Reading Binary
" wb ", writing Binary

readlines() is used to read all the lines at a single go and then return them as each line a string element in a list.
This function can be used for small files, as it reads the whole file content to the memory,
then split it into separate lines. We can iterate over the list and strip the newline '\n'
character using strip() function.

Using readline()
readline() function reads a line of the file and return it in the form of the string. It takes a parameter n,
which specifies the maximum number of bytes that will be read. However, does not reads more than one line,
even if n exceeds the length of the line. It will be efficient when reading a large file because instead of fetching all
the data in one go, it fetches line by line. readline() returns the next line of the file which contains a
newline character in the end. Also, if end of the file is reached, it will return an empty string.

"""

try:
    if os.path.exists("abc.txt"):
        os.remove("abc.txt")            # Delete File
        print("File Deleted")

    FileObj = open("abc.txt", "x")
    FileObj = open("abc.txt", "w")
    FileObj.write("Nagesh Mahadev Kadam\n")
    FileObj.writelines("This is the write command\n")
    FileObj.writelines("It allows us to write in a particular file\n")
    FileObj = open("abc.txt", "a")
    FileObj.writelines("This is Appending\n")

    FileObj = open("abc.txt", "r")

    readData = FileObj.read()       # This Will Read all file data @Time
    print(readData)

    FileObj = open("abc.txt", "r")

    Lines = FileObj.readlines()

    count = 1
    for line in Lines:
        line = line.strip()
        line = line.strip()
        print("Line{}: {}".format(count, line))
        count += 1

    FileObj = open("abc.txt", "r")

    count = 0

    while True:
        line = FileObj.readline()
        if not line:
            break
        line = line.strip()
        line = line.strip()
        print("Line{}: {}".format(count, line))
        count += 1

except Exception as e:
    print("Exception is Occurred", e)
finally:
    FileObj.close()
    print("File is Closed")

"""
We can use with statement in Python such that we don’t have to close the file handler. The with statement 
creates a context manager and it will automatically close the file handler for you when you are done with it.
"""

print("With statement")
count = 0

with open("abc.txt", "r") as readfile:
    while True:
        line = readfile.readline()
        if not line:
            break
        line = line.strip()
        line = line.strip()
        print("Line{}: {}".format(count, line))
        count += 1

