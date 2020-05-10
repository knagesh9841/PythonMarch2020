import zope.interface

"""
The package zope.interface provides an implementation of “object interfaces” for Python. 
It is maintained by the Zope Toolkit project. The package exports two objects, ‘Interface’ and ‘Attribute’ directly. 
It also exports several helper methods. It aims to provide stricter semantics and better error messages than 
Python’s built-in abc module.

"""

# Declaring Interface


class MyInterface(zope.interface.Interface):
    name = zope.interface.Attribute("Nagesh")

    def method1(self, name):
        pass

    def method2(self):
        pass


# Implementing Interface


@zope.interface.implementer(MyInterface)
class MyClass:

    def method1(self, x):
        return x ** 2

    def method2(self):
        return "foo"


Obj1 = MyClass()
print(Obj1.method1(10))
print(Obj1.method2())
