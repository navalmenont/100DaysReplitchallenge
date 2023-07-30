# Day_32_revision

import random

timetable = ["Mathematics","Chemistry","Physics","Biology","Economics"]

def call_time_table():
  counter = 1
  for i in timetable:
    print(f"{i} for Period {counter}")
    counter +=1


timetable[3] = "Sport"
timetable[4] = "Art"

call_time_table()


#Day 1 - Beginner Level:
#Exercise: Create a Shopping List
#Description: Write a Python program that allows the user to add items to a shopping list. The program should use a list to store the items and provide options to add new items and display the current list.

import time 
import os
shoppinglist = []

def add_to_cart(item):
  if item not in shoppinglist:
    shoppinglist.append(item)
  else:
    print(f"{item} is already present in {shoppinglist}")
   

def printlist():
  print("Current cart contains these items")
  for items in shoppinglist:
    print(f"{items}", end="")
    print()
    

while True:
  print("Options")
  print("if you want to view current list, Press 1")
  print("if you want to edit the  current list, Press 2")

  request = input("").lower()
  if request == "1":
    printlist()
    
  elif request == "2":
    item = input("please enter the item you want to add to shopping list: ").lower()
    add_to_cart(item)
    printlist()
    time.sleep(3)
    os.system("clear")

  

