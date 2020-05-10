"""
Python | Method Overloading
Like other languages (for example method overloading in C++) do, python does not supports method overloading.
We may overload the methods but can only use the latest defined method.

"""


class Student:
    def sum(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        elif a!=None:
            return a
        else:
            return 0


SObj1 = Student()
print(SObj1.sum())
print(SObj1.sum(10))
print(SObj1.sum(10, 10))
print(SObj1.sum(10, 10, 10))


# We can Handle same Things using Variable arguments

