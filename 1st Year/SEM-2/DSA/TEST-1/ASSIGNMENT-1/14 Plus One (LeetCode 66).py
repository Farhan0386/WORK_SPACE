def plus_one(digits):
    n = len(digits)
    
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    
    # If all digits were 9
    return [1] + digits
# Example usage
digits = [1, 2, 3]
result = plus_one(digits)
print(f"The result after adding one is: {result}")