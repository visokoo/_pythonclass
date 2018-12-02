#!/usr/local/bin/python3
'''
Author: Vivian Ta
Assignment 9
1. Create a New Customer Application that works like the Customers one
   we made in the Module 09 labs. You can use the code samples I included in
   the Module 09 Python Programming Notes as a guide.
'''

# __main__
if __name__ == "__main__":
  import DataProcessing, Customers
else:
  raise Exception("This file was not created to be imported.")

# -- Data --#
# declare variables and constants
objC = None  # an Customer object
intId = 0  # an CustomerId
gIntLastId = 0  # Records the last CustomerId used in the client
strFirstName = ""  # an Customer's first name
strLastName = ""  # an Customer's last name
strInput = ""  # temporary user input

# -- Processing --#
# perform tasks
def AddNewCustomerData(Id, FirstName, LastName):
  try:
    # Create Customer object
    objC = Customers.Customer()
    objC.Id = Id
    objC.FirstName = FirstName
    objC.LastName = LastName
    Customers.CustomerList.AddCustomer(objC)
  except Exception as e:
    print(e)


def SaveDataToFile():
  try:
    objF = DataProcessing.DataProcessing()
    objF.FileName = "CustomerData.txt"
    objF.TextData = Customers.CustomerList.ToString()
    objF.SaveData()
  except Exception as e:
    print(e)

# -- Presentation (I/O) --#
# __main__

# get user input
strUserInput = ""
while (True):
  strUserInput = input("Would you like to add Customer data? (y/n)")
  if (strUserInput == "y"):
    # Get Customer Id from the User
    try:
      intId = int(input("Enter a Customer Id (Last id was " + str(gIntLastId) + "): "))
      gIntLastId = intId
    except ValueError as e:
      print("Please enter an integer.")
    # Get Customer FirstName from the User
    strFirstName = str(input("Enter a Customer First Name: "))
    # Get Customer LastName from the User
    strLastName = str(input("Enter a Customer Last Name: "))
    # Process input
    AddNewCustomerData(intId, strFirstName, strLastName)
  else:
    break

  # send program output
print("The Current Data is: ")
print("------------------------")
print(Customers.CustomerList.ToString())

# get user input
strInput = input("Would you like to save this data to the dat file?(y/n)")
if (strInput == "y"):
  SaveDataToFile()
  # send program output
  print("Data has been saved in file.")
else:
  print("There was an issue saving the file.")

print("This application has ended. Thank you!")