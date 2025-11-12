# 3. Drawing Patterns with Nested Loops

# pattern_drawing.py

# Prompt the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print asterisks (*) in each column
    for col in range(size):
        print("*", end="")  # Print on the same line
    print()  # Move to the next line after finishing one row
    row += 1  # Increment the row counter

