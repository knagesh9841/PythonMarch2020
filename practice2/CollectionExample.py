import collections
from collections import deque
from collections import ChainMap
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import UserList
from collections import UserDict

"""
Specialized Collection Data Structures
namedtuple( )
deque
ChainMap
Counter
OrderedDict
defaultdict
UserDict
UserList

"""

"""
namedtuple( )
It returns a tuple with a named entry, which means there will be a name assigned to each value in the tuple. 
It overcomes the problem of accessing the elements using the index values. 
With namedtuple( ) it becomes easier to access these values, since you do not have to remember the index values to get specific elements.
"""

# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)

# Access using getattr()
print("The Student DOB using getattr() is : ", end="")
print(getattr(S, 'DOB'))


"""
deque
deque pronounced as ‘deck’ is an optimized list to perform insertion and deletion easily.

"""

a = ['d', 'u', 'r', 'e', 'k']
a1 = deque(a)
print(a1)
#the output will be deque([ 'd' , 'u' , 'r' , 'e' , 'k' ])

a1.append('a')
print(a1)
# the output will be deque([ 'd' , 'u' , 'r' , 'e' , 'k' , 'a' ])
a1.appendleft('e')
print(a1)
# the output will be deque(['e' , 'd' , 'u' , 'r' , 'e' , 'k' , 'a' ])

a1.pop()
print(a1)
#the output will be deque([ 'e' , 'd' , 'u' , 'r' , 'e' , 'k' ])
a1.popleft()
print(a1)
#the output will be deque([ 'd' , 'u' , 'r' , 'e' , 'k' ])


"""
ChainMap
It is a dictionary like class which is able to make a single view of multiple mappings. 
It basically returns a list of several other dictionaries. 
Suppose you have two dictionaries with several key value pairs, in this case ChainMap will make a single list 
with both the dictionaries in it.
"""

a = {1: 'edureka', 2: 'python'}
b = {3: 'data science', 4: 'Machine learning'}
c = ChainMap(a, b)
print(c)
#the output will be ChainMap[{1: 'edureka' , 2: 'python'} , {3: 'data science' , 4: 'Machine learning'}]

"""
Counter
It is a dictionary subclass which is used to count hashable objects.
"""

a = [1, 1, 1, 1, 2, 3, 3, 4, 3, 3, 4]
c = Counter(a)
print(c)
#the output will be Counter = ({1:4 , 2:1 , 3:4 , 4:2})

for key, value in c.items():
    print(key,value)

"""
OrderedDict
It is a dictionary subclass which remembers the order in which the entries were added. 
Basically, even if you change the value of the key, the position will not be changed because of the order 
in which it was inserted in the dictionary.
"""

od = OrderedDict()
od[1] = 'e'
od[2] = 'd'
od[3] = 'u'
od[4] = 'r'
od[5] = 'e'
od[6] = 'k'
od[7] = 'a'
print(od)
#the output will be OrderedDict[(1 , 'e'), (2 , 'd') , (3 , 'u'), (4 , 'r'), (5 , 'e'), (6 , 'k'), (7 , 'a')]


"""
defaultdict
It is a dictionary subclass which calls a factory function to supply missing values. 
In general, it does not throw any errors when a missing key value is called in a dictionary.
"""

d = defaultdict(int)
#we have to specify a type as well.
d[1] = 'edureka'
d[2] = 'python'
print(d[3])
#it will give the output as 0 instead of keyerror.


"""
UserList
This class acts like a wrapper around the list objects. It is a useful base class for other list like classes 
which can inherit from them and override the existing methods or even add a fewer new ones as well.

The need for this class came from the necessity to subclass directly from list. 
It becomes easier to work with this class as the underlying list becomes an attribute.

"""


class MyList(UserList):

    # Function to stop deleltion
    # from List
    def remove(self, s=None):
        raise RuntimeError("Deletion not allowed")

        # Function to stop pop from

    # List
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Driver's code


L = MyList([1, 2, 3, 4])

print("Original List")

# Inserting to List"
L.append(5)
print("After Insertion")
print(L)

# Deleting From List
L.remove()


"""
UserDict
This class acts as a wrapper around dictionary objects. 
The need for this class came from the necessity to subclass directly from dict. 
It becomes easier to work with this class as the underlying dictionary becomes an attribute.
"""


class MyDict(UserDict):

    # Function to stop deletion
    # from dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")

        # Function to stop pop from

    # dictionary
    def pop(self, s=None):
        raise RuntimeError("Deletion not allowed")

        # Function to stop popitem

    # from Dictionary
    def popitem(self, s=None):
        raise RuntimeError("Deletion not allowed")

    # Driver's code


d = MyDict({'a': 1,
            'b': 2,
            'c': 3})

print("Original Dictionary")
print(d)

d.pop(1)
