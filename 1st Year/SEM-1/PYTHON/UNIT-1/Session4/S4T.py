"""
Python Features:
Simple, interpreted, dynamically typed, strong libraries and IDE support.
"""

"""
Why VS Code:
Lightweight IDE with terminal, Git, IntelliSense, debugging, and venv support.
"""

"""
Linting Tools:
Linting helps catch errors and enforce coding standards before runtime.
flake8 - checks for style issues and unused imports
pylint - deeper analysis for code quality and smells
"""

# pip install flake8 pylint
# flake8 my_script.py
# pylint my_script.py

"""
Black Formatter:
Black is an auto code formatter that enforces PEP 8 style rules.
PEP 8 is the official style guide for Python code — it promotes readability and consistency.
"""

# pip install black
# black my_script.py

"""
Running Python:
Save your code in a .py file and run it using the terminal or Python shell.
"""

# print("Hello, World!")

"""
Indentation:
Indentation refers to spaces at the beginning of a line.
Python uses indentation to define blocks of code instead of braces {}.
All lines in a block must be indented equally.
"""

def greet():
    print("Hello")

"""
Comments:
Used to explain code and improve readability.
Single-line: starts with #
Multi-line: use multiple # or triple quotes ''' '''
Docstring: triple quotes placed after function/class to describe its purpose
"""

# This is a comment
'''This is a multi-line comment'''

def example():
    """This is a docstring"""
    pass

"""
Blank Lines:
Used to separate code sections and improve readability.
You can print blank lines using newline character \n.
"""

print("\n" * 3)

"""
Quotations:
Python supports single (' '), double (" "), and triple (''' ''' or """ """) quotes.
Triple quotes are used for multi-line strings or docstrings.
"""

text1 = 'Hello'
text2 = "World"
text3 = '''Multi-line'''

"""
Multi-line Statements:
Use backslash \ or wrap the statement in parentheses to continue across lines.
"""

total = (1 + 2 +
         3 + 4)

"""
Keywords:
Reserved words that define Python's syntax and structure.
Examples: if, else, elif, for, while, def, return, class, import, try, except
"""

import keyword
print(keyword.kwlist)

"""
Even/Odd Example
"""

def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

"""
Maximum of Two
"""

def find_maximum(a, b):
    if a > b:
        return a
    else:
        return b

"""
Factorial Function
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

"""
Try-Except Example:
Used for error handling. Prevents program crash on exceptions.
"""

def divide(x, y):
    try:
        print("Result:", x / y)
    except ZeroDivisionError:
        print("Error: Division by zero!")

"""
Loops Example:
for loop - iterates over a sequence
while loop - runs until a condition becomes false
"""

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

count = 0
while count < 5:
    print("Count:", count)
    count += 1

"""
Class Example:
A class is a blueprint for creating objects.
__init__ is the constructor method that initializes object attributes.
"""

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} barks!")

my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()
