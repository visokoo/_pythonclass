#!/usr/local/bin/python3
'''
Author: Vivian Ta
LAB 4-2
1) Create an application that uses a two dimensional tuple
to hold the following data.

2) Add code that searches for customers by name and returns a
customer ID.

3) Extra: Add a loop that lets the user keep trying

'''

tuple1 = (1, 'Bob Smith', 'BSmith@Hotmail.com')
tuple2 = (2, 'Sue Jones', 'SueJ@Yahoo.com')
tuple3 = (3, 'Joe James', 'JoeJames@Gmail.com')
combined_tuples = (tuple1, tuple2, tuple3)

while True:
  customerName = input("Customer Name: ")
  found = False
  for item in combined_tuples:
    if customerName in item:
      print("Customer found with ID: " + str(item[0]))
      found = True
  if found == False: print("Customer cannot be found.")
  promptContinue = input("Search again? (y/n): ")
  if promptContinue.lower() == 'n': break