def is_armstrong(n):
    original = n
    n = abs(n)
    
    digits = len(str(n))
    total = 0
    temp = n
    
    while temp > 0:
        digit = temp % 10
        total += digit ** digits
        temp //= 10
    
    return total == original
# Example usage:
number = 153
print(is_armstrong(number))  # Output: True
number = 123
print(is_armstrong(number))  # Output: False