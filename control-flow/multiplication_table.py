# multiplication_table.py

# 1. Prompt User for a Number
# We convert the input to an integer to perform math operations
number = int(input("Enter a number to see its multiplication table: "))

# 2. Generate and Print the Multiplication Table
# The range(1, 11) function generates numbers from 1 up to (but not including) 11
for i in range(1, 11):
    product = number * i
    # Print the result in the format: X * Y = Z
    print(f"{number} * {i} = {product}")
