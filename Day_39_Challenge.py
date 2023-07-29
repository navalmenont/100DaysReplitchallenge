def hangman(word):
    guessed_letters = set()
    wrong_guesses = 0
    word_set = set(word.lower())

    while True:
        display_word = ""
        for letter in word.lower():
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        if display_word == word.lower():
            print(f"Congratulations! You win! The word was '{word}'.")
            break

        print(f"\nWord: {display_word}")
        print(f"Guessed Letters: {', '.join(guessed_letters)}")
        guess = input("Guess a letter: ").lower()x

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_set:
            print("Correct guess!")
        else:
            print("Wrong guess.")
            wrong_guesses += 1

        if wrong_guesses > 6:
            print("Sorry, you lost. The word was:", word)
            break

# Prompt the user to enter a word for the hangman game
target_word = input("Enter the word to guess: ").strip().lower()

# Start the hangman game
hangman(target_word)
