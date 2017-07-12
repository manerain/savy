# Name:
# Date:

"""
proj04

Asks the user for a string and prints out whether or not the string is a palindrome.

"""
loop_control = True
while loop_control == True:
    str = raw_input ("Enter words here and you will know if it is a palindrome or not: ")
    lst = []
    for letter in str:
        lst.append(letter)
    lst.reverse()
    lst2 = []
    for letter in str:
        lst2.append(letter)
    if lst2 == lst:
        print str, "is a palindrome."
    elif lst2 != lst:
        print str, "is not a palindrome."





















