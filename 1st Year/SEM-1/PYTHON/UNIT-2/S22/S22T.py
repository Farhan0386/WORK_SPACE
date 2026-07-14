# ============================================
# Sets in Python – Session 22 Summary
# Instructor: Ms. Jyoti Yadav (KRMU)
# ============================================

# -------------------------------
# Introduction
# -------------------------------
# A set is a collection of unique, unordered items.
# - Elements must be immutable (int, float, string, tuple).
# - Sets are mutable → can add/remove elements.
# - Duplicates are automatically removed.
# - Defined using curly braces { } or set() constructor.

# Example: Creating Sets
my_set = {1, 2, 3}
another_set = set([4, 5, 6])
print(my_set)       # Output: {1, 2, 3}
print(another_set)  # Output: {4, 5, 6}

# -------------------------------
# Adding and Updating Elements
# -------------------------------
my_set.add(4)              # Adds single element
my_set.update([5, 6, 7])   # Adds multiple elements
print(my_set)              # Output: {1, 2, 3, 4, 5, 6, 7}

# -------------------------------
# Set Operations
# -------------------------------
A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)  # Union → {1, 2, 3, 4, 5}
print(A & B)  # Intersection → {3}
print(A - B)  # Difference → {1, 2}
print(A ^ B)  # Symmetric Difference → {1, 2, 4, 5}

# -------------------------------
# Test Yourself Examples
# -------------------------------

# Union
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

# Intersection
print(set1 & set2)  # Output: {3}

# Difference
print(set1 - set2)  # Output: {1, 2}

# Symmetric Difference
print(set1 ^ set2)  # Output: {1, 2, 4, 5}

# Add, Update, Remove
set1.add(6)          # Adds 6
set1.update([7, 8])  # Adds 7 and 8
set1.remove(1)       # Removes 1
print(set1)

# -------------------------------
# Exercises
# -------------------------------

# 1. Basic Set Creation
fruits = {"apple", "banana", "cherry"}
print(fruits)

# 2. Adding Items
fruits.add("orange")
print(fruits)

# 3. Removing Items
# remove() → raises error if item not found
# discard() → does not raise error
fruits.remove("banana")   # Removes banana
fruits.discard("banana")  # Safe discard
print(fruits)

# -------------------------------
# Recap
# -------------------------------
# - Sets store unique, unordered items
# - Mutable (can add/remove elements)
# - Not indexed → cannot access by position
# - Useful for membership tests and mathematical set operations
# - Common methods: add(), update(), remove(), discard()
