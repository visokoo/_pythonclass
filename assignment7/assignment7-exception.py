#!/usr/local/bin/python3
'''
Author: Vivian Ta
Assignment 7
1.	Research Python Exception Handling
2.  Research Python Pickling
3.  Create a simple example for python exception handling.
4.  Create a simple example for python pickling.
'''

# Python Exception Handling Code
import sys

def add_numbers():
  try:
    userArg = int(sys.argv[1])  # define arg1 from user
    userArg2 = int(sys.argv[2])  # define arg2 from user
    if len(sys.argv) > 3: raise Exception("Too many args")
    combined = userArg + userArg2  # add both args
    print(combined)  # print the result
  # catch not enough args provided error
  except IndexError as e:
    print("Please provide at least 2 args, eg: python3 <script> <arg> <arg2>")
  # catch args that are not numbers error
  except ValueError as e:
    print("This function can only add numbers")
  # catch all for everything else
  except Exception as e:
    print(e)

add_numbers()