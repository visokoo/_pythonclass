#!/usr/local/bin/python3
'''
----------------------------------------------
Author: Vivian Ta
Assignment 2
• Create a new program that asks the user to input 2 numbers then prints out the sum, difference, product, and quotient.
----------------------------------------------
'''

print("Please give me 2 numbers and I'll calculate the sum, difference, product, and quotient of them.", end="\n\n")

num1 = float(input("First number? "))
num2 = float(input("Second number? "))

print("Sum: ", num1 + num2, ", " + "Difference: ", num1 - num2, ", ", "Product: ", num1 * num2, ", " , "Quotient: ", num1 / num2, sep="")
