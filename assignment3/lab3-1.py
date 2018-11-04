!/usr/local/bin/python3

intVar = 2
"""
Since the nested if statement never gets hit due to the first if statement
being evaluating to false, it'll hit the else case
"""
if (intVar == 1):
    print("1")
elif (intVar == 2): # This is a nested if statement
    print("2")
else:
    print("other")