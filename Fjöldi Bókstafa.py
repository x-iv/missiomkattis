# Read the input string from standard input
import sys
input_string = sys.stdin.read().strip()

# Initialize the letter count to 0
letter_count = 0

# Loop through each character in the input string
for char in input_string:
    # Check if the character is a letter
    if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
        # Increment the letter count
        letter_count += 1

# Print the total number of letters
print(letter_count)
