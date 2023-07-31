#day 41 Dictionaries With Loops

myDictionary = {"name":"Das","health":"210","stength":"300","eqipped":"sword" }


for name,value in myDictionary.items():
  if name == "name":
    if value == "Das":
      print(f"{name}:{value}")

  else:
     print(f"{name}:{value}")



website_name = input("Type in your website name: ")
website_email = input("Type in your website_email: ")
website_url = input("Type in your websiteURL: ")
website_description = input("Type in your webisiteDescription: ")
website_rating = input("Type in your webisiterating: ")

data = {"name":website_name ,"email":website_email,"url":website_url,"description":website_description,"rating":website_rating}


for name,value in data.items():
  print(f"{name}:{value}")
  
