# ==============================
# 🔁 Looping in Python
# ==============================

"""
Definition:
Loops are used to repeatedly execute a block of code until a specified condition is met or a sequence is fully iterated.
Types of loops in Python:
1. for loop
2. while loop
3. nested loops
"""

# ------------------------------
# 1️⃣ For Loop
# ------------------------------

"""
Definition:
A for loop is used to iterate over a sequence (like list, tuple, string, or range).
Syntax:
for item in iterable:
    # code block
"""

# Example: Iterating over a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# Example: Using range()
for i in range(5):
    print(i)

# Example: Using range with start, stop, step
for x in range(3, 8, 2):
    print(x)

# Example: Using else with for loop
string = "Python Loop"
for s in string:
    if s == "o":
        print("If block")
    else:
        print(s)

# ------------------------------
# 2️⃣ While Loop
# ------------------------------

"""
Definition:
A while loop executes a block of code as long as the condition is true.
Syntax:
while condition:
    # code block
"""

# Example: Counting up
i = 0
while i < 5:
    print(i)
    i += 1

# Example: User input loop
user_input = ''
while user_input != 'quit':
    user_input = input('Enter a word (type "quit" to exit): ')
    print('You entered:', user_input)

# Example: Summing numbers
total = 0
number = 1
while number <= 10:
    total += number
    number += 1
print('The sum is:', total)

# Example: Password check
password = 'secret'
user_input = ''
while user_input != password:
    user_input = input('Enter the password: ')
    if user_input != password:
        print('Incorrect password. Try again.')
print('Password correct. Access granted!')

# ------------------------------
# 3️⃣ Nested Loops
# ------------------------------

"""
Definition:
A nested loop is a loop inside another loop. Useful for matrix operations, pattern printing, etc.
"""

# Example: Nested for loop
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Example: Nested while loop
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

# Example: Multiplication table
for i in range(1, 6):
    for j in range(1, 11):
        print(f"{i} * {j} = {i*j}")

# Example: Pattern printing
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

# ==============================
# 🧪 Practice Prompts
# ==============================

# Squaring numbers in a list
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number ** 2)

# Sum of odd numbers between 1 and 50
total = 0
num = 1
while num <= 50:
    if num % 2 != 0:
        total += num
    num += 1
print("Sum of odd numbers:", total)

# Print names longer than 5 characters
names = ["Alice", "Bob", "Jonathan", "Eve", "Isabelle"]
for name in names:
    if len(name) > 5:
        print(name)

# Factorial using while loop
num = 5
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print("Factorial:", factorial)

# ==============================
# 🔁 Recap
# ==============================

"""
- for loop: Iterates over sequences like lists, strings, or ranges.
- while loop: Executes as long as a condition is true.
- nested loops: Enables multi-level iteration.
- range(): Generates sequences for controlled iteration.
"""
