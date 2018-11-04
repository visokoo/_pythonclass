#!/usr/local/bin/python3
'''
----------------------------------------------
Author: Vivian Ta
Assignment 3
• Create a new program that asks the user for the name of a household item,
and then asks for its estimated value. Store, both pieces of data in a text
file called, HomeInventory.txt
----------------------------------------------
'''

## first iteration
# # echo to user what's needed
# print("Please input the name of the household item and the cost when prompted.")
# # open file in append mode
# fileToWriteTo = open("HomeInventory.txt", "a")
#
# # gather params from user
# item = input("Item Name? ")
# price = input("Price? ")
# # concatenate both pieces of information into one var w/ a pipe separator and $
# combined = item + " | " + "$" + price + "\n"
# #  write result to file
# fileToWriteTo.write(combined)
# # close the file
# fileToWriteTo.close()

## second iteration
# echo to user what's needed
print("Please input the name of the household item and the cost when prompted.")
# open file in append mode
fileToWriteTo = open("HomeInventory.txt", "a")

# gather params from user
item = input("Item Name? ")
price = float(input("Price? "))
# concatenate both pieces of information into one var w/ a pipe separator and $
# also formatting the float into a string that always returns 2 decimal values
combined = item + " | " + "$" + "%0.2f" % price + "\n"
#  write result to file
fileToWriteTo.write(combined)
# close the file
fileToWriteTo.close()