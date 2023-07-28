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



def generate_star_wars_name():
    # Ask the user for first and last names
    full_name = input("Enter your first and last names (separated by a space): ")

    # Split the input into first name and last name
    first_name, last_name = full_name.split()

    # Generate Star Wars first name
    star_wars_first_name = f"{first_name[:3].capitalize()}{last_name[:3].capitalize()}"

    # Ask the user for mother's maiden name and city of birth
    maiden_name, city_of_birth = input("Enter your mother's maiden name and city of birth (separated by a space): ").split()

    # Generate Star Wars last name
    star_wars_last_name = f"{maiden_name[:2].capitalize()}{city_of_birth[-3:].capitalize()}"

    # Print the Star Wars names
    print(f"Your Star Wars name is: {star_wars_first_name} {star_wars_last_name}.")

# Run the program
generate_star_wars_name()




