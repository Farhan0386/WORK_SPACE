"""
Topic: Understanding Variables in Python
Variables are used to store data.
They can be short (x, y) or descriptive (age, total_volume).
"""

x = 5
name = "John"
is_student = True
x = 10  # reassignment

"""
Variable Naming Rules:
- Only letters, numbers, and underscores
- Cannot start with a number
- Case-sensitive
"""

my_var = 10
MyVar = 20  # different from my_var

"""
Variable Naming Conventions:
- Use lowercase
- Use underscores for multiple words
- Be clear and concise
"""

user_input = "Hello"
num_of_items = 5

"""
Variable Declaration:
No need to declare type.
Type is inferred from the assigned value.
"""

a = 100       # int
b = "Python"  # str
c = 3.14      # float

"""
Type Examples:
Assigning values creates the variable with its type.
"""

x = 2
print(x)
print(type(x))  # <class 'int'>

x = '2'
print(x)
print(type(x))  # <class 'str'>

x = 2.0
print(x)
y = float(2) # converts int to float
print(y)

"""
Working with Variables:
- Declaration
- Assignment
- Manipulation
- Printing
- Deletion
"""

x = 10    # declaration and assignment
x = x + 5 # manipulation
print(x)  # printing
del x     # deletion

"""
Local and Global Variables:
- Local: inside functions
- Global: outside functions
"""

my_var = "global"

def my_func():
    print(my_var)  # accesses global variable

my_func()

print()

def another_func(): # defines a local variable
    my_var = "local"
    print(my_var)

another_func()

"""
Using global keyword:
Allows modifying global variable inside a function
"""

def update_var():  # uses global keyword
    global my_var
    my_var = "updated globally"

update_var()
print(my_var)

"""
Understanding Numbers in Python:
Supports int, float, and arithmetic operations
"""

x = 5       # int
y = 3.14    # float

sum = x + y
difference = x - y
product = x * y
quotient = x / y

print(sum, difference, product, quotient)

"""
Temperature Conversion Example
"""

celsius = 20
fahrenheit = (celsius * 9/5) + 32
print("Celsius:", celsius, "C")
print("Fahrenheit:", fahrenheit, "F")

fahrenheit = 68
celsius = (fahrenheit - 32) * 5/9
print("Fahrenheit:", fahrenheit, "F")
print("Celsius:", celsius, "C")

"""
Simple Interest Calculation
"""

principal = 1000
rate = 5
time = 2
simple_interest = (principal * rate * time) / 100

print("Principal Amount:", principal)
print("Rate of Interest:", rate, "%")
print("Time Period:", time, "years")
print("Simple Interest:", simple_interest)