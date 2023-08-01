#day 42 challenge



beast_name = input("Input your beast's name: ")
beast_type = input("Input your beast's type: ")
beast_special_move = input("Input your beast's special move: ")
beast_hp = input("Input your beast's staring HP: ")
beast_mp = input("Input your beast's staring MP: ")

data = {"name":beast_name ,"type":beast_type ,"move":beast_special_move,"HP":beast_hp, "MP":beast_mp}



for name,value in data.items():
  if name == "type":
    if value == "white":
      print(f"{name}:{value}")

  else:
     print(x)
     print(f"{name}:{value}")



# Function to change text color based on the MokéBeast type
def change_text_color(beast_type):
    colors = {
        "earth": "\033[0;33m",  # Yellow
        "fire": "\033[0;31m",   # Red
        "air": "\033[0;37m",    # White
        "water": "\033[0;34m",  # Blue
        "spirit": "\033[0;35m"  # Purple
    }
    return colors.get(beast_type.lower(), "\033[0m")  # Default to default color if type not recognized

# Ask the user to input MokéBeast details
name = input("Enter the name of your MokéBeast: ")
type_of_beast = input("Enter the type of your MokéBeast (earth, fire, air, water, or spirit): ")
special_move = input("Enter the special move of your MokéBeast: ")
starting_hp = int(input("Enter the starting HP of your MokéBeast: "))
starting_mp = int(input("Enter the starting MP of your MokéBeast: "))

# Store the details in a dictionary
mokebeast_details = {
    "Name": name,
    "Type": type_of_beast,
    "Special Move": special_move,
    "Starting HP": starting_hp,
    "Starting MP": starting_mp
}

# Output the beast's details with colored text based on its type
print("\nMokéBeast Details:")
for key, value in mokebeast_details.items():
    print(f"{change_text_color(key)}{key}: {value}\033[0m")  # Reset text color to default after each line
