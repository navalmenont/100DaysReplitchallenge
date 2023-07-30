#Day 40 Dictionaries

myuser = {"name":"Das","prof":"PTL","age":"29"}
myuser["age"] = 34
print(myuser["age"])

#Challenge

form_name = input("Type in your name: ")
form_email = input("Type in your email: ")
form_twitter = input("Type in your twitterID: ")
form_birthdate = input("Type in your birthdate: ")

contact_details = {"name":form_name,"email":form_email,"form_twitter":form_twitter,"form_birthdate":form_birthdate}

print(f'{contact_details["form_twitter"]}')
