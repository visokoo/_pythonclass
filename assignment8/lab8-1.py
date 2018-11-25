#!/usr/local/bin/python3
'''
----------------------------------------------------
Author: Vivian Ta
LAB 8-1
1) Create a constructor for your Person class.

2) Add FirstName and LastName attributes to the constructor of your person class.

'''

#--- Make the class ---
class Person(object):
    FirstName = ""
    LastName = ""

    def ToString(self):
        return self.FirstName + " " + self.LastName
#End of class

# --- Use the class ----
# by making an object!
objP1 = Person()
objP1.FirstName = "Bob"
objP1.LastName = "Lasso"

objP2 = Person()
objP2.FirstName = "Sue"
objP2.LastName = "Poe"

print(objP1.ToString())
print("-------------")
print(objP2.ToString())
