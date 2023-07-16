

#Day 31 Challenge 2

def color_t(color, text):
    if color == "black":
        return "\033[0;30m" + text + "\033[0m"
    elif color == "red":
        return "\033[0;31m" + text + "\033[0m"
    elif color == "green":
        return "\033[0;32m" + text + "\033[0m"
    elif color == "blue":
        return "\033[0;34m" + text + "\033[0m"
    else:
        return "\033[1;33m" + text + "\033[0m"

# create variables with color codes by calling the function
black = color_t("black", "=")
red = color_t("red", "=")
green = color_t("green", "=")
blue = color_t("blue", "=")
white = color_t("white", "=")

welcome = color_t("white","WELCOME TO")
book = color_t("blue", "ARMBOOK")
book_text =f"{blue} {blue} {book: ^25} {blue} {blue}"
print(f"{welcome:^95}")
print(f"{book_text:^140}")
print()
print()
text_1 =  color_t("green", "Definitely not a rip off of a certain other social networking site ")
text_2 =  color_t("green", "Honest")
text_3 =  color_t("blue", "Username")
text_4 =  color_t("black", "Password")

print(f"{text_1:^100}")
print()

print(f"{text_2:^94}")
print()
print(f"{text_3:^94}")
print(f"{text_4:^94}")
