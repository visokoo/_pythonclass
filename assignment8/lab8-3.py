#!/usr/local/bin/python3
'''
----------------------------------------------------
Author: Vivian Ta
LAB 8-2
1) Make the FirstName and LastName attributes private in the constructor
of your Person class.

2) Add an accessors and mutators property procedures for the FirstName
and LastName attributes.

'''

#--- Make the class ---
class Person(object):

    def __init__(self, FirstName, LastName):
      self.__FirstName = FirstName
      self.__LastName = LastName

    # Properties
    @property # getter
    def FirstName(self):
      return self.__FirstName

    @FirstName.setter # setter
    def FirstName(self, Value):
      self.__FirstName = Value

    @property # getter
    def LastName(self):
      return self.__LastName

    @LastName.setter # setter
    def LastName(self, Value):
      self.__LastName = Value

    def ToString(self):
        return self.__FirstName + " " + self.__LastName
#End of class

# --- Use the class ----
# by making an object!
objP1 = Person("Bob", "Lasso")

objP2 = Person("Sue", "Poe")

print(objP1.ToString())
print("-------------")
print(objP2.ToString())
