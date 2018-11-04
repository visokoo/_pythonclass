#!/usr/local/bin/python3
'''
Author: Vivian Ta
Assignment 4
1)	Create new program that asks the user for the name of a household item,
and then asks for its estimated value. (This project is similar to the last one!)

2)	Ask the user for new entries and stores them in the 2-dimensional Tuple.

3)	Ask the user, when the program exits, if they would like to save/add the
data to a text file called, HomeInventory.txt.
'''

item_table = ()
# echo to user what's needed
print("Please input the name of the household item and the cost when prompted.")
while True:
  # gather params from user
  item = input("Item Name? ")
  price = float(input("Price? "))

  # store in tuple
  userItems = (str(item).capitalize(), str("$"+ "%0.2f" % price))
  # add tuple to table
  item_table += (userItems,)
  print(item_table)

  promptMore = input("More stuff to add? (y/n: ")
  if promptMore.lower() == 'n': break
# after exiting loop, prompt to save items
promptSave = input("Save your items to HomeInventory.txt? (y/n) ")
if promptSave.lower() == 'y':
  # open file in append mode
  fileToWriteTo = open("HomeInventory.txt", "a")
  #  write result to file
  fileToWriteTo.write(str(item_table))
  # close the file
  fileToWriteTo.close()