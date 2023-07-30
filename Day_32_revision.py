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


