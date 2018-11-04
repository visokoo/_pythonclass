#!/usr/local/bin/python3
'''
----------------------------------------------------
Author: Vivian Ta
LAB 3-3
1) Create a script that lets a user add two numbers together
and saves the answer to a file. Let the user continue adding
numbers until they type in the word "exit."
----------------------------------------------------
'''

print("Please continue to provide two numbers that you'd like to add." +
      " The results will be saved to /tmp/results.txt until you type 'exit.'")

fileToWriteTo = open("/tmp/results.txt", "a")
while True:
  input1 = input("Number 1? ")
  # if input1.lower() == "exit": break
  input2 = input("Number 2? ")
  fileToWriteTo.write(str(float(input1) + float(input2)) + "\n")
  if input("Type 'exit' to end this program, enter to continue: "): break
fileToWriteTo.close()