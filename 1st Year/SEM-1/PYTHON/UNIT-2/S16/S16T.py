# ================================
# 📘 Summary: Functions in Python
# ================================

# Definition:
# A function is a block of organized, reusable code
# that performs a single, related action.
# Functions improve modularity, readability, and reusability.

# --------------------------------
# Characteristics of Functions
# --------------------------------
# - Breaks large problems into smaller parts
# - Promotes code reuse
# - Variables inside functions are local (scope control)
# - Functions can return values using 'return'
# - If no return is specified, function returns None

# --------------------------------
# Types of Functions
# --------------------------------
# 1. Built-in Functions → print(), len(), int()
# 2. Functions in Modules → math.sqrt(), random.randint()
# 3. User-defined Functions → created using 'def'

# --------------------------------
# Defining a Function
# --------------------------------
# Syntax:
# def function_name(parameters):
#     """Optional docstring"""
#     # function body
#     return value

# --------------------------------
# Examples
# --------------------------------

# Simple Function
def greet():
    print("Hello, welcome to Python!")

greet()  # Output: Hello, welcome to Python!


# Function with Parameters
def print_info(name, age):
    print(f"{name} is {age} years old.")

print_info("Alice", 30)  # Output: Alice is 30 years old.


# Function with Return Value
def add_numbers(a, b):
    return a + b

result = add_numbers(10, 5)
print("The sum is:", result)  # Output: The sum is: 15


# Default Parameter Values
def describe_pet(animal_type='dog', pet_name='Rex'):
    print(f"I have a {animal_type} and its name is {pet_name}.")

describe_pet()  # Output: I have a dog and its name is Rex.
describe_pet(pet_name='Whiskers', animal_type='cat')  
# Output: I have a cat and its name is Whiskers.


# Recursive Function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))  # Output: 120


# Lambda Function (Anonymous Function)
square = lambda x: x * x
print("Square of 5:", square(5))  # Output: 25


# Function as a Variable
def say_hello():
    print("Hello!")

greet_var = say_hello
greet_var()  # Output: Hello!


# Nested Functions
def outer_function(text):
    def inner_function():
        print(text)
    inner_function()

outer_function("Hello from the inner function!")  
# Output: Hello from the inner function!


# --------------------------------
# Test Yourself (Practice Examples)
# --------------------------------

# 1. Return Larger Number
def max_num(a, b):
    return a if a > b else b

print(max_num(5, 3))  # Output: 5


# 2. Countdown
def countdown(n):
    while n > 0:
        print(n)
        n -= 1

countdown(5)  # Output: 5 4 3 2 1


# 3. Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

print(celsius_to_fahrenheit(0))  # Output: 32.0


# 4. String Length
def string_length(s):
    return len(s)

print(string_length("hello"))  # Output: 5


# 5. Multiply Elements in List
def multiply_list(lst):
    result = 1
    for number in lst:
        result *= number
    return result

print(multiply_list([1, 2, 3, 4]))  # Output: 24


# 6. Reverse String
def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  # Output: olleh


# 7. Palindrome Check
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("radar"))  # Output: True


# --------------------------------
# Exercise Questions (Try Yourself)
# --------------------------------
# 1. Write a function 'contains' that checks if a list contains a specific element.
# 2. Design a function 'concat_strings' that concatenates two given strings.
# 3. Formulate a function 'count_vowels' that counts the number of vowels in a string.
# 4. Establish a function 'sum_range' that calculates the sum of all numbers within a specified range.
