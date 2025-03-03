import random


def hangman():
    words = ["python", "computer", "programming", "artificial", "intelligence", "random", "game", "challenge"]
    secret_word = random.choice(words)
    guessed_word = ["_"] * len(secret_word)
    attempts = 6
    guessed_letters = []

    print("Welcome to Hangman!")

    while attempts > 0 and "_" in guessed_word:
        print("\nWord:", " ".join(guessed_word))
        print(f"Attempts left: {attempts}")
        print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print("Wrong guess!")

    if "_" not in guessed_word:
        print(f"\nCongratulations! You guessed the word: {secret_word}")
    else:
        print(f"\nGame Over! The word was: {secret_word}")


hangman()
