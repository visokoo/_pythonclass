#!/usr/local/bin/python3
'''
----------------------------------------------------
Author: Vivian Ta
LAB 5-1
1) Create an application that uses a dictionary to hold the following data:
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

dict1 = {"ID":1, "Name":"Bob Smith", "Email":"BSmith@Hotmail.com"}
dict2 = {"ID":2, "Name":"Sue Jones", "Email":"SueJ@Yahoo.com"}
dict3 = {"ID":3, "Name":"Joe James", "Email":"JoeJames@Gmail.com"}

dict_collection = [dict1, dict2, dict3]

while True:
  id = int(input("ID: "))
  name = input("Name: ")
  email = input("Email: ")
  new_row = {"ID":id, "Name":name, "Email":email}
  dict_collection.append(dict(new_row))
  prompt = input("Add another? y/n ")
  if prompt.lower() == 'n': break

save = input("Did you want to save the items you added to /tmp/dict.txt? y/n ")
if save.lower() == 'y':
  fileToWriteTo = open("/tmp/dict.txt", "a")
  for row in dict_collection:
    fileToWriteTo.write(str(row) + '\n')
  fileToWriteTo.close()
