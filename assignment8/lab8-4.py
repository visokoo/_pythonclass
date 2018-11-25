#!/usr/local/bin/python3
'''
----------------------------------------------------
Author: Vivian Ta
LAB 8-4
1) Add code to return the FirstName and LastName attribute in the __str__
method of your Person class.
'''

#--- Make the class ---
class Person(object):

    def __init__(self, FirstName, LastName):
      self.__FirstName = FirstName
      self.__LastName = LastName

    # Properties
    @property  # getter
    def FirstName(self):
      return self.__FirstName

    @FirstName.setter  # setter
    def FirstName(self, Value):
      self.__FirstName = Value

    @property  # getter
    def LastName(self):
      return self.__LastName

    @LastName.setter  # setter
    def LastName(self, Value):
      self.__LastName = Value

    def ToString(self):
        return self.__FirstName + " " + self.__LastName

    def __str__(self):
        return self.ToString()
#End of class

# --- Use the class ----
# by making an object!
objP1 = Person("Bob", "Lasso")

objP2 = Person("Sue", "Poe")

print(objP1.ToString())
print("-------------")
print(objP2)
