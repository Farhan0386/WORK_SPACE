# A list comprehension is a concise way to create lists using a loop and expression in one line.
numbers = [1, 2, 3, 4, 5]
squares = [n**2 for n in numbers]
print("Squares:", squares)

# 2. Simple Arithmetic Expressions
print("\n2. Simple Arithmetic Expressions")
# Apply arithmetic operations directly in the expression.
double = [n * 2 for n in numbers]
print("Doubled:", double)

# 3. String Manipulation
print("\n3. String Manipulation")
# Modify strings using list comprehension.
words = ["hello", "world", "python"]
uppercased = [word.upper() for word in words]
print("Uppercased:", uppercased)

# 4. Conditional Expressions
print("\n4. Conditional Expressions")
# Filter items based on a condition.
even_numbers = [n for n in numbers if n % 2 == 0]
print("Even Numbers:", even_numbers)

# 5. Conditional with Else (Ternary)
print("\n5. Conditional with Else (Ternary)")
# Use if-else inside the comprehension.
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers]
print("Labels:", labels)

# 6. Using Functions in Expressions
print("\n6. Using Functions in Expressions")
# Apply a function to each item.
def cube(x):
    return x**3

cubes = [cube(n) for n in numbers]
print("Cubes:", cubes)

# 7. Nested Loops in Comprehensions
print("\n7. Nested Loops in Comprehensions")
# Combine items from two lists.
list1 = [1, 2]
list2 = ['a', 'b']
pairs = [(x, y) for x in list1 for y in list2]
print("Pairs:", pairs)

# 8. Filtering with Multiple Conditions
print("\n8. Filtering with Multiple Conditions")
# Apply more than one condition.
filtered = [n for n in range(10) if n > 2 and n % 2 == 0]
print("Filtered:", filtered)

# 9. Complex Expressions
print("\n9. Complex Expressions")
# Use expressions with multiple operations.
complex_result = [(n**2 + 1) for n in numbers]
print("Complex Result:", complex_result)

# 10. List Comprehension with range()
print("\n10. List Comprehension with range()")
# Use range directly.
range_list = [x for x in range(5)]
print("Range List:", range_list)

# 11. Flattening Lists
print("\n11. Flattening Lists")
# Flatten a 2D list.
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [item for sublist in matrix for item in sublist]
print("Flattened:", flat)

# 12. Using Built-in Functions
print("\n12. Using Built-in Functions")
# Use built-in functions like len().
lengths = [len(word) for word in words]
print("Lengths:", lengths)

# 13. Removing Duplicates
print("\n13. Removing Duplicates")
# Convert to set and back to list.
data = [1, 2, 2, 3, 3, 3]
unique = list(set(data))
print("Unique:", unique)

# 14. Using zip() with Comprehensions
print("\n14. Using zip() with Comprehensions")
# Combine elements from two lists.
list_a = [10, 20, 30]
list_b = [1, 2, 3]
summed = [a + b for a, b in zip(list_a, list_b)]
print("Summed:", summed)

# 15. Performance Note
print("\n15. Performance Note")
# List comprehensions are faster than loops but should remain readable.
# Avoid overly complex logic inside comprehensions.