# ============================================
# Strings in Python – Session 19 Summary
# Instructor: Ms. Jyoti Yadav (KRMU)
# ============================================

# -------------------------------
# Introduction
# -------------------------------
# Strings are sequences of characters enclosed in quotes:
# - Single quotes (' ')
# - Double quotes (" ")
# - Triple quotes (''' ''' or """ """)
# Strings are immutable (cannot be changed once created).

# Example: Creating Strings
str1 = 'Hello Python'
print(str1)  # Output: Hello Python

str2 = "Hello Python"
print(str2)  # Output: Hello Python

str3 = '''Triple quotes are generally used for multi-line strings'''
print(str3)

# -------------------------------
# Indexing and Slicing
# -------------------------------
# Indexing starts at 0 (left to right).
# Negative indexing starts at -1 (right to left).
# Slicing uses colon (:) to extract substrings.

s = "HELLO"
print(s[0])    # Output: H
print(s[1:4])  # Output: ELL
print(s[-1])   # Output: O

# -------------------------------
# Slicing Example
# -------------------------------
s = "Hello, world!"
print(s[0])      # Output: H
print(s[1:5])    # Output: ello
print(s[-1])     # Output: !

# -------------------------------
# Splitting and Joining
# -------------------------------
text = "apple,banana,cherry"
print(text.split(","))  # Output: ['apple', 'banana', 'cherry']

words = ['Python', 'is', 'awesome']
print(" ".join(words))  # Output: Python is awesome

# -------------------------------
# String Properties
# -------------------------------
filename = "example.txt"
print(filename.endswith(".txt"))  # True
print(filename.startswith("ex"))  # True
print("1234".isdigit())           # True
print("abc".isalpha())            # True
print("abc123".isalnum())         # True

# -------------------------------
# String Methods
# -------------------------------
print("hello".upper())   # Output: HELLO
print("HELLO".lower())   # Output: hello

user_input = " Python "
print(user_input.strip())  # Output: Python

text = "Hello, world!"
print(text.replace("world", "Python"))  # Output: Hello, Python!
print(text.find("world"))               # Output: 7

# -------------------------------
# Practice Questions
# -------------------------------
# 1. Replace all vowels with '*'
def replace_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join('*' if ch in vowels else ch for ch in s)

print(replace_vowels("Hello World"))  # Output: H*ll* W*rld

# 2. Count vowels and consonants
def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count = sum(1 for ch in s if ch in vowels)
    c_count = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
    return v_count, c_count

print(count_vowels_consonants("Hello"))  # Output: (2, 3)

# 3. Capitalize first and last letters of each word
def capitalize_first_last(s):
    words = s.split()
    result = []
    for word in words:
        if len(word) > 1:
            word = word[0].upper() + word[1:-1] + word[-1].upper()
        else:
            word = word.upper()
        result.append(word)
    return " ".join(result)

print(capitalize_first_last("python is fun"))  # Output: PythoN IS FuN

# 4. Character frequency
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

print(char_frequency("hello"))  # Output: {'h':1, 'e':1, 'l':2, 'o':1}

# -------------------------------
# Recap
# -------------------------------
# - Strings are immutable sequences of characters
# - Access via indexing, slicing, negative indexing
# - Useful methods: upper(), lower(), strip(), replace(), split(), join(), find()
# - Strings are fundamental in Python programming
