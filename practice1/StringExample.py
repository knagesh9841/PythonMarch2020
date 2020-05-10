
str1 = "Nagesh Mahadev 'Kadam'"

print(str1)

str1 = 'Nagesh mahadev "Kadam"'

print(str1)

str1 = "Nagesh" + " Kadam"

print(str1)

str1 = "Nagesh " * 10

print(str1)

str1 = "c:\docs\navin"

print(str1)

str1 = "c:\docs\\navin"  # \ is Escape character

print(str1)

print(r"c:\docs\navin")  # r is used for Raw

str1 = "Youtube"

print(str1[1:])     # this will print from 1 to End

print(str1[:])      # This will print start to end

print(str1[:10])    # This will not throw error even if 10 is out of bound

print(str1[0])

#print(str1[10])   # This throw Exception IndexError: string index out of range

print(str1[-6:-1])  # -1 is Last Element and -6 calculate in reverse direction

print(str1[-7:0])   # this will not print anything

print(str1[-7:2])

#str1[0:2] = 'My'  # This will throw Exception as TypeError: 'str' object does not support item assignment

mail = """
This Multi line String
We can use Single quote also
"""

print(mail)

mail = "Python Programming"

print(len(mail))    # Length of String

mail = "Python 'Programming"   # This will print Python 'Programming

print(mail)

First = "Nagesh"
Last = "Kadam"

FullName = f"{First} {Last}"  # This is format will print the value of variable which is {}

print(FullName)

mail = " python Programming "

print(mail.upper())     # This will convert str to Upper case
print(mail.lower())     # This will convert str to Lower case
print(mail.title())     # This will Convert Starting letter to Upper
print(mail.strip())     # This will remove spaces from Left and Right Side
print(mail.rstrip())    # This will remove spaces from Right Side
print(mail.lstrip())    # This will remove spaces from Left Side
print(mail.find(" pyt"))     # This will find the string and return index if it is not present then it will return -1
print(mail.replace(" pyt", "PYT"))      # This is used to replace the given String if the Given String is not present then it willnot replace anything and won't throw error
print(" pyt" in mail)   # This will return true/False after checking given string is present or not
print(" pyt" not in mail)   # This will return true/False after checking given string is present or not

mail = "Nagesh,Mahadev,Kadam"
result = mail.split(",")  # This is used to Split str based on value given
print(result)
print(type(result))         # This is List Type

age = 36
txt = "My name is John, and I am {}"  # The format() method takes unlimited number of arguments, and are placed into the respective placeholders
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

mail = "Nagesh Nagesh Kadam"

print(mail.count("a"))  # print no of Times String present

print(mail.startswith("Na"))  # This is used to check String is startsWith given string

print(mail.endswith("a"))     # This is used to check String is endsWith given string

print(mail.index("Na"))       # Searches the string for a specified value and returns the position of where it was found

print(isinstance(mail, str))    # This is used to check mail variable is of type str or not

mail = ""                       # Empty Str
print(bool(mail))               # This will return False


Str1 = "Nagesh"
Str2 = "Nagesh"

if Str1 == Str2:
    print("Both the Strings are Equal")
else:
    print("Both the Strings are not equal")


Str1 = "Nagesh"
Str2 = "nagesh"

if Str1 == Str2:
    print("Both the Strings are Equal")
else:
    print("Both the Strings are not equal")

Str1 = "Nagesh"
Str2 = "nagesh"

if Str1.casefold() == Str2.casefold():      # it check for EqualIgnoreCase
    print("Both the Strings are Equal")
else:
    print("Both the Strings are not equal")


Str1 = "Nagesh"
Str2 = "nagesh"

if Str1.__eq__(Str2):                       # it will check for equality
    print("Both the Strings are Equal")
else:
    print("Both the Strings are not equal")


Str1 = "nagesh"
Str2 = "Nagesh"

if Str1 < Str2:
    print("Str1 is Less than Str2")
elif Str1 > Str2:
    print("Str2 is Less than Str3")
else:
    print("Both the Strings are Equal")


# Split the Line into Word

lines = "Nagesh Mahadev Kadam"
line = lines.split()
for i in line:
    print(i)
