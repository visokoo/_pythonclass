#!/usr/local/bin/python3
'''
----------------------------------------------------
Author: Vivian Ta
LAB 7-1
1) Create a script that allows you to store product IDs, names, and prices.
The code will be similar to the last example.
'''

while True:
  add_to_file = open("inventory.txt", "a+")
  print("Enter the product ID, name, and cost, separated by commas." +
        "\n" + "Type exit to quit.")
  p_id = input("Product ID? ")
  if p_id.lower() == 'exit': break
  else:
    name = input("Product Name? ")
    cost = input("Product Cost? ")
    item = {"ID":p_id, "Name":name, "Cost":cost}
    add_to_file.write("\n" + str(item['ID'] + "," + item['Name'] + "," + "$" + item['Cost']))
add_to_file.seek(0)
print(add_to_file.read())
add_to_file.close()


