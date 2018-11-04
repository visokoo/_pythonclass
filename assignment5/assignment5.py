#!/usr/local/bin/python3
'''
Author: Vivian Ta
Assignment 5
1.	Create a text file called Todo.txt using the following data:

Clean House,low
Pay Bills,high

2.	When the program starts, load each row of data from the ToDo.txt text file into a Python dictionary. (The data will be stored like a row in a table.)
Tip: You can use a for loop to read a single line of text from the file and then place the data into a new dictionary object.

3.	After you get the data in a Python dictionary, Add the new dictionary “row” into a Python list object (now the data will be managed as a table).

4.	Display the contents of the List to the user.

5.	Allow the user to Add or Remove tasks from the list using numbered choices. Something like this would work:
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program

6.	Save the data from the table into the Todo.txt file when the program exits.
'''

# Grab data from text file and load into dictionary var via loop
initialTodoListfile = open("Todo.txt", "r+")
todoListobject = []
for line in initialTodoListfile.readlines():
	split_line = line.strip().split(",") # {'Item': 'Clean House,low\n'} had to add this line to remove \n
	todoDict = {"Item":split_line[0], "Priority":split_line[1]}
	# Add the dictionary object that was just created and add it into a python list
	todoListobject += [todoDict]

def show_current_items():
	global todoListobject
	for row in todoListobject:
		print(row)

def add_item():
	todoItem = input("Item: ")
	priority = input("Priority: ")
	newDict = {"Item":todoItem, "Priority":priority}
	global todoListobject
	todoListobject += [newDict]

def delete_item():
	# declaring a count var and incrementing as it loops through so the user can specify a list index to remove
	count = 0
	global todoListobject
	for item in todoListobject:
		print(count, ")", item, sep='')
		count += 1
	itemToRemove = int(input('\n' + "Which item number did you want to remove? " '\n'))
	todoListobject.pop(itemToRemove)
	print("Item #:", itemToRemove, "removed")

def save_list():
  # open file in append mode
  fileToWriteTo = open("Todo.txt", "w")
  #  write result to file
  global todoListobject
  for row in todoListobject:
  	fileToWriteTo.write(str(row['Item'] + "," + row['Priority'] + '\n'))

  # close the file
  fileToWriteTo.close()
  print("File saved to Todo.txt!")

# print list object contents to user
print("Initial contents of your Todo list:" + '\n')
show_current_items()

# Give user numbered choices for specific actions using if/elif/else statements
while True:
	print('\n' + "Things you can do with your list..." + '\n')
	print("1) Show current data" + '\n' + 
				"2) Add a new item" + '\n' +
				"3) Remove an existing item" + '\n' +
				"4) Save Data to File" + '\n' +
				"5) Exit Program, making no changes")
	choice = input("Choose one of the above options to interact with the list: ")
	if int(choice) == 1:
		show_current_items()
	elif int(choice) == 2:
		add_item()
	elif int(choice) == 3:
		delete_item()
	elif int(choice) == 4:
		save_list()
	else:
		print("Exiting...") 
		break