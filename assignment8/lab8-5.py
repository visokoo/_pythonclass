#!/usr/local/bin/python3
'''
----------------------------------------------------
Author: Vivian Ta
LAB 8-5
1) Create a customer class that has a CustomerId, FirstName, and LastName
properties by inheriting code from your Person class.
'''

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

class Customer(Person):
    def __init__(self, CustomerId, FirstName, LastName):
      self.__CustomerId = CustomerId
      super(Customer, self).__init__(FirstName, LastName)

    @property
    def CustomerId(self):
      return self.__CustomerId

    @CustomerId.setter
    def CustomerId(self, Value):
      self.__CustomerId = Value

    def ToString(self):
      person = super().ToString()
      return person + ', ' + str(self.CustomerId)

    def __str__(self):
      person = super().ToString()
      return self.ToString()

objP1 = Person("Bob", "Lasso")
objP2 = Person("Sue", "Poe")
custP1 = Customer(1, "James", "Cameron")

print(objP1.ToString())
print("-------------")
print(objP2)
print("-------------")
print(custP1)

