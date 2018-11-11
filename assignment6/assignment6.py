#!/usr/local/bin/python3
'''
Author: Vivian Ta
Assignment 6
1.	Take what you did in assignment5 and put them into functions and organize it as a class.
'''

# Grab data from text file and load into dictionary var via loop
initialTodoListfile = open("Todo.txt", "r+")
todoListobject = []

for line in initialTodoListfile.readlines():
  split_line = line.strip().split(",")  # {'Item': 'Clean House,low\n'} had to add this line to remove \n
  todoDict = {"Item": split_line[0], "Priority": split_line[1]}
  # Add the dictionary object that was just created and add it into a python list
  todoListobject += [todoDict]

class TodoList(object):

  # @staticmethod
  # def loadInitialList():
  #   initialTodoListfile = open("Todo.txt", "r+")
  #   todoListobject = []
  #   for line in initialTodoListfile.readlines():
  #     split_line = line.strip().split(",")  # {'Item': 'Clean House,low\n'} had to add this line to remove \n
  #     todoDict = {"Item": split_line[0], "Priority": split_line[1]}
  #     # Add the dictionary object that was just created and add it into a python list
  #     todoListobject += [todoDict]
  #   return todoListobject

  def show_current_items():
    global todoListobject
    for row in todoListobject:
      print(row)

  def add_item():
    todoItem = input("Item: ")
    priority = input("Priority: ")
    newDict = {"Item": todoItem, "Priority": priority}
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
TodoList.show_current_items()

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
		TodoList.show_current_items()
	elif int(choice) == 2:
		TodoList.add_item()
	elif int(choice) == 3:
		TodoList.delete_item()
	elif int(choice) == 4:
		TodoList.save_list()
	else:
		print("Exiting...")
		break