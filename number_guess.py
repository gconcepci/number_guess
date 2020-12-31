from random import randint

#Our structure is as follows:
#Program gets a random number.
#User tries to guess number.
#If number is within 15 digits to guess, Program says warm.
#If number is not within 15 digits, program say cold.
#User has 5 chances to guess.
#If guessed correctly, program says congrats and tells you how many guesses it took.
#If not guessed, program shows number and asks to play again.


#Initialize the winning number.
secret_number = randint(1, 100)
print("I'm thinking of a number between 1 and 100.")
print("Try to guess the number. I'll let you know if you're close.")
print("Enter 'q' at any time to quit.")
#For testing only.
print(secret_number)
#Our closeness ranges.
warm = range(1,15)
hot = range(1,5)

#Set our flag for the while loop.
active = True

#Set our counter for attempts.
guess_attempts = 1

while active:
    #Sets user input to variable guess.
    guess = input("What is your guess: ")

    # If guess is q, flag is set to false and program terminates.
    if guess == "q":
        active = False

    elif guess != secret_number and guess_attempts == 5:
        print("\nSorry, you ran out of guesses.")
        print(f"The number was {secret_number}.")
        active = False
        


    #Otherwise the guess is converted to an integer to be used in the program correctly.
    elif guess != "q":
        guess = int(guess)
        
        #If guess is not the winning number, attempts is incremented by 1 and loop restarts.
        if guess != secret_number:
            guess_attempts += 1
            
            #This is  where program will tell you if you are warm or cold.
            if abs(secret_number - guess) in warm:
                print("You're warm!")
                continue
            if abs(secret_number - guess) not in warm:
                print("Youre cold!")
                continue

        
       
        #If guess is the winning number, a congrats is printed with the attempts it took and program ends.
        else:
            #To make the win message more grammatically correct, the program checks if guess attempts
            #is 1 or greater. If 1, the message will say 1 try. If more than 1, it will say # tries.
            if guess_attempts == 1:
                print(f"Congrats, you guessed the number in {guess_attempts} try!")
                active = False

            elif guess_attempts > 1:
                print(f"Congrats, you guessed the number in {guess_attempts} tries!")
                active = False
            

            
#Success! But can you refactor all this sloppy code and create functions for each step?

