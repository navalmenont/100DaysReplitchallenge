import random

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

def draw_hangman(wrong_guesses):
    hangman_parts = [
        "  O  ",
        " /|\ ",
        " / \ ",
    ]
    hangman_display = "\n".join(hangman_parts[:wrong_guesses])
    print(hangman_display)

def hangman(word):
    guessed_letters = []
    wrong_guesses = 0
    word_list = list(word.lower())

    while True:
        display_word = ""
        for letter in word_list:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        if display_word == word.lower():
            print(f"Congratulations! You win! The word was '{word}'.")
            break

        print("\nWord:", display_word)
        print("Guessed Letters:", ", ".join(guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_list:
            print("Correct guess!")
        else:
            print("Wrong guess.")
            wrong_guesses += 1
            draw_hangman(wrong_guesses)

        if wrong_guesses > 6:
            print("Sorry, you lost. The word was:", word)
            break


# Choose a random word from the list for the player to guess
target_word = random.choice(listOfWords)

# Start the hangman game with the selected word
hangman(target_word)
