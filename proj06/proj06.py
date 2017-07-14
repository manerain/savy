# Name:
# Date:
# proj06: Hangman
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string
WORDLIST_FILENAME = "words.txt"
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist
def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
# end of helper code
# -----------------------------------
# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()
# your code begins here!
print"Welcome to hangman."
print"Today in this game you will guess the letters and have a great time playing hangman. You have 6 lives."
random_word= choose_word(wordlist)
list = []
str=random_word
for letter in str:
    list.append(letter)
#print list
wrong_guesses = []
list1=[]
len(list1) #
counter=0
for letter in list:
    #len(list) == len(list)
    list1.append("_")
    counter=counter+1
print list1
limit = 6
counter2 = 0
while list != list1:
    N_word=False
    counter1 = 0
    guess = raw_input("Enter guess here: ")
    while counter1 < len(list):
        if len(guess) > 1:
            if guess == random_word:
                N_word = True
                list1 = list
                #print "Congratulations! You got the word!"
                break
            else:
                print "Incorrect."
                #limit = limit - 1
                break
        if len(guess) == 1:
            if guess == list[counter1]:
                list1[counter1]= guess
                N_word = True
               # print "Correct!"
            counter1 = counter1 + 1
            if counter1 == len(list):

                break
            if limit == 0:
                print "you ran out of guesses."
                break


    print list1
    if N_word == False:
        limit = limit -1
        print "Your guess is incorrect. You have", limit, "guesses left."
    else:
        print "Correct!"
    if limit == 0:
        print "You ran out of guesses. The game has ended.The word was", random_word
        break
if list == list1:
    print "Congratulations!You got the word!"
