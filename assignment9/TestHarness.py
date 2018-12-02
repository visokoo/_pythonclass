# !/usr/local/bin/python3
import Persons

person = Persons.Person()
person.FirstName = "James"
person.LastName = "Cameron"
print(person)
print(person.GetObjectCount())

import Customers

customer = Customers.Customer()
customer.Id = 1
customer.FirstName = "Alisha"
customer.LastName = "Banner"
print("This is the Customer Object: ",  customer)

import DataProcessing

file = DataProcessing.DataProcessing()
file.FileName = "Testfile.txt"
file.TextData = "Blah"
file.SaveData()
