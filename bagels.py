import random

NUM_DIGITS = 3
MAX_GUESSES = 3

def main():
    print("Bagels is a deductive logic game.")
    print("I am thinking of a {}-digit number with no repeated digits."
          "Try to gues what it is.Here are some clues:"
          "When I say:  That means:"
          "Pico  One digit is correct but in the wrong position."
          "Fermi One digit is correct and in the right position."
          "Bagels No digit is correct."
          ""
          "For example, if the secret number was 250 and your guess was 840 the clues would be Fermi Pico."
          .format(NUM_DIGITS))

    while True:  # The main game loop

        # This holds the secret number the player needs to guess:
        secretNum = getSecretNum()

        print("I have thought up a number.")
        print("You have {} guesses to get it.".format(MAX_GUESSES))

        numGuesses = 1

        while numGuesses <= MAX_GUESSES:

            guess = ""

            # Keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess #{}:".format(numGuesses))
                guess = input("> ")

            clues = getClues(guess, secretNum)
            print(clues)

            numGuesses += 1

            if guess == secretNum:
                break  # They are correct, so break out of this loop.

            if numGuesses > MAX_GUESSES:
                print("You ran out of guesses")
                print("The answer was {}.".format(secretNum))

        # Ask the player if they want to play again:
        print("Do you want to play again? (yes or no)")
        if not input(">").lower().startswith("y"):
            break

    print("Thanks for playing!")


def getSecretNum():
    """Returns a string made up of NUM_DIGITS unique random digits."""

    numbers = list("0123456789")
    random.shuffle(numbers)

    # Get the first NUM_DIGITS in the list for the secret number:
    secretNum = ""

    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

    return secretNum


def getClues(guess, secretNum):
    """Returns a string with the Pico, Fermi, Bagels for a guess and a secret number pair."""

    if guess == secretNum:
        return "You got it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit in the correct place
            clues.append("Fermi")

        elif guess[i] in secretNum:
            # A correct digit in the wrong place
            clues.append("Pico")

            # No correct digit

    if len(clues) == 0:
        # There are no correct digits at all
        return "Bagels"

    else:
        # Sort the clues into alphabetical order so their original order doesn't give information away.
        clues.sort()

        # Make a single string from the list of clues.
        return "".join(clues)


# If the program is run (instead of imported), run the game:
if __name__ == "__main__":
    main()