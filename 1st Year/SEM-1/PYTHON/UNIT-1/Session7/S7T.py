"""
IMMUTABLE TYPES: NUMBERS (int, float, complex)
Numbers in Python are immutable, meaning their value cannot be changed after creation.
Python supports three core numeric types, distinguished by the presence or absence of a decimal point.
"""
# 1. Integer (int): Whole numbers without a fractional part.
num_int = 5 # Literal representation [cite: 24, 44]
print(f"Integer Example: {num_int} is of type {type(num_int)}")

# 2. Floating-point number (float): Numbers containing a decimal point.
num_float = 5.42 # Example of a float [cite: 24, 46]
print(f"Float Example: {num_float} is of type {type(num_float)}")

# 3. Complex number (complex): Numbers with a real and an imaginary part (j).
num_complex = 8 + 2j # Example of a complex number 
print(f"Complex Example: {num_complex} is of type {type(num_complex)}")


"""
BOOLEAN TYPE (bool)
Boolean is a data type with only two values: True or False.
It is essential for logic and decision-making (control flow) in programming.
"""
x = 10
y = 5

# 4. Boolean - Result of Comparison Operators
# Booleans often result from comparisons like > (greater than) or == (equal to) 
print(f"Is x > y? (10 > 5): {x > y}") # Output: True
print(f"Is x == y? (10 == 5): {x == y}") # Output: False

# 5. Boolean Logic - Logical Operators (and, or, not)
# These operators combine or invert boolean values 
is_morning = True
is_cold = False

# 'and' operator: True only if both are True 
should_stay_inside = is_morning and is_cold
print(f"'and' Logic: {should_stay_inside}") # Output: False

# 'or' operator: True if at least one is True 
is_free = is_morning or is_cold
print(f"'or' Logic: {is_free}") # Output: True

# 'not' operator: Inverts the value 
not_cold = not is_cold
print(f"'not' Logic: {not_cold}") # Output: True