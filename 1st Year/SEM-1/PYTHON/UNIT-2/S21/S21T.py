# ============================================
# Tuples in Python – Session 21 Summary
# Instructor: Ms. Jyoti Yadav (KRMU)
# ============================================

# -------------------------------
# Introduction
# -------------------------------
# Tuples are ordered, immutable collections of items.
# Defined using parentheses ( ) and commas.
# Can contain mixed data types and allow duplicates.

# Example: Creating Tuples
tuple1 = (1, 2, 3)
tuple2 = ("apple", "banana", "cherry")
print(tuple1)  # Output: (1, 2, 3)
print(tuple2)  # Output: ('apple', 'banana', 'cherry')

# -------------------------------
# Accessing Elements
# -------------------------------
print(tuple1[0])   # Output: 1
print(tuple2[-1])  # Output: cherry

# -------------------------------
# Concatenation and Repetition
# -------------------------------
new_tuple1 = tuple1 + (4, 5)
new_tuple2 = tuple2 + ("date",)
print(new_tuple1)  # Output: (1, 2, 3, 4, 5)
print(new_tuple2)  # Output: ('apple', 'banana', 'cherry', 'date')

repeated_tuple1 = tuple1 * 2
repeated_tuple2 = tuple2 * 3
print(repeated_tuple1)  # Output: (1, 2, 3, 1, 2, 3)
print(repeated_tuple2)  # Output: ('apple','banana','cherry','apple','banana','cherry','apple','banana','cherry')

# -------------------------------
# Tuple Operations
# -------------------------------
# Count occurrences
count1 = tuple1.count(1)
count2 = tuple2.count("banana")
print(count1)  # Output: 1
print(count2)  # Output: 1

# Find index
index1 = tuple1.index(3)
index2 = tuple2.index("apple")
print(index1)  # Output: 2
print(index2)  # Output: 0

# -------------------------------
# Unpacking and Iterating
# -------------------------------
a, b, c = tuple1
x, y, z = tuple2
print(a, b, c)  # Output: 1 2 3
print(x, y, z)  # Output: apple banana cherry

for item in tuple1:
    print(item)  # Output: 1 2 3

for item in tuple2:
    print(item)  # Output: apple banana cherry

# -------------------------------
# Test Yourself Examples
# -------------------------------

# Tuple Creation
my_tuple = (1, 'hello', 3.14)
print(my_tuple)  # Output: (1, 'hello', 3.14)

# Tuple Concatenation
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
concatenated_tpl = tuple1 + tuple2
print("Concatenated Tuple:", concatenated_tpl)  # Output: (1, 2, 3, 'a', 'b', 'c')

# Tuple Slicing
original_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
sliced_tuple = original_tuple[2:6]
print("Sliced Tuple:", sliced_tuple)  # Output: (3, 4, 5, 6)

# Tuple Membership
my_tuple = (1, 2, 3, 4, 5)
element = 3
if element in my_tuple:
    print(f"{element} exists in the tuple.")  # Output: 3 exists in the tuple.

# Tuple Length
my_tuple = (1, 2, 3, 4, 5)
print("Length of Tuple:", len(my_tuple))  # Output: 5

# Counting Elements
my_tuple = (1, 2, 2, 3, 2, 4, 2, 5)
element = 2
count = my_tuple.count(element)
print(f"Count of {element}:", count)  # Output: 4

# Tuple Repetition
my_tuple = (1, 2, 3)
repeated_tuple = my_tuple * 3
print("Repeated Tuple:", repeated_tuple)  # Output: (1,2,3,1,2,3,1,2,3)

# Iterating Over Tuple
my_tuple = (1, 2, 3, 4, 5)
for item in my_tuple:
    print(item)  # Output: 1 2 3 4 5

# -------------------------------
# Practice Questions
# -------------------------------
# 1. Check if element exists in tuple
def check_membership(tpl, element):
    return element in tpl

print(check_membership((1,2,3), 2))  # Output: True

# 2. Repeat tuple elements
def repeat_tuple(tpl, times):
    return tpl * times

print(repeat_tuple((1,2), 3))  # Output: (1,2,1,2,1,2)

# 3. Iterate over tuple
def iterate_tuple(tpl):
    for item in tpl:
        print(item)

iterate_tuple(("apple","banana","cherry"))

# 4. Demonstrate immutability
immutable_tuple = (1,2,3)
try:
    immutable_tuple[0] = 10
except TypeError as e:
    print("Error:", e)  # Output: Error: 'tuple' object does not support item assignment

# -------------------------------
# Recap
# -------------------------------
# - Tuples are ordered and immutable
# - Created with parentheses ()
# - Support indexing, slicing, concatenation, repetition
# - Methods: count(), index()
# - Useful for fixed collections of items
