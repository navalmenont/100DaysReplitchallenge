#Day 43
#2D lists

my2DList =  ["Johnny", 21, "Mac"],
             ["Sian" 19, "PC"],
             ["Gethin", 17, "PC"], ]
print(my2DList[0][1])


import random


bingo_list = [["Q","W","R"],
              ["G","H","T"],
              ["A","B","C"]]



for i in range(0,3):
  if i == 0:
    for y in range(0,3):
      bingo_number = random.randint(1, 90)
      bingo_list[i][y] = bingo_number
  elif i == 1:
    for y in range(0,3):
        bingo_number = random.randint(1, 90)
        bingo_list[i][y] = bingo_number
              
  elif i == 2:
      for y in range(0,3):
        bingo_number = random.randint(1, 90)
        bingo_list[i][y] = bingo_number

bingo_list[1][1] = "BINGO"
print(bingo_list)
