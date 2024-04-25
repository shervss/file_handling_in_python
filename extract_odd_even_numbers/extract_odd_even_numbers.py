# Purpose: A program that will read a file named numbers.txt containing 20 integers 
#          and create two other text files: even.txt, which will contain all the even 
#          numbers extracted from numbers.txt, and odd.txt, which will contain all the 
#          odd numbers extracted from numbers.txt.

# Pseudocode
# Read numbers from numbers.txt
input_file = 'integers.txt'
even_numbers = []
odd_numbers = []

with open(input_file, 'r') as file:
    for line in file:
        number = int(line.strip())
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

# Extract even and odd numbers
# Write even numbers to even.txt
# Write odd numbers to odd.txt