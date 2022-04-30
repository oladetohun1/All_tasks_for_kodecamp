'''Write a number guessing game using python. Make the computer randomly
chooses a number between 1 to 10 (Use the randint function in the random module).
Then give users a hint to guess the number. Every time the user guess's a
wrong number, he gets another clue. the user has only three (3) chances to
guess this number.After the chances are given, the computer should output the
number.But if the user guesses the number correctly, then the computer should
tell the user that he guessed correctly.'''
#import randint from random
from random import randint
random_number = randint(1,10)
#Assign a random number between one and ten
Turns =3
while Turns >0:
    Your_guess = input("Enter a number between 1 and 10\n")#asks the user for a number between 1 and 10
    Turns -=1#decreaes the umber of turns while greater than zero
    if random_number==int(Your_guess):
        print("You guessed correctly!")
        print("You guessed correctly in ",(3-Turns),"guess(es)")
        break#condition to checkk if guessed number is equal to the right number
    if random_number!=int(Your_guess):
        print("You guessed wrongly, Try again")#to let the user know he guessed wrongly
        if Turns == 0:
            print("Game over!")#let the user know the game is over
