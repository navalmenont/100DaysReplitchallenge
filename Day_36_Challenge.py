#Day 35 String Manipulation

name = input("What's your name? ")
if name.lower().strip() == "david":
  print("Hello Baldy!")
else: 
  print("What a beautiful head of hair!")



# no duplicates


myList = []
def printList():
  print()
  for i in myList:
    print(i)
  print()
while True:
  addItem = input("Item > ").capitalize().strip()
  if addItem not in myList:
    myList.append(addItem) 
  printList()


# no duplicates(Fix common errors)


myList = []
def printList():
  print()
  for i in myList:
    print(i)
  print()
while True:
  addItem = input("Item > ").strip().capitalize()
  if addItem not in myList:
    myList.append(addItem) 
  printList()




###Fix My Code
👉 Try and fix this code which is full of errors.

First, delete any other code in your main.py file. Copy each code snippet below into main.py by clicking the copy icon in the top right of each code box. Then, hit run and see what errors occur. Fix the errors and press run again until you are error free. Click on the 👀 Answer to compare your code to the correct code.

whatToEat = input("What do you fancy for dinner? ")
if whatToEat.strip = "pasta": 
  print("Get out the pasta maker.")
elif whatToEatlower() == "TACOS":
  print("Let's do Taco Tuesday!")
else: 
  print("Go search the fridge.")

#Fixed code






## Challenge

# Day 36 Challenge
list_of_people = []

while True:
  ask_first_name = input("Please type in your First name: ").strip().capitalize()
  ask_Second_name = input("Please type in your Second name: ").strip().capitalize()
  name = f"{ask_first_name} {ask_Second_name}" #lower can be used with f strings and will help remove duplicates
  name = name.lower() # once lower is used above this statement wont be required
  list_of_people.append(name)
  print(f"{list_of_people}")
  
