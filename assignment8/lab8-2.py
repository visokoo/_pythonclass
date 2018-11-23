#!/usr/local/bin/python3
'''
----------------------------------------------------
Author: Vivian Ta
LAB 8-2
1) Create a constructor for your Person class.

2) Add FirstName and LastName attributes to the constructor of your person class.

'''

#--- Make the class ---
class Person(object):

    def __init__(self, FirstName, LastName):
      self.FirstName = FirstName
      self.LastName = LastName

    def ToString(self):
        return self.FirstName + " " + self.LastName
#End of class

# --- Use the class ----
# by making an object!
objP1 = Person("Bob", "Lasso")

objP2 = Person("Sue", "Poe")

print(objP1.ToString())
print("-------------")
print(objP2.ToString())
