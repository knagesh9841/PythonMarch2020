from abc import ABC, abstractmethod, abstractproperty


class Laptop(ABC):

    school = "IIMP"

    def __init__(self):
        print("Abstract Class Constructor is called")
        self.name = "Nagesh"

    @abstractmethod
    def process(self):
        pass

    @classmethod
    @abstractmethod
    def classmethod(cls):
        pass

    @staticmethod
    @abstractmethod
    def my_abstract_staticmethod():
        pass

    @property
    @abstractmethod                 # getter/Setter/Deleter method we can Override and make it abstract
    def gettermethod(self):
        return

    def concretemethod(self):
        print("Concrete method of abstract is called")
        print("Name is "+self.name)


class Computer(Laptop):

    def __init__(self):
        super(Computer, self).__init__()        # Call Abstract class Constructor
        print("Implemented Class Constructor is called")
        self.nickname = "Bappa"

    def process(self):
        print("Abstract method is Implemented")
        print("Nick name is "+self.nickname)
        super(Computer, self).concretemethod()          # Call The concrete method of Abstract class

    @classmethod
    def classmethod(cls):
        print("Implemented Class Method")
        print("School Name is "+cls.school)

    @staticmethod
    def my_abstract_staticmethod():
        print("Static Method is overridden")

    def gettermethod(self):
        return "Getter Method of Implemented Class is called"


Obj1 = Computer()
Obj1.process()
Obj1.classmethod()
Computer.classmethod()
Obj1.my_abstract_staticmethod()
Computer.my_abstract_staticmethod()
print("School Name is "+Computer.school)
print(Obj1.gettermethod())



