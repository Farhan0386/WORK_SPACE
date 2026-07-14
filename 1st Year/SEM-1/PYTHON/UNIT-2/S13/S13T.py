# ----------------------------------------
"""
Conditional Statements in Python

These are used to make decisions in code based on conditions.
Python supports:
- if
- if-else
- if-elif-else
- nested if-else
"""
# Example: Simple if-else
x = 10
if x > 0:
    print("Positive number")
else:
    print("Non-positive number")

# ----------------------------------------
"""
Nested Conditional Statements

An if statement placed inside another if statement.
Used when decisions depend on previous conditions.
Indentation defines nesting levels.
"""
# Example: Nested if-else
num = 5
if num >= 0:
    if num == 0:
        print("Number is 0")
        
    else:
        print("Number is positive")
else:
    print("Number is negative")

# ----------------------------------------
"""
Nested Conditional Exercise

Task 1:
Check if a number is positive, negative, or zero.
If positive, check if it's even or odd.

Task 2:
Find the largest among three numbers.
If multiple values are equally the largest, indicate that.
"""
# Example: Task 1
n = int(input("Enter a number: "))
if n > 0:
    if n % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
elif n == 0:
    print("Zero")
else:
    print("Negative number")

# ----------------------------------------
"""
Multi-way Branching (if-elif-else)

Used when multiple conditions need to be checked sequentially.
Executes the first block whose condition is true.
"""
# Example: Grade calculation
score = 85
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")

# ----------------------------------------
"""
Multi-way Branching Exercise

Task 1:
Check if a number is positive, negative, or zero.

Task 2:
Determine grade from score using scale:
A (90–100), B (80–89), C (70–79), D (60–69), F (0–59)

Task 3:
Check if a year is a leap year.
Leap year rules:
- Divisible by 4
- Not divisible by 100 unless also divisible by 400

Task 4:
Print number of days in a month (1–12).
Assume February has 28 days.

Task 5:
Find the largest among three integers.
"""
# Example: Leap year check
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

# ----------------------------------------
"""
Review Summary

- if: Executes block if condition is true.
- if-else: Executes one of two blocks.
- if-elif-else: Checks multiple conditions in sequence.
- nested if-else: Enables complex decision-making.
"""
# Example: if-elif-else
day = 3
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
else:
    print("Invalid day number")