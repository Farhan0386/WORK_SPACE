def sum_of_digits(n):
    n = abs(n)
    total = 0
    
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    
    return total

# Example usage:
number = 12345
print(sum_of_digits(number))  # Output: 15