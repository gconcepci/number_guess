from random import randint
"""
Our structure is as follows:
Program gets a random number.
User tries to guess number.
If user quits, print a message saying bye. Try to make a shuffled list of different messages that can be printed.
Program verifies that input is a number.
If number is within 10 digits to guess, Program says warm.
If number is not within 10 digits, program say cold.
User has 8 chances to guess.
If guessed correctly, program says congrats and tells you how many guesses it took.
If not guessed, program shows number and asks to play again.
"""
# Initialize the winning number.
secret_number = randint(1, 100)
secret_number_range = range(1,101)
print("I'm thinking of a number between 1 and 100.\nTry to guess the number in 8 tries. I'll let you know if you're close.\nEnter 'q' at any time to quit.")
# Set our flag for the while loop.
active = True
first_guess = True
# Set our counter for attempts.
guess_attempts = 0
guess = ""
guess_distances = []

while active:
    # Sets user input to variable guess.
    guess = input("What is your guess: ")

    if guess == "q":
        print("Thanks for playing! Bye bye!")
        break

    elif guess.isdigit() is False:
        print("Your guess has to be a number!")
        first_guess = True
        continue 

    elif guess.isdigit():
        guess = int(guess)
        guess_distance = abs(guess - secret_number)

        if guess not in secret_number_range:
            print("Not a valid guess. Number has to be between 1 and 100!")
            first_guess = True
            continue

        elif guess in secret_number_range:
            guess_attempts += 1
            guess_distances.append(guess_distance) 

            if first_guess is True and guess != secret_number:    
                if guess_distances[0] < 10:
                    print("You're warm!")
                    first_guess = False                   
                    continue

                elif guess_distances[0] > 10:
                    print("You're cold!")
                    first_guess = False
                    continue

            elif first_guess is False and guess != secret_number: 
                if guess_distances[-1] < guess_distances[-2]:
                    print("You're getting warmer!")
                    continue

                elif guess_distances[-1] > guess_distances[-2]:
                    print("You're getting colder!")
                    continue

                else:
                    print("You just guessed the same number!")
            else:
                if guess_attempts == 1:
                    print(f"Congratulations! You guessed the number in {guess_attempts} try!")
                    break

                else:
                    print(f"Congratulations! You guessed the number in {guess_attempts} tries!")
                    break
                
    if guess_attempts >= 8:
        print(f"Sorry you failed to guess the number.\nThe number was {secret_number}.")
        active = False