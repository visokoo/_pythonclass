#!/usr/local/bin/python3
'''
----------------------------------------------------
Author: Vivian Ta
LAB 6-2
1) Create a function that prints the Sum, Difference, Product, and Quotient
of two numbers.
2) Display the results to the user.
3) Divide your program into data, processing, and presentation sections.
'''

def doSomeMath(n1, n2):
  float(n1)
  float(n2)
  sum = n1 + n2
  difference = n1 - n2
  product = n1 * n2
  quotient = n1 / n2
  return {"Sum":sum, "Difference": difference, "Product": product, "Quotient": quotient}

print(doSomeMath(2, 2))


# answers = doSomeMath(2,2)
# print("The sum is:", answers['Sum'])
# print(doSomeMath(2,2)['Sum'])