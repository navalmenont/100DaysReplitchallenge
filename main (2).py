# Day 35 Challenge, creating a todolist

import os,time #os and time libraries to make output look better
todolist = [] #defined a empty list for lisst


def print_todolist():
  os.system("clear")
  counter =1
  print("Below are the items in Dasans To Do List\n")
  for item in todolist:
    print(f"{item}")
  time.sleep(1) #Function to print

while True:
  print("Dasans To Do list")
  print()
  menu = input("1.add items to list\n2.remove items from list\n3.view items from list\n4.edit the existing list\n5.Erase the complete list\n\n>>")
  if menu == "1":
    todo = input("What need to be added? ")
    if todo not in todolist:
      todolist.append(todo)
      print(f"added the {todo} to todolist and new list is {todolist}")
    else:
       print("The Value already exists hence cannot be added again")
    

  elif menu == "2":
    todo = input("What need to be removed? ")
    print(f"you are going to remove {todo} from the list and this change cant be undone")
    ask_f = input("yes/no: ")
    if ask_f == "yes":
      todolist.remove(todo)
      print(f"the current {todolist} is this")
    else:
      break

  elif menu == "3":
    print_todolist()

  elif menu == "4":
    print(f"existing todolist has {todolist} present")
    ask_index = input("Please input the text or word that you want to edit: ")
      #ask which item to be replaced
    print(ask_index)
    todolist.remove(ask_index)
    replace_index = input("Enter text that need to be added after edit: ")
    if replace_index not in todolist:
      todolist.append(replace_index)
      print(f"added the value and todolist is {todolist}")
    else:
       print("The Value already exists hence cannot be added again")

  elif menu == "5":
    todolist = []
    

    
    
    
  time.sleep(1)
  os.system("clear")

