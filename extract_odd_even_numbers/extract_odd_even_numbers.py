# Purpose: A program that will read a file named numbers.txt containing 20 integers 
#          and create two other text files: even.txt, which will contain all the even 
#          numbers extracted from numbers.txt, and odd.txt, which will contain all the 
#          odd numbers extracted from numbers.txt.

# Pseudocode

def main():
    # Read numbers from numbers.txt
    with open("numbers.txt", "r") as file:
        numbers = [int(num.strip()) for num in file.readlines()]

    # Extract even and odd numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    # Write even numbers to even.txt
    with open("even.txt", "w") as even_file:
        for num in even_numbers:
            even_file.write(str(num) + "\n")

    # Write odd numbers to odd.txt
    with open("odd.txt", "w") as odd_file:
        for num in odd_numbers:
            odd_file.write(str(num) + "\n")

    print("Even and odd numbers extracted and written to even.txt and odd.txt respectively.")


if __name__ == "__main__":
    main()