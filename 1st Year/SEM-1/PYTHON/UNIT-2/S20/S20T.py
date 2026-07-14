# ============================================
# Lists in Python – Session 20 Summary
# Instructor: Ms. Jyoti Yadav (KRMU)
# ============================================

# -------------------------------
# Introduction
# -------------------------------
# Lists are ordered collections of items, enclosed in square brackets [ ].
# They can contain elements of different data types (int, float, string, complex, etc.).
# Lists are mutable → elements can be added, removed, or modified.

# Example: Creating Lists
list1 = [1, 2, "Python", "Program", 15.9]
print(list1)  # Output: [1, 2, 'Python', 'Program', 15.9]

list2 = [25.50, True, -55, 1+2j]
print(list2)  # Output: [25.5, True, -55, (1+2j)]

# -------------------------------
# Indexing and Slicing
# -------------------------------
# Indexing starts at 0, negative indexing starts at -1.
# Slicing uses colon (:) to extract sublists.

my_list = [1, 2, 3, 4, 5]
print(my_list[0])     # Output: 1
print(my_list[-1])    # Output: 5
print(my_list[1:3])   # Output: [2, 3]

# -------------------------------
# List Methods
# -------------------------------
# append() → add element at end
# insert() → add element at specific index
# remove() → remove first occurrence of element
# extend() → add elements from another list
# count() → count occurrences
# + operator → concatenate lists

# Append
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

# Insert
my_list = [1, 2, 3, 4, 5]
my_list.insert(2, 10)
print(my_list)  # Output: [1, 2, 10, 3, 4, 5]

# Remove
my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)  # Output: [1, 2, 4, 5]

# Extend
my_list = [1, 2, 3, 4, 5]
another_list = [7, 8, 9]
my_list.extend(another_list)
print(my_list)  # Output: [1, 2, 3, 4, 5, 7, 8, 9]

# Concatenate
combined_list = [1, 2, 3] + [4, 5]
print(combined_list)  # Output: [1, 2, 3, 4, 5]

# Count
my_list = [1, 2, 3, 4, 5]
print(my_list.count(10))  # Output: 0

# Membership
print(10 in my_list)  # Output: False

# -------------------------------
# Practice Questions
# -------------------------------

# 1. Reverse list without reverse()
def reverse_list(lst):
    return lst[::-1]

print(reverse_list([1, 2, 3, 4]))  # Output: [4, 3, 2, 1]

# 2. Find largest and smallest without max()/min()
def find_min_max(lst):
    smallest = lst[0]
    largest = lst[0]
    for num in lst:
        if num < smallest:
            smallest = num
        if num > largest:
            largest = num
    return smallest, largest

print(find_min_max([3, 7, 2, 9, 5]))  # Output: (2, 9)

# 3. Remove duplicates while maintaining order
def remove_duplicates(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]

# 4. Find pairs with a given sum
def find_pairs(lst, target):
    pairs = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
    return pairs

print(find_pairs([1, 2, 3, 4, 5], 6))  # Output: [(1, 5), (2, 4)]

# -------------------------------
# Recap
# -------------------------------
# - Lists are mutable ordered collections
# - Access via indexing, slicing, negative indexing
# - Methods: append(), insert(), remove(), extend(), count()
# - Operators: + for concatenation, 'in' for membership
# - Lists are fundamental data structures in Python
