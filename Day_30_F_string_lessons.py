# Day 30
#F string

name = "Katie"
age = "28"
pronouns = "she/her"


#******* the normal print statement*********
#print("This is", name, "using", pronouns, "pronouns and is age", age)

#********* used basic format to print the statement with print********
#print("This is {}, using {} pronouns,and is {} years old.".format(name,pronouns,age))

#LocalVaiables*******************
#print("This is {name}, using {pronouns} pronouns,and is {age} years old. Addiing additional statement to this thread for {name}, {pronouns} is being additionaly called to explain how f_statement works, however the {age} matters".format(name=name,pronouns=pronouns,age=age))

#assigning conactenated string to variable and then print the variable

#v_to_print = "This is {name}, using {pronouns} pronouns,and is {age} years old. Addiing additional statement to this thread for {name}, {pronouns} is being additionaly called to explain how f_statement works, however the {age} matters, right now variable containing {age} year old {name} is being assigned to variable to print ,lets see if {pronouns} print as we need".format(name=name,pronouns=pronouns,age=age)
#print(v_to_print)


#******* use of f*********

#""""""v_to_print = f"This is {name}, using {pronouns} pronouns,and is {age} years old. Addiing additional statement to this thread for {name}, {pronouns} is being additionaly called to explain how f_statement works, however the {age} matters, right now variable containing {age} year old {name} is being assigned to variable to print ,lets see if {pronouns} print as we need"
#print(v_to_print)""""""

#******* use of f with """" *********

###v_to_print = f"""This is {name}, using {pronouns} pronouns,and is {age} years old.

##Addiing additional statement to this thread for {name}, {pronouns} is being additionaly called to explain how f_statement works, however the {age} matters,

#right now variable containing {age} year old {name} is being assigned to variable to print ,lets see if {pronouns} print as we need"""

#print(v_to_print)



#******* use of allignment*********

#left = <, right = >, center = ^
#for i in range(1, 31):
#  print(f"Day {i: >3} of 30")



