# ============================================
# Python Control Structures: Loops, Break, Continue
# Session 15 Summary 
# ============================================

# -------------------------------
# For Loop
# -------------------------------
# Iterates over a sequence (list, tuple, string, etc.)
# Executes a block of code for each item

for item in [1, 2, 3]:
    print(item)  # Output: 1 2 3

# -------------------------------
# While Loop
# -------------------------------
# Repeats a block of code as long as a condition is True

i = 0
while i < 3:
    print(i)  # Output: 0 1 2
    i += 1

# -------------------------------
# Else Clause with Loops
# -------------------------------
# Executes after loop ends normally (not via break)

for i in range(3):
    print(i)
else:
    print("Loop completed")  # Output: Loop completed

# -------------------------------
# Break Statement
# -------------------------------
# Terminates the loop prematurely when a condition is met

for i in range(5):
    if i == 3:
        break
    print(i)  # Output: 0 1 2

# -------------------------------
# Continue Statement
# -------------------------------
# Skips the current iteration and continues with the next

for i in range(5):
    if i == 2:
        continue
    print(i)  # Output: 0 1 3 4

# -------------------------------
# Test Yourself Examples
# -------------------------------

# Break when number is 5
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num == 5:
        break
    print(num)  # Output: 1 2 3 4

# Continue to skip odd numbers
for num in range(1, 11):
    if num % 2 == 1:
        continue
    print(num)  # Output: 2 4 6 8 10

# Break in nested loops
for i in range(3):
    for j in range(3):
        if j == 2:
            break
        print(f"({i}, {j})")
# Output: (0,0) (0,1) (1,0) (1,1) (2,0) (2,1)

# Continue in nested loops
for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(f"({i}, {j})")
# Output: (0,0) (0,2) (1,0) (1,2) (2,0) (2,2)

# Break on empty input
while True:
    data = input("Enter a value (or press Enter to exit): ")
    if not data:
        break
    print("You entered:", data)

# Break when specific value is found
numbers = [10, 20, 30, 40, 50]
search_value = 30
for num in numbers:
    if num == search_value:
        print(f"Found {search_value} in the list.")
        break
else:
    print(f"{search_value} not found in the list.")

# Continue to print only odd numbers
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(f"Odd number: {i}")  # Output: 1 3 5

# Continue to skip even numbers and print squares
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        continue
    print(f"Square of {num} is {num ** 2}")  # Output: 1, 9, 25

# Break when condition in nested loop is met
for i in range(3):
    for j in range(3):
        if i == j:
            break
        print(f"({i}, {j})")
# Output: (0,1) (0,2) (1,0) (1,2) (2,0) (2,1)

# -------------------------------
# Practice Questions
# -------------------------------

# Q1: Skip multiples of 7 using continue
for i in range(1, 51):
    if i % 7 == 0:
        continue
    print(i)

# Q2: Sum even numbers from user input, break on non-numeric
try:
    user_input = input("Enter numbers separated by commas: ")
    numbers = user_input.split(",")
    total = 0
    for num in numbers:
        if not num.strip().isdigit():
            break
        if int(num) % 2 == 0:
            total += int(num)
    print("Sum of even numbers:", total)
except:
    print("Invalid input")

# Q3: Generate random numbers until one > 7 is found
import random
count = 0
while True:
    num = random.randint(1, 10)
    count += 1
    if num > 7:
        break
print("Numbers generated:", count)

# -------------------------------
# Recap
# -------------------------------
# break → exits loop early
# continue → skips current iteration

