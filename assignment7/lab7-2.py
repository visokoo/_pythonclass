#!/usr/local/bin/python3
'''
----------------------------------------------------
Author: Vivian Ta
LAB 7-1
1) Add error handling code to the lab7-1.py.
'''

while True:
  try:
    add_to_file = open("inventory.txt", "a+")
    print("Enter the product ID, name, and cost, separated by commas." +
          "\n" + "Type exit to quit.")
    p_id = input("Product ID? ")
    if p_id.lower() == 'exit': break
    else:
      name = input("Product Name? ")
      try:
        cost = float(input("Product Cost? "))
      except ValueError as e:
        print("Cost must be an number.")
      item = {"ID":p_id, "Name":name, "Cost":cost}
      add_to_file.write("\n" + str(item['ID'] + "," + item['Name'] + "," + "$" + item['Cost']))
  except Exception as e:
    print("An unexpected error has occurred and no data was saved.", "\n")
add_to_file.seek(0)
print(add_to_file.read())
add_to_file.close()