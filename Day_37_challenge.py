#Day 37 String Slicing

first_name = input("Type in your first name: ") # type in the first name
last_name = input("Type in your second name: ") # type in the second name
first_name_s = first_name[:4].lower() # convert firstname to lower 
last_name_s = last_name[:4].lower() # convert secondname to lower
mothers_maiden_name =  input("Type in your Mothers Maiden name: ")
city_mother_born = input("Type in the city where your mother was born: ")
mothers_maiden_name_s = mothers_maiden_name[:3].lower()
city_mother_born_s = city_mother_born[-3:].lower()
star_wars_name = f"{first_name_s}{last_name_s} {mothers_maiden_name_s }{city_mother_born_s}"
print(f"Your StarWars Name is", {star_wars_name})




