#Purpose: A program that will allow the user to input multiple lines of 
#         text content and write them into a text file named mylife.txt.

# Pseudocode

# Function to write input lines to a file
def write_to_file(filename):
        
    # Open the file in 'write' mode
    with open(filename, 'w') as file:
        while True:
              
              # Prompt the user to input a line
              line = input("Enter line: ")
              
              # Write the line to the file
              file.write(line + '\n')
              
              # Ask if there are more lines to add
              more_lines = input("Are there more lines? (y/n): ").lower()
              if more_lines != 'y':
                  break

write_to_file('mylife.txt')