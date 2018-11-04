#!/usr/local/bin/python3
'''
----------------------------------------------------
Author: Vivian Ta
LAB 5-1
1) Create an application that uses a list to hold the following data:
--------------------------------------
(1, 'Bob Smith', 'BSmith@Hotmail.com')
--------------------------------------
(2, 'Sue Jones', 'SueJ@Yahoo.com')
--------------------------------------
(3, 'Joe James', 'JoeJames@Gmail.com')

2) Add code that lets users append a new row of data

3) Add a loop that lets the user keep adding rows.

4) Ask the user if they want to save the data to a file when they exit the loop.

5) Save the data to a file if they say 'yes.'
'''

header = ['ID', 'Name', 'Email']
list1 = [1, 'Bob Smith', 'BSmith@Hotmail.com']
list2 = [2, 'Sue Jones', 'SueJ@Yahoo.com']
list3 = [3, 'Joe James', 'JoeJames@Gmail.com']

list_collection = [header, list1, list2, list3]

while True:
  print("Add a new row of data in the format of ID, Name, and Email.")
  id = int(input("ID: "))
  name = input("Name: ")
  email = input("Email: ")
  new_row = [id, name, email]
  list_collection.append(list(new_row))
  prompt = input("Add another? y/n ")
  if prompt.lower() == 'n': break

save = input("Did you want to save the items you added to /tmp/list.txt? y/n ")
if save.lower() == 'y':
  fileToWriteTo = open("/tmp/list.txt", "a")
  for row in list_collection:
    fileToWriteTo.write(str(row) + '\n')
  fileToWriteTo.close()
