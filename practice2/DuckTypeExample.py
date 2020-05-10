
"""
Duck Typing is a type system used in dynamic languages. For example, Python, Perl, Ruby, PHP, Javascript, etc. where the
type or the class of an object is less important than the method it defines. Using Duck Typing, we do not check types at
all. Instead, we check for the presence of a given method or attribute.

"""

class Laptop:
    def code(self, ide):        # We can pass any Object which has execute method
        ide.execute()


class PyCharm:
    def execute(self):
        print("PyCharm is Executing")


class MyEditor:
    def execute(self):
        print("MyEditor is Executing")


PyCharmObj = PyCharm()
MyEditorObj = MyEditor()
LaptopObj = Laptop()
LaptopObj.code(PyCharmObj)
LaptopObj.code(MyEditorObj)


