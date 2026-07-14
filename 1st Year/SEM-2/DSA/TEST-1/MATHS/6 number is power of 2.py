def is_power_of_two(n):
    if n <= 0:
        return False
    
    while n % 2 == 0:
        n //= 2
    
    return n == 1
# Example usage:
number = 16
print(is_power_of_two(number))  # Output: True
number = 18
print(is_power_of_two(number))  # Output: False