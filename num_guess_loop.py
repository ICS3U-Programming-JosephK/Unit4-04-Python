#!/usr/bin/env python3

# Created by: Joseph Kwon
# Created on: November 8
# This program generates a random number from 0-9 and repeats
# the process of asking the user to guess that random
# number until the user gets it correct

# imports random
import random

# assigns a random number from 0-9 to the secret_number variable
# secret_number = secret_number = random.randint(0, 9)
secret_number = secret_number = random.randint(0, 9)


def main():

    # Tries to get the user's number as an integer.
    try:
        user_number = int(input("Enter a positive integer from 0-9: "))

    # Exception thrown if the user did not enter a number
    except ValueError:
        input("You must enter a positive integer. Please try again.")

    # Restarts the program if the user entered a negative number
    if user_number < 0 and user_number < 9:
        print("Your guess must be between 0-9. Please try again.")

    else:
        # While user's guess is wrong, continue asking
        # using a while loop and end with a break statement
        while secret_number == user_number:
            print("Correct Guess!!!")
            break

        if user_number != secret_number:
            print("Your guess was wrong, guess again")
            main()


if __name__ == "__main__":
    main()
