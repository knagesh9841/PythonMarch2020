class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        sobj = A(a, b)
        return sobj

    def __gt__(self, other):
        if self.a > other.a and self.b > other.b:
            return True
        else:
            return False

    def __str__(self):
        return "{} and {}".format(self.a, self.b)


Obj1 = A(10, 20)
Obj2 = A(30, 40)

Obj3 = Obj1 + Obj2
print(Obj3)

if Obj1 > Obj2:
    print("Obj1 is Greater than Obj2")
else:
    print("Obj2 is Greater than Obj1")
