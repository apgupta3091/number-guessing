#----------IMPORTS---------------------

import random
from art import logo

#---------PRINT/INPUTS-----------------

print("Welcome to the Number Guessing Game!")

print("I am thinking of a number between 1 and 100")

difficulty = input("Choose a difficulty type 'easy or 'hard': ")

#-----------CHECK DIFFICULTY-------------

if difficulty == 'easy':
    guesses = 10
    game_started = True

if difficulty == 'hard':
    guesses = 5
    game_started = True

#--------------FUNCTIONS---------------

def random_num():
    random_number = random.randint(1,100)
    return random_number

def compare(guess, random_number):
    if guess == random_number:
        return 0
    elif guess > random_number:
        return "Too high\nGuess again"
    else:
        return "Too low\nGuess again"

#-----------BEGGINIING OF GAME------------
while game_started:
    print(logo)

    print(f"You have {guesses} attempts remaing to guess the number")

    guess = int(input("Make a guess: "))
    random_number = random_num()
    
    #----CHECKS GUESSES > 1 and GAME STARTED----
    while guesses > 1 and game_started == True:
        
        if compare(guess,random_number) == 0:
            print(f"You got it the answer was {guess}")
            game_started = False
        else:   
            print(compare(guess,random_number))
            guesses -= 1
            print(f"You have {guesses} attempts remaining to guess the number")

            guess = int(input("Make a guess: "))

    #--------CHECK IF GUESSES = 0 ------------
    if game_started == True:
        print("You ran out of guesses, try again next time")
        game_started = False

        
            



