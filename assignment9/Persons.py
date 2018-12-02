#!/usr/local/bin/python3
'''
----------------------------------------------------
Author: Vivian Ta
LAB 9-2
1) Create a Persons Base class in its own module called Persons.py.

2) Create an Customer child class in its own module called Customers.

3) Create a test harness and test that they work.
'''

if __name__ == "__main__":
  raise Exception("This file is not meant to run by itself")

# --- Make the class ---
class Person(object):

  # --Fields--
  __Counter = 0  # Hey Devs, please consider this a private class field. Thx!

  # --Constructor--
  def __init__(self, FirstName="", LastName=""):
    # Attributes
    self.__FirstName = FirstName  # Private Attribute
    self.__LastName = LastName # Private Attribute
    Person.__SetObjectCount()  # Private Method

  # --Properties--
  # FirstName
  @property  # getter(accessor)
  def FirstName(self):
    return self.__FirstName

  @FirstName.setter  # (mutator)
  def FirstName(self, Value):
    self.__FirstName = Value

  @property  # getter(accessor)
  def LastName(self):
    return self.__LastName

  @LastName.setter  # (mutator)
  def LastName(self, Value):
    self.__LastName = Value

  # --Methods--
  def ToString(self):
    """Explictly returns field data"""
    return self.FirstName + "," + self.LastName

  def __str__(self):
    """Implictly returns field data"""
    return self.ToString()

  @staticmethod
  def GetObjectCount():  # You do not need the self keyword
    return Person.__Counter

  @staticmethod
  def __SetObjectCount():  # This is a private and static method
    Person.__Counter += 1

  # --End of class Person--