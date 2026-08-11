def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print("Factorial of 5 :", factorial(5))
print("Factorial of 0 :", factorial(0))
print("Factorial of 1 :", factorial(1))

print()

print("------------------------")
