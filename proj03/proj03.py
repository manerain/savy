import random

# Name: Trey & Laila
# Date: July 2017

points = 5

print ""
print "Welcome to the Guessing Game!"
enter = raw_input("Press ENTER")
print ""
number = random.randint(1,9)

number = int(number)
loop = True
   




while loop == True:
    guess = raw_input("Guess my number, 1 to 9 (enter 0 to end game): ")
    guess = int(guess)
    if guess > number:
        
        print ""
        print "Your guess is too high."
        points = points - 1

    elif guess < number:
       
        if guess == 0:
            loop = False
            print "\nYou exited the game."
            print "Your total points: ", points
     
        elif guess < number:
            print ""
            print "Your guess is too low."

            points = points - 1

    elif guess == number:
        points = points + 5
        print "\nYou guessed my number! Congratulations!"
        print "You total points: ", points
        print ""
        number = random.randint(1,9)













