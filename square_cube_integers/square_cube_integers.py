# Purpose: A method in Python that will create two separate text files 
#          after reading the source text file named integers.txt, which 
#          contains 20 integers. The first output file will be named 
#          double.txt, containing the square of all even integers found 
#          in integers.txt, and the second file will be named triple.txt, 
#          containing the cube of all odd numbers found in integers.txt.

# Pseudocode
# Read integers from input file
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

# Calculate squares of even numbers
even_squares = [num ** 2 for num in even_numbers]

# Calculate cubes of odd numbers
odd_cubes = [num ** 3 for num in odd_numbers]

# Write even squares to double.txt
with open('double.txt', 'w') as double_file:
    for square in even_squares:
        double_file.write(str(square) + '\n')

# Write odd cubes to triple.txt
with open('triple.txt', 'w') as triple_file:
    for cube in odd_cubes:
        triple_file.write(str(cube) + '\n')