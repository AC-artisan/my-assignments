# guessing_game.py - basic structure

import random # built in module for random numbers

play_again = "yes" 

while play_again.lower() in ["yes", "y"]:

    # generate a random number between 1 and 100
    secret = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("===  Number Guessing Game ===")
    print(f"\nI'm thinking of a number between 1 and 100.")
    print(f"You have {attempts + 1}/{max_attempts} attempts")

    # the game loop
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}: "))
        except ValueError:
            print("Please enter a valid number.")
            continue # dont run invalid input as an 'attempt'

        attempts += 1

        # check the guess
        if guess == secret:
            print(f"\nYou got it in {attempts} attempts! ")
            break # exit the loop; they won

        elif guess < secret:
            print("Too low! ")
        else:
            print("Too high! ")

    # show remaining attempts 
    remaining = max_attempts - attempts
    if remaining > 0:
        print(f"({remaining} attempts remaining!)")

    # handle the case where they run out of attempts
    # this runs only if the loop completed w/o hitting 'break' - meaning the player never guessed correctly
    else:
        print(f"\nOut of attempts!\nThe number was {secret}")


    play_again = input("\nPlay again? (yes/no): ")
    
print("Thanks for playing!")
     