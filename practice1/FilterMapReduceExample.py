from functools import reduce

"""
The filter() function in Python takes in a function and a list as arguments. This offers an elegant way to filter out
all the elements of a sequence “sequence”, for which the function returns True.

"""

MyList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
MyList = list(filter(lambda x: (x % 2 == 0), MyList))

print(MyList)

"""
The map() function in Python takes in a function and a list as argument. The function is called with a lambda function 
and a list and a new list is returned which contains all the lambda modified items returned by that function for each 
item.

"""

MyList = list(map(lambda x: (x*2), MyList))

print(MyList)


"""
The reduce() function in Python takes in a function and a list as argument. The function is called with a lambda 
function and a list and a new reduced result is returned. This performs a repetitive operation over the pairs of the 
list. This is a part of functools module

"""


MyList = reduce(lambda x, y: (x+y), MyList)

print(MyList)

