"""
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
To prevent the iteration to go on forever, we can use the StopIteration statement.

"""


class MyNumbers:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):     # you can do operations initializing etc.,must always return the iterator object itself.
        self.a = 1
        return self

    def __next__(self):     # method also allows you to do operations, and must return the next item in the sequence.
        if self.a <= self.limit:
            val = self.a
            self.a += 1
            return val
        else:
            raise StopIteration # prevent the iteration to go on forever, we can use the StopIteration statement


MyNumbersObj = MyNumbers(10)

for i in MyNumbersObj:
    print(i)

