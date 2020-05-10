"""
Public Access Modifier:
The members of a class which are declared public are easily accessible from any part of the program.
All data members and member functions of a class are public by default.

Protected Access Modifier:
The members of a class which are declared protected are only accessible to a class derived from it.
Data members of a class are declared protected by adding a single underscore ‘_’
symbol before the data member of that class.

Private Access Modifier:
The members of a class which are declared private are accessible within the class only,
private access modifier is the most secure access modifier.
Data members of a class are declared private by adding a double underscore ‘__’ symbol before the data member of that class.

"""


class Super:
    # constructor
    def __init__(self, var1, var2, var3):
        self.var1 = var1                # public data member
        self._var2 = var2               # protected data member
        self.__var3 = var3              # Private data Member


# derived class
class Sub(Super):

    # constructor
    def __init__(self, var1, var2, var3):
        Super.__init__(self, var1, var2, var3)

        # public member function

    def accessProtectedMemebers(self):
        print("Protected Member of Super Class", self._var2)


PObj2 = Super("Geeks", 4, "Geeks !")
print("Public Variable ", PObj2.var1)       # Public Member access anywhere
# Private member cannot accessible outside of class
CObj1 = Sub("Geeks", 4, "Geeks !")
CObj1.accessProtectedMemebers()             # Protected member accessed through Inheritance
# In Python there is protected concept just by using _variable we are using it
