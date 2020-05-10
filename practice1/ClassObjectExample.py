"""
Class is Design or Blueprint
Object is Instance

"""


class Person:
    school = "IIMP"     # Variable declare outside of __init__ is Static/Class Variable

    def __init__(self, name, address):      # This is constructor
        self.name = name                    # Variable declare inside __init__ is instance variable
        self.address = address
        self._salary = 0

    @classmethod                            # This Class method it works on Class/Static Variable
    def get_schoolname(cls):                # It acts on Static/Class variable we can change cla name but it is standard
        print("School Name is "+cls.school)

    @staticmethod                           # This is static method
    def get_genericinfo():
        print("This is person Class generic Static method")

    def get_persondetails(self):            # This is instance method
        print("Name is "+self.name)
        print("Address is "+self.address)
        print("School Name is " + self.school)      # Accessing using self

    @property
    def getttername(self):
        return self.name


PObj1 = Person("Nagesh", "Latur")
PObj2 = Person("Nagesh", "Latur")
PObj1.get_persondetails()           # Calling instance method with Object
PObj1.get_schoolname()              # Calling class method with Object
PObj1.get_genericinfo()             # Calling static method with Object
Person.get_schoolname()             # Calling class method with Class name
Person.get_genericinfo()            # Calling static method with Class name
Person.get_persondetails(PObj1)         # Another way to call Instance method by passing Object

print(PObj1 == PObj2)           # It checks for address

PObj1.name = "Bappa"

PObj1.get_persondetails()

print(PObj1.getttername)        # calling getter Method

"""
The pass Statement
class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error

"""


class Computer:
    pass


CompObj = Computer()        # We can create Object of Empty class


"""

Delete Objects
You can delete objects by using the del keyword:

Example
Delete the p1 object:

del p1

"""

del PObj1


