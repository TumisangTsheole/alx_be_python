# arithmetic_operations.py

def perform_operation(num1, num2, operation):
    """
    Performs basic arithmetic based on the operation string.
    Handles add, subtract, multiply, and divide.
    """
    if operation == 'add':
        return num1 + num2
    
    elif operation == 'subtract':
        return num1 - num2
    
    elif operation == 'multiply':
        return num1 * num2
    
    elif operation == 'divide':
        # Handling the division by zero case gracefully
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    
    else:
        return "Error: Invalid operation."
