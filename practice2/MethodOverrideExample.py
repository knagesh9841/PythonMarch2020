"""
Single Inheritance
In case of Same Method name in Super class and Sub Class
We can access Parent Class Method  using 2 Ways
1.ClassName.MethodName
2.Super.MethodName

we cannot call Variable with same name in Parent and Child which overrides the value with Child Value

"""


class A(object):

    school = "IIMP"

    def __init__(self):
        print("Parent Class A Constructor is Called")
        self.name = "Nagesh"

    def show(self):
        print("Parent Class Method Show is called.")
        print("Name is "+self.name)

    @classmethod
    def classmethod(cls):                   # Class method is Inherited and Overridden
        print("Parent Class Method")
        print("School Name is " + cls.school)

    @staticmethod                           # Static method is Inherited and Overridden
    def my_abstract_staticmethod():
        print("Parent Static Method is called")

    def _protectedmethod(self):             # protected method is Inherited and Overridden
        print("Parent Protected Method is called and Name is "+self.name)


class B(A):
    def __init__(self):
        super(B, self).__init__()
        print("Child Class B Constructor is Called")
        self.name = "Bappa"

    def show(self):
        #A.show(self)        # Call Parent Class Method which is having same name as Child Class
        super(B, self).show()   # Another Way to Call Parent Class Method which is having same name as Child Class
        print("Child Class Method Show is called.")
        print("Name is "+self.name)
        self._protectedmethod()     # Call Protected Method inside public method

    @classmethod
    def classmethod(cls):
        A.classmethod()
        print("Child Class Method")
        print("School Name is " + cls.school)

    def _protectedmethod(self):
        super()._protectedmethod()
        print("Child Protected Method is called and Name is "+self.name)


BObj1 = B()
BObj1.show()
BObj1.classmethod()
BObj1._protectedmethod()        # We can call using Objname._methodname but access it in public method
# same for protected variable
B.classmethod()
B.my_abstract_staticmethod()
A.show(BObj1)   # Call Parent Class Method which is having same name as Child Class


# Multiple Inheritance

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


# multiLevel Inheritance


class A1:

    def __init__(self):
        print("Grand parent A1 class constructor is called")
        self.gname = "Harichandra"

    def feature1(self):
        print("Grand Parent Name is "+self.gname)


class B1(A1):
    def __init__(self):
        super().__init__()
        print("Parent B1 class constructor is called")
        self.pname = "Mahadev"

    def feature1(self):
        super(B1, self).feature1()
        print("Parent Name is " + self.pname)


class C1(B1):
    def __init__(self):
        super().__init__()
        print("Child C1 class constructor is called")
        self.name = "Nagesh"

    def feature1(self):
        super(C1, self).feature1()
        print("Name is " + self.name)


CObj1 = C1()
CObj1.feature1()

