# ================================
# 📘 Summary: Python Functions (Args, Kwargs, Docstrings, Type Hints)
# ================================

# --------------------------------
# Keyword vs Positional Arguments
# --------------------------------
# - Keyword arguments → passed using parameter names (order doesn’t matter).
# - Positional arguments → passed in the order of parameters (order matters).

# Keyword Arguments Example
def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is", age)

nameAge(name="Prince", age=20)
nameAge(age=20, name="Prince")
# Output: Hi, I am Prince / My age is 20


# Positional Arguments Example
print("Case-1:")
nameAge("Prince", 20)   # Correct order
print("\nCase-2:")
nameAge(20, "Prince")   # Wrong order → swapped meaning


# --------------------------------
# *args → Variable-length Positional Arguments
# --------------------------------
# Collects multiple values into a tuple.

def myFun(*argv):
    for arg in argv:
        print(arg)

myFun('Hello', 'Welcome', 'to', 'KRMU')
# Output: Hello, Welcome, to, KRMU


def fun(arg1, *argv):
    print("First argument:", arg1)
    for arg in argv:
        print("Argument *argv:", arg)

fun('Hello', 'Welcome', 'to', 'KRMU')


# --------------------------------
# **kwargs → Variable-length Keyword Arguments
# --------------------------------
# Collects multiple keyword arguments into a dictionary.

def fun(**kwargs):
    for k, val in kwargs.items():
        print(f"{k} == {val}")

fun(s1="How", s2="are", s3="you")
# Output: s1 == How, s2 == are, s3 == you


# Using both *args and **kwargs
def mix_fun(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

mix_fun(1, 2, 3, a=4, b=5)
# Output: Positional arguments: (1, 2, 3)
#         Keyword arguments: {'a': 4, 'b': 5}


# --------------------------------
# Docstrings
# --------------------------------
# - Docstrings document functions, classes, modules.
# - Declared using triple quotes (""" or ''').
# - Accessed via __doc__ or help().

# Single-line Docstring
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

print("Sum:", add(5, 3))  # Output: 8
print(add.__doc__)        # Output: Return the sum of two numbers.


# Multi-line Docstring
def add_numbers(a, b):
    """
    This function takes two numbers as input and returns their sum.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of a and b.
    """
    return a + b

print(add_numbers(3, 5))  # Output: 8


# Docstring in Classes
class Student:
    """Represents a student with name and age."""

    def __init__(self, name: str, age: int):
        """Initialize student with name and age."""
        self.name = name
        self.age = age

    def info(self):
        """Return student info as string."""
        return f"{self.name} is {self.age} years old."

s = Student("Farhan", 21)
print(s.info())


# --------------------------------
# Type Hints
# --------------------------------
# - Improve readability and allow static type checking.
# - Syntax: variable: type, function args: type, return: -> type

age: int = 25

def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Farhan"))


# Function Return Type
def add_numbers(x: int, y: int) -> int:
    return x + y

print(add_numbers(10, 5))  # Output: 15


# Optional Types and Collections
from typing import Optional, List, Tuple

def get_user(id: int) -> Optional[str]:
    return None if id == 0 else "User"

def sum_numbers(nums: List[int]) -> int:
    return sum(nums)

def get_name_and_age() -> Tuple[str, int]:
    return ("Abc", 25)

print(get_user(0))             # Output: None
print(sum_numbers([1, 2, 3]))  # Output: 6
print(get_name_and_age())      # Output: ('Abc', 25)
