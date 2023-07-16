#day 32 Lists

# Learning lists starts with "[]" brackets.Always remember the list starts with Zero

timetable = ["computer science","Mathematics","History","chemistry","physics"]
print(timetable[3],timetable[1],timetable[2],timetable[0]) # printing the list above by calling each one

# adding/replace more variables to the list

timetable[3] = "Sport"
timetable[4] = "physics"

#instead of calling each by doing a print we can use loop to iterate through list and print one by one
for subject in timetable:
  print(subject)

#fixing the errors

#below code is one with error
grocery list = ["bananas", "bread", "milk", "eggs", "juice", "cheese"]
print("The first grocery item to buy is {grocery list[1]}.")

#fixed to 
grocery_list = ["bananas", "bread", "milk", "eggs", "juice", "cheese"]
print(f"The first grocery item to buy is {grocery_list[0]}.")
