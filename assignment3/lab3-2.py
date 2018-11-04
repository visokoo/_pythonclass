#!/usr/local/bin/python3
'''
----------------------------------------------------
Author: Vivian Ta
LAB 3-2
1) Write a script that lets a user select one of three
options by entering an argument when the script starts.
----------------------------------------------------
'''

# Get the argument value
# Execute if 1, 2, or 3 is selected
# Print "You chose one" only if option 1 is selected.
# Print "You chose two" execute only if option 2 is selected.
# Print "You chose three" execute only if option 3 is selected.
# Print "Please choose 1, 2, or 3"

import sys

# if (len(sys.argv) > 1):
#   userArg = int(sys.argv[1])
#   if userArg == 1:
#     print("You chose one")
#   elif userArg == 2:
#     print("You chose two")
#   elif userArg == 3:
#     print("You chose three")
#   else:
#     print("Please provide an arg, eg: python3 <script> <arg>)
# else:
#   print("Please choose 1, 2, or 3")

if (len(sys.argv) > 1):
  userArg = int(sys.argv[1])
  if userArg == 1: print("You chose one")
  elif userArg == 2: print("You chose two")
  elif userArg == 3: print("You chose three")
  else: print("Please choose 1, 2, or 3")
else: print("Please provide an arg, eg: python3 <script> <arg>")