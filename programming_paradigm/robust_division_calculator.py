def safe_divide(numerator, denominator):
    try:
        # Step 1: Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)
        
        # Step 2: Attempt the division
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Handles the case where the denominator is 0
        return "Error: Cannot divide by zero."
    
    except ValueError:
        # Handles cases where input cannot be converted to a float (e.g., "ten")
        return "Error: Please enter numeric values only."
