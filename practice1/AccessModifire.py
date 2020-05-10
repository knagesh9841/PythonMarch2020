from practice1.AccessModifiiers import *

PObj2 = Super("Geeks", 4, "Geeks !")
print("Public Variable ", PObj2.var1)       # Public Member access anywhere
# Private member cannot accessible outside of class
CObj1 = Sub("Geeks", 4, "Geeks !")
CObj1.accessProtectedMemebers()             # Protected member accessed through Inheritance
# In Python there is protected concept just by using _variable we are using it
