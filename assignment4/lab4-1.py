#!/usr/local/bin/python3
'''
----------------------------------------------------
Author: Vivian Ta
LAB 4-2
1) Create an application that uses a two dimensional tuple
to hold the following data.

2) Create a for loop that prints out each row of the data as follows:
ID, Name, Email
--------------------------------------
(1, 'Bob Smith', 'BSmith@Hotmail.com')
--------------------------------------
(2, 'Sue Jones', 'SueJ@Yahoo.com')
--------------------------------------
(3, 'Joe James', 'JoeJames@Gmail.com')

3) Now add a nested for-loop to extract the individual elements
(columns) data and display it as follows.
ID
Name
Email
--------------------------------------
1
Bob Smith
BSmith@Hotmail.com
--------------------------------------
2
Sue Jones
SueJ@Yahoo.com
--------------------------------------
3
Joe James
JoeJames@Gmail.com

'''

tuple0 = ('ID', 'Name', 'Email')
tuple1 = (1, 'Bob Smith', 'BSmith@Hotmail.com')
tuple2 = (2, 'Sue Jones', 'SueJ@Yahoo.com')
tuple3 = (3, 'Joe James', 'JoeJames@Gmail.com')

tuple_collection = (tuple1, tuple2, tuple3)
tuple_added = (tuple0 + tuple1 + tuple2 + tuple3)

print(tuple0[0] + ', ' + tuple0[1] + ', ' + tuple0[2])
for row in tuple_collection:
  print('--------------------------------------')
  print(row)

print('\n')

for i in tuple0:
  print(i)
for row in tuple_collection:
  print('--------------------------------------')
  for item in row:
    print(item)