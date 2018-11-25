#!/usr/local/bin/python3
'''
Author: Vivian Ta
Assignment 8
1.  Create and test a new Python file using the following code.
2.  Create one or more classes to store and process Product data using the provided code.
'''

class Product(object):
  def __init__(self, ID, Name, Price):
    self.__ID = ID
    self.__Name = Name
    self.__Price = Price

  @property
  def ID(self):
    return self.__ID

  @ID.setter
  def ID(self, value):
    self.__ID = value

  @property
  def Name(self):
    return self.__Name

  @Name.setter
  def Name(self, value):
    self.__Name = value

  @property
  def Price(self):
    return self.__Price

  @Price.setter
  def Price(self, value):
    self.__Price = value

  def ToString(self):
    return str(self.__ID) + ", " + self.__Name + ", " + "$" + str(self.__Price)

  def __str__(self):
    return self.ToString()

class AccessProductData(Product):
  def DisplayMenu():
    print("Welcome to the Product List." + "\n" +
          "Hit enter to add an item or type 'exit' to save and exit")

  # Processing
  def WriteProductUserInput(File):
    try:
      while(True):
        try:
          choice = input("Continue or Exit? ")
          if choice.lower() == "exit": break
          id = int(input("Enter the ID: "))
          name = input("Enter the name of the product: ")
          price = float(input("Enter the price of the product: "))
          product = Product(id, name, price).ToString()
          File.write(product + "\n")
        except ValueError as e:
          print("Unexpected value type, exiting...")
          break
    except Exception as e:
      print("Error: " + str(e))

  def ReadAllFileData(File, Message="Contents of File"):
    try:
      print(Message)
      File.seek(0)
      print(File.read())
    except Exception as e:
      print("Error: " + str(e))

# I/O
try:
  AccessProductData.DisplayMenu()
  objFile = open("Products.txt", "r+")
  AccessProductData.ReadAllFileData(objFile, "Here is the current data:")
  AccessProductData.WriteProductUserInput(objFile)
  AccessProductData.ReadAllFileData(objFile, "Here is the data that has been saved so far:")
except FileNotFoundError as e:
     print("Error: " + str(e) + "\n Please check the file name")
except Exception as e:
    print("Error: " + str(e))
finally:
  if(objFile != None):objFile.close()
