#!/usr/local/bin/python3
'''
----------------------------------------------------
Author: Vivian Ta
LAB 6-2
1) Create a class with 4 methods that prints the Sum, Difference, Product, and Quotient
of two numbers.
2) Name the class MathProcessor
3) Name the methods AddValues, SubtractValues, MultiplyValues, DivideValues
4) Display the results to the user by calling each method.
'''

class MathProcessor(object):

  @staticmethod
  def AddValues(n1, n2):
    return n1 + n2

  @staticmethod
  def SubtractValues(n1, n2):
    return n1 - n2

  @staticmethod
  def MultiplyValues(n1, n2):
    return n1 * n2

  @staticmethod
  def DivideValues(n1, n2):
    return n1 / n2

print("The value of the sum is:", MathProcessor.AddValues(2,2))
print("The value of the difference is:", MathProcessor.SubtractValues(2,2))
print("The value of the product is:", MathProcessor.MultiplyValues(2,2))
print("The value of the quotient is:", MathProcessor.DivideValues(2,2))