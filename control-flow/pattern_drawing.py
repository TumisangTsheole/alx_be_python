# pattern_drawing.py

# 1. Prompt User for Pattern Size
size = int(input("Enter the size of the pattern: "))

# Initialize the row counter for the while loop
row = 0

# 2. Draw the Pattern
# The while loop iterates through each row
while row < size:
    # Inside the while loop, a for loop prints asterisks side by side
    for column in range(size):
        print("*", end="")
    
    # After the for loop finishes a row, print a newline to move down
    print()
    
    # Increment the row counter to move to the next row
    row += 1