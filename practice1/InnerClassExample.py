"""
You can create object of Inner Class inside the outer class
or
You can create object of inner class outside the outer class
provided you use outer class name to call it

"""


class Student:
    def __init__(self):
        self.name = "Nagesh"
        self.address = "Latur"
        self.lap = self.Laptop()        # Create Object Inside Outer Class

    def showdata(self):
        print("Name is "+self.name)
        print("Address is "+self.address)
        self.lap.showlaptopdata()       # This will call Inner class method

    class Laptop:
        def __init__(self):
            self.Brand = "HP"
            self.CPU = "I5"
            self.RAM = "16 GB"

        def showlaptopdata(self):
            print("Laptop Brand is "+self.Brand)
            print("Laptop CPU is " + self.CPU)
            print("Laptop RAM is " + self.RAM)


SObj1 = Student()
SObj1.showdata()
SObj1.lap.showlaptopdata()      # Call Inner class method

LapObj1 = Student.Laptop()      # Create Inner Class Object Outside outer class method
LapObj1.showlaptopdata()

