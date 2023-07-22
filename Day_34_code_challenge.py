#Day 34


###Pretty Print

# import the libraries
import os,time 
#define a list

listofemail = []

def pretty_print():
  os.system("clear")
  print("listofemail")
  print()
  counter = 1
  for email in listofemail:
    print(f"{counter}: {email}")
    counter +=1
  time.sleep(1)  

#Create a whoile loop to iterate
while True:
  print("Spammer Inc.")
  menu = input("1: Add email\n2: Remove Email\n3: Show Email\n4: Get Spamming\n\n>> ")
  if menu == "1":
    email = input("Add email: ")
    listofemail.append(email)
  elif menu == "2":
    email = input("Add email: ")
    listofemail.remove(email)
  elif menu == "3":
    pretty_print()
  elif menu == "4":
    print(f"spamming with {listofemail}")
    break

time.sleep(1)
os.system("clear")

################# with Index

#Day 34

# import the libraries
import os,time 
#define a list

listofemail = []

def pretty_print():
  os.system("clear")
  print("listofemail")
  print()
  for index in range(len(listofemail)):
    print(f"{index}: {listofemail[index]}")
  time.sleep(1)  

#Create a whoile loop to iterate
while True:
  print("Spammer Inc.")
  menu = input("1: Add email\n2: Remove Email\n3: Show Email\n4: Get Spamming\n\n>> ")
  if menu == "1":
    email = input("Add email: ")
    listofemail.append(email)
  elif menu == "2":
    email = input("Add email: ")
    listofemail.remove(email)
  elif menu == "3":
    pretty_print()
  elif menu == "4":
    print(f"spamming with {listofemail}")
    break

time.sleep(1)
os.system("clear")

########Challenge


import os, time
listOfFood = []
def prettyPrint():
  os.system("clear") 
  print("listofFood") 
  print()
  counter = 1 
  for order in listOfFood: 
    print(f"[counter]: {order}") 
    counter + 1 
  time.sleep(1)
while True:
  print("Yummy Food Restaurant")
  menu = input("1. Order food\n2: Delete order\n3. Leave a review\n4. Delivery\n> ")
  if menu == "1":
    order = input("order > ")
    listOfFood.append(order)
  elif menu =="2":
    order = input ("delete order> ")
    if order in listOfFood:
      listOfFood.remove(order)
  elif menu == "3": 
  prettyPrint() 
  time.sleep(1)
  os.system("clear")

############Fixed

import os, time
listOfFood = []

def prettyPrint():
  os.system("clear") 
  print("listofFood") 
  print()
  counter = 1 
  for order in listOfFood: 
    print(f"{counter}: {order}") 
    counter +=1 
  time.sleep(1)
while True:
  print("Yummy Food Restaurant")
  menu = input("1. Order food\n2: Delete order\n3. Leave a review\n4. Delivery\n> ")
  if menu == "1":
    order = input("order > ")
    listOfFood.append(order)
  elif menu =="2":
    order = input ("delete order> ")
    if order in listOfFood:
      listOfFood.remove(order)
  elif menu == "3": 
    prettyPrint() 
  time.sleep(1)
  os.system("clear")
