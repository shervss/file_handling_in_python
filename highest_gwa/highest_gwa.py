# Purpose: A program that reads a file containing the names of 20 students along 
#          with their GWA (Grade Weighted Average) and outputs the name of the 
#          student who achieved the highest GWA, including their GWA score.

# Pseudocode
def main():
    # Read student names and GWAs from file
    with open("student_gwa.txt", "r") as file:
        student_data = [line.strip().split(",") for line in file.readlines()]

# Find student with highest GWA
# Output the name of the student with the highest GWA

if __name__ == "__main__":
    main()