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
print"Today in this game you will guess the letters and have a great time playing hangman"
random_word= choose_word(wordlist)
print random_word
list = []
str=random_word
for letter in str:
    list.append(letter)
print list
list1=[]
len(list1)
print len(list1)
counter=0
for letter in list:
#len(list) == len(list):
    list1.append("_")
    counter=counter+1
print list1, list
while list != list1:
    counter1 = 0
    guess = raw_input("Enter guess here:")
    while counter1 < len(list):
        if guess == list [counter1]:
            list1[counter1]= guess
        print "That's correct!"
        break
    else:
        print"the guess is incorrect"
        break
        counter1 = counter1 + 1
    print list1









