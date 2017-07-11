# THIS IS A TEST COMMENT!

# Name:
# Date:

# proj01: A Simple Program
# This program asks the user for his/her name and age.
# Then, it prints a sentence that says when the user will turn 100.

# If you complete extensions, describe your extensions here!
name = raw_input("Enter your name:")
first_letter = name[0].upper()
begin_slice =name[1:].lower()
name = first_letter + begin_slice
print name
b = raw_input("Enter your age: ")
b = int(b)
if b > 13 or b == 13:
    print "You are allowed to watch PG13 rated and down movies."
elif b > 18:
    print "You are allowed to watch R rated and down movies."
if b < 13:
    print 'You are allowed to watch PG or G movies.'
a = raw_input('Have you had your birthday yet this year?')
if a == 'no':
    z = b + 1
    c = 2017 - z
    y = c + 100
else:
    c = 2017 - b
    y = c + 100
print name,'you will turn 100 in', y


