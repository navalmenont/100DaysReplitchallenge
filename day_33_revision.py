#Day 2 - Beginner Level
#Exercise: Find Even Numbers
#Description: Write a Python function that takes a list of integers as input and returns a new list containing only the even numbers from the original list.

inputlist = []
evennumber = []

def find_even():
  for number in inputlist:
    if number%2 == 0:
      evennumber.append(number)
  print(f"{evennumber} are even numbers in the above list",end="")


while True:
  yes_no = input("if you want to add a number type in Yes: ")
  if yes_no == "yes":
    ask_input = int(input("Please type in the numbers to find out the even numbers in them (enter by sperating them in ,s):  "))
    inputlist.append(ask_input)
    print(f"{inputlist} has these numbers")
  elif yes_no == "no":
    print("not a valid input")
    break
  else:
    break
print(f"{inputlist}")  
find_even()
