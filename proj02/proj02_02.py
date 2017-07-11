# Name:
# Date:

# proj02_02: Fibonaci Sequence

"""
Asks a user how many Fibonacci numbers to generate and generates them. The Fibonacci 
sequence is a sequence of numbers where the next number in the sequence is the sum of the 
previous two numbers in the sequence. The sequence looks like this: 
1, 1, 2, 3, 5, 8, 13..."""
counter = 0
counter3 = 0
cntr2 = 1
loop_control = counter
fib = raw_input('How many fibonacci numbers do you want to generate:')
fib = int(fib)
while counter < fib:
    seq = counter3 + cntr2
    seq = int(seq)
    print seq
    cntr2 = seq
    counter3 = cntr2
    counter = counter + 1
    

