def count_digits(n):
    if n == 0:
        return 1
    
    count = 0
    n = abs(n)   # handle negative numbers
    
    while n > 0:
        n //= 10
        count += 1
        
    return count
print(count_digits(12345))  # Output: 5
print(count_digits(-9876))  # Output: 4
print(count_digits(0))  # Output: 1