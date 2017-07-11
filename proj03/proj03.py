# Name:
# Date:


""" 
proj 03: Guessing Game

Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random
answer = random.randint(1,9)
answer = int(answer)
counter = 0
print "You have 4 guesses."
guess = raw_input("I'm thinking of a number between 1 and 9. Can you guess my number? Enter a number, or exit to exit:")
guess = int(guess)
True = guess != answer
loop_control = True
counter = counter + 1
if guess == answer:
    print "Congratulations, you guessed my number! You used", counter,"guess."
if guess == exit:
    print "You have exited the game."
    loop_control = false
while loop_control == True:
    guess = int(guess)
    if guess > answer:
        print 'Your number is too high!'
        counter = counter + 1
        guess = raw_input("Enter a number, or 'exit' to end the game:")
    elif guess < answer:
        print 'Your number is too low!'
        counter = counter + 1
        guess = raw_input("Enter a number, or 'exit' to end the game:")
    elif guess == answer:
        print "Congratulations, you guessed my number! You used", counter, "guesses"
        loop_control = False
    elif guess == exit:
        loop_control = False
    if counter == 4:
        print "You ran out of guesses! The game has ended."
        loop_control = False






