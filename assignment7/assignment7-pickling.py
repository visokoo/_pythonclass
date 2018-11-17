#!/usr/local/bin/python3
'''
Author: Vivian Ta
Assignment 7
1.	Research Python Exception Handling
2.  Research Python Pickling
3.  Create a simple example for python exception handling.
4.  Create a simple example for python pickling.
'''

# Python Pickling Code
import pickle

# creating a dict to be dumped by pickle
dict = {"dairy": "milk, eggs, butter",
        "grains": "wheat, barley",
        "vegetables": "carrots, tomato, celery"}

dict2 = {"meat": "chicken, pork, beef",
         "fruit": "apples, oranges, pears"}

# opening a file in binary write mode
file = open("food_pyramid.dat", "wb")

# dump the dict to the file
pickle.dump(dict, file)
pickle.dump(dict2, file)

# close the file
file.close()

# open the file in binary read mode
dat = open("food_pyramid.dat", "rb")

# assign the load to a var
food_pyramid = pickle.load(dat)
food_pyramid2 = pickle.load(dat)

dat.close()

# print the var for the data
print(food_pyramid)
print(food_pyramid2)