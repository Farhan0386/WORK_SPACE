def is_palindrome(n):
    if n < 0:
        return False
    
    original = n
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    
    return original == reversed_num

# Example usage:
number = 121    
print(is_palindrome(number))  # Output: True
number = -121
print(is_palindrome(number))  # Output: False