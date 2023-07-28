def get_color_code(color):
    colors = {
        'r': '\033[31m',  # Red
        'g': '\033[32m',  # Green
        'b': '\033[34m',  # Blue
        'p': '\033[35m',  # Purple/Magenta
        'y': '\033[33m',  # Yellow
    }
    return colors.get(color.lower(), '\033[0m')  # Default color reset code


def rainbowize_string(sentence):
    colored_output = ""

    current_color = None

    for letter in sentence:
        if letter.lower() in 'rgbpy':
            current_color = get_color_code(letter)
            colored_output += current_color

        colored_output += letter

        if letter == ' ':
            colored_output += '\033[0m'  # Reset color back to default after encountering a space

    print(colored_output + '\033[0m')  # Reset color to default at the end

# Ask the user to input a sentence
user_input = input("Enter a sentence: ")

# Rainbow-ize the input string and print the result
rainbowize_string(user_input)
