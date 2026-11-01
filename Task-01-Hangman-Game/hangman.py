import random

WORDS = [
    "python",
    "computer",
    "programming",
    "developer",
    "project",
    "learning",
    "hangman",
    "keyboard",
    "algorithm",
    "function",
]


def choose_word():
    return random.choice(WORDS)


def display_word(secret_word, guessed_letters):
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        print("\nWord: " + display_word(secret_word, guessed_letters))
        print("Attempts left: {}".format(attempts))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            attempts -= 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in secret_word):
            print("\nCongratulations! You won.")
            print("The word was: {}".format(secret_word))
            break

    if not all(letter in guessed_letters for letter in secret_word):
        print("\nGame over! You ran out of attempts.")
        print("The word was: {}".format(secret_word))


if __name__ == "__main__":
    play_hangman()
