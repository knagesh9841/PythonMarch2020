"""
When we create constructor only in Super class then super class constructor is called
when we create constructor in Super class and Sub class then only Sub class constructor is called
we need to use Super().__init__() to call Super class constructor

"""

"""

What is object class?
Like Java Object class, in Python (from version 3.x), object is root of all classes.

"""

"""
Private members of parent class
We don’t always want the instance variables of the parent class to be inherited by the child class i.e. we can make some
of the instance variables of the parent class private, which won’t be available to the child class.
We can make an instance variable by adding double underscores before its name.
"""

# Single Inheritance


class A(object):
    school = "IIMP"                     # Class/Static variable it is Inherited

    def __init__(self):
        self.name = "Nagesh"
        self.address = "Latur"
        self.__married = "Yes"          # This is Private Instance variable it won't be inherited access in
        # public method same for private method.
        self._affair = "No"             # protected Instance variable and it is Inherited we can access it in Sub class
        # Similar for protected method but access in public method

    def show(self):
        print("Parent Class A Name is "+self.name)
        print("Parent Class A address is " + self.address)
        self.__marriedstatus()

    def _protectedmethod(self):
        print("Protected method of Class A and Affair Status is "+self._affair)

    def __marriedstatus(self):
        print("Married Status is", self.__married)


class B(A):
    def __init__(self):
        super().__init__()          # This will call Parent class Constructor
        self.name = "Bappa"
        self.address = "Pune"

    def show(self):
        super().show()              # This will call parent class show method
        super(B, self)._protectedmethod()   # Calling Protected method of Parent Class method always call in public
        print("Parent Class B Name is " + self.name)
        print("Parent Class B address is " + self.address)
        print("Parent Class B Affair status is " + self._affair)


BObj1 = B()
BObj1.show()
print("Static Variable in Child Class "+BObj1.school)       # Static/Class variable is inherited in Python


print(issubclass(B, A))     # This will check for B is Sub class of A

# MultiLevel Inheritance


class A1:

    def __init__(self):
        print("Grand parent A1 class constructor is called")
        self.gname = "Harichandra"

    def feature1(self):
        print("Grand Parent Name is "+self.gname)


class B1(A1):
    def __init__(self):
        super().__init__()
        print("Grand parent B1 class constructor is called")
        self.pname = "Mahadev"

    def feature2(self):
        print("Parent Name is " + self.pname)


class C1(B1):
    def __init__(self):
        super().__init__()
        print("Grand parent C1 class constructor is called")
        self.name = "Nagesh"

    def feature3(self):
        print("Name is " + self.name)


CObj1 = C1()
CObj1.feature1()
CObj1.feature2()
CObj1.feature3()


"""

Multiple Inheritance

MRO(Method Resolution order)
Incase of Multiple Inheritance class C(A,B) when we called super().__init__() 
then it will call left side class A constructor it works on left to right.We can call Class and B constructor using
A.__init__(self) and B.__init__(self)
when method in A and B class are same name then it will call 
left side class A method.we can call class A and B method using A.methodname(self) and B.methodname(self)

"""


class A2:
    def __init__(self):
        print("Mother A2 class constructor is called")
        self.mname = "Sujata"

    def feature1(self):
        print("Mother Name is "+self.mname)


class B2:
    def __init__(self):
        print("Father B2 class constructor is called")
        self.fname = "Mahadev"

    def feature1(self):
        print("Father Name is " + self.fname)


class C2(A2, B2):
    def __init__(self):
        #super().__init__()
        A2.__init__(self)
        B2.__init__(self)
        print("Child C2 class constructor is called")
        self.name = "Nagesh"

    def feature1(self):
        #super().feature1()         # it is similar to super(C2, self).feature1()
        A2.feature1(self)
        B2.feature1(self)
        print("Name is " + self.name)


C2Obj = C2()
C2Obj.feature1()



