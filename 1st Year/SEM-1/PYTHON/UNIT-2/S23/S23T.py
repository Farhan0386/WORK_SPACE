# ============================================
# Dictionaries in Python – Session 23 Summary
# Instructor: Ms. Jyoti Yadav (KRMU)
# ============================================

# -------------------------------
# Introduction
# -------------------------------
# A dictionary is a built-in Python data type.
# It stores data as key-value pairs.
# Keys must be immutable (string, number, tuple).
# Values can be of any type.
# Dictionaries are mutable → can add, remove, or modify entries.

# Example: Creating a Dictionary
emp = {"Name": "Johnny", "Age": 32, "Salary": 26000, "Company": "TCS"}
print("Employee Dictionary:", emp)
# Output: {'Name': 'Johnny', 'Age': 32, 'Salary': 26000, 'Company': 'TCS'}

# -------------------------------
# Accessing Values
# -------------------------------
name = emp["Name"]
age = emp["Age"]
salary = emp["Salary"]
company = emp["Company"]
print("Name:", name, "Age:", age, "Salary:", salary, "Company:", company)

# -------------------------------
# Modifying and Adding Entries
# -------------------------------
emp["Salary"] = 28000   # Modify existing value
emp["Department"] = "IT"  # Add new key-value pair
print(emp)

# -------------------------------
# Removing Entries
# -------------------------------
del emp["Company"]   # Remove key-value pair
print(emp)

# -------------------------------
# Checking Key Existence
# -------------------------------
if "Department" in emp:
    print("Employee belongs to the", emp["Department"], "department.")
else:
    print("Department info not available.")

# -------------------------------
# Iterating Over Dictionary
# -------------------------------
for key, value in emp.items():
    print(key, ":", value)

# -------------------------------
# Test Yourself Examples
# -------------------------------

# Accessing Values
my_dict = {"Name": "Zara", "Age": 7, "Class": "First"}
print("Name:", my_dict["Name"])
print("Age:", my_dict["Age"])
print("Class:", my_dict["Class"])

# Modifying an Entry
my_dict["Age"] = 8
print("Modified Dictionary:", my_dict)

# Adding a New Entry
my_dict["Grade"] = "A"
print("Updated Dictionary:", my_dict)

# -------------------------------
# Practice Questions
# -------------------------------

# 1. Student Information Dictionary
student = {"name": "Ali", "age": 20, "grade": "A", "school": "KRMU"}
print(student)

# 2. Car Attributes Dictionary
car = {"brand": "Toyota", "model": "Corolla", "year": 2020, "color": "Blue"}
print("Car Brand:", car["brand"], "Year:", car["year"])

# 3. Team Roster Iteration
team = {"Messi": 10, "Ronaldo": 7, "Neymar": 11}
for player, jersey in team.items():
    print(player, ":", jersey)

# 4. Modify Person’s Age
person = {"name": "Ahmed", "age": 25, "city": "Delhi"}
person["age"] = 30
print("Updated Person:", person)

# -------------------------------
# Recap
# -------------------------------
# - Dictionaries store key-value pairs
# - Keys must be unique and immutable
# - Values can be any type
# - Mutable → can add, remove, modify entries
# - Methods: keys(), values(), items()
# - Useful for structured data and mappings
