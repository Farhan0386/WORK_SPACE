# ==============================
# 📘 Topic Definitions
# ==============================

"""
Definition: Control Structures
Control structures are the building blocks of programming logic.
They allow programs to:
- Make decisions based on conditions
- Repeat tasks using loops
- Control the flow of execution using statements like break and continue
"""

"""
Definition: Conditional Statements
Conditional statements enable selective execution of code blocks.
They evaluate expressions and execute code only when conditions are met.
Types include:
- if
- if-else
- nested if
- if-elif-else ladder
"""

# ==============================
# ✅ One-way Decision: if Statement
# ==============================

# Example 1: Basic comparison
x = 3
y = 10
if x < y:
    print("x is smaller than y.")

# Example 2: Multiple independent conditions
age = 18
isGraduated = True
hasLicense = True

if age >= 18:
    print("You're 18 or older. i.e adulthood!")
if isGraduated:
    print("Congratulations on your graduation!")
if hasLicense:
    print("Happy driving!")

# ==============================
# 🧪 Exercises on if Statement
# ==============================

# Exercise 1
x = 3
y = 10
z = None
if x < y:
    z = 13
    print(f"Variable z is now {z}.")

# Exercise 2
x = 3
y = 10
if x > y:
    print("x is greater than y.")  # No output expected

# Exercise 3
x = 200
y = 1000
if (x < y) or (y / 11 == 0):
    print("At least one condition is true")

# Exercise 4
number = 6
if number > 5:
    print(number * number)
print("Next lines of code")

# Exercise 5
s = 3000
t = 1000
if s > t and t / 2 == 0:
    print("Both conditions are true")  # No output expected

# ==============================
# 🔄 Two-way Decision: if-else Statement
# ==============================

# Example 1: Password check
password = "PYnative@29"
if password == "PYnative@29":
    print("Correct password")
else:
    print("Incorrect Password")

# Example 2: Value comparison
i = 20
if i < 15:
    print("i is smaller than 15")
    print("I'm in if Block")
else:
    print("i is greater than 15")
    print("I'm in else Block")
print("I'm not in if and not in else Block")

# ==============================
# 🧪 Exercises on if-else Statement
# ==============================

# Instance 1
x = 20
if x < 50:
    print("first suite")
    print("x is small")
else:
    print("second suite")
    print("x is large")

# Instance 2
x = 3
y = 3
if x < y:
    print("x is smaller than y.")
else:
    print("x is greater than y.")

# Instance 3
number = 6
if number >= 6:
    print(number, "Positive Number")
else:
    print(number, "Negative Number")
print("Outside If block")

# Instance 4
a = 9
if a > 5 and a < 10:
    print("Hello")
else:
    print("Bye")

# ==============================
# 🧮 Practice Problems
# ==============================

# Problem 1: Find maximum of two numbers
a = 15
b = 22
if a > b:
    print("Maximum is", a)
else:
    print("Maximum is", b)

# Problem 2: Add 7 if odd, else add 4
N = 11
if N % 2 != 0:
    N += 7
else:
    N += 4
print("Updated value:", N)

# Problem 3: Simple number guessing game
secret = 7
guess = int(input("Guess the number: "))
if guess == secret:
    print("You win!")
else:
    print("You lose!")

# ==============================
# 📌 Review
# ==============================

"""
Review:
- The if statement executes code only when a condition is true.
- The if-else statement provides an alternate path when the condition is false.
- Logical operators (and, or, not) help combine multiple conditions.
- Control structures are essential for dynamic and responsive programs.
"""