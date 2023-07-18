#Day 33 Dynamic Lists

'''Practice 1, What are lists'''

myAgenda = []

def printList():
  print()
  for item in myAgenda:
    print(item)
  print()

while True:
  item = input("what is next on agenda? ")
  myAgenda.append(item)
  printList()


'''Practice 2, add or remove items from lists'''

myAgenda = []

def printList():
  print()
  for item in myAgenda:
    print(item)
  print()

while True:
  menu = input("add or remove: ")
  if menu == "add":
    item = input("what is next on agenda? ")
    myAgenda.append(item)

  elif menu == "remove":
      item = input("what on agenda should be remvoved? ")
      myAgenda.remove(item)
  printList()

'''Practice 3, add or remove items from lists with handling exception to remove items'''


myAgenda = []

def printList():
  print()
  for item in myAgenda:
    print(item)
  print()

while True:
  menu = input("add or remove: ")
  if menu == "add":
    item = input("what is next on agenda? ")
    myAgenda.append(item)

  elif menu == "remove":
      item = input("what on agenda should be remvoved? ")
      if item in myAgenda:
        myAgenda.remove(item)
      else:
        print("item not on the list")
  printList()

'''Fix My Code'''

#Errored Code

def printList():
  print() 
  for item in myPartyList:
    print(item)
  print() 
while True:
  menu = input("add or remove?: )
  if menu = "add":
    item = input("Who should I add to the party list?: ")
    myPartyList.add(item)
  elif menu == "remove":
    item = input("Who should I remove from the party list?: ")
    if item in myPartyList:
      myPartyList.remove(list)
    else:
      print("{item} was not in the list)
  printList()

# Fixed one

myPartyList = []

def printList():
  print() 
  for item in myPartyList:
    print(item)
  print() 
while True:
  menu = input("add or remove? " )
  if menu == "add":
    item = input("Who should I add to the party list?: ")
    myPartyList.append(item)
  elif menu == "remove":
    item = input("Who should I remove from the party list?: ")
    if item in myPartyList:
      myPartyList.remove(item)
    else:
      print(f"{item} was not in the list")
  printList()


# challenge

#Day 33 Challenge
#To do list


todoList = []

def printList():
  print() 
  for item in todoList :
    print(item)
  print() 
  
while True:
  ae = input("view, add or edit? " )
  if ae == "add":
    item = input("type in the item that you want to add?: ")
    todoList.append(item)
  elif ae == "edit":
    item = input("type in the item that you want to edit?: ")
    if item in todoList:
      todoList.remove(item)
    else:
      print(f"{item} was not in the list")
 
  elif ae == "view":
    printList()
   
  
