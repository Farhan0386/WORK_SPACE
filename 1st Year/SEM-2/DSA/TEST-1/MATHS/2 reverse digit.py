def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10
    
    return sign * reversed_num
print(reverse_number(12345))  # Output: 54321
print(reverse_number(-9876))  # Output: -6789