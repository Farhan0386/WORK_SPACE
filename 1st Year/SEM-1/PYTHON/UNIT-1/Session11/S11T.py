# 🧵 STRING BASICS
# Definition: A string is a sequence of characters enclosed in quotes.
single_quote = 'Hello'
double_quote = "World"
triple_quote = '''Multiline
String'''

print(single_quote)
print(double_quote)
print(triple_quote)

# Strings are immutable: cannot be changed after creation
immutable_example = "Python"
# immutable_example[0] = 'J'  # ❌ This will raise an error

# 🔢 INDEXING & SLICING
# Indexing: Access characters by position
s = "Python"
print(s[0])      # Output: P
print(s[-1])     # Output: n

# Slicing: Extract substrings
print(s[1:4])    # Output: yth
print(s[::2])    # Output: Pto

# ➕ CONCATENATION
# Combine strings using '+' or join()
greeting = "Hello"
name = "Farhan"
message = greeting + ", " + name
print(message)   # Output: Hello, Farhan

words = ["Python", "is", "fun"]
joined = " ".join(words)
print(joined)    # Output: Python is fun

# 🔡 ESCAPE CHARACTERS
# Special characters prefixed with '\'
print("Line1\nLine2")       # Newline
print("Column1\tColumn2")   # Tab
print("She said, \"Hi\"")   # Double quote
print("Path: C:\\Users\\Farhan")  # Backslash

# 🧩 STRING FORMATTING
# Using format()
name = "Alice"
age = 21
print("My name is {} and I am {} years old.".format(name, age))

# Using f-strings
height = 1.75
print(f"My name is {name} and I am {age} years old. I am {height:.2f} meters tall.")

# 🛠️ BUILT-IN STRING METHODS
sample = "  Hello, World!  "

print(sample.upper())       # HELLO, WORLD!
print(sample.lower())       # hello, world!
print(sample.capitalize())  # Hello, world!
print(sample.strip())       # Hello, World!
print(sample.replace("World", "Python"))  # Hello, Python!
print(sample.split(","))    # ['  Hello', ' World!  ']
print(" ".join(["Python", "3.10"]))       # Python 3.10
print(sample.find("World")) # 9
print(sample.index("World"))# 9
print(sample.count("l"))    # 3
print(sample.startswith(" "))  # True
print(sample.endswith("!  "))  # True
print("abc".isalpha())      # True
print("abc123".isalnum())   # True

# 🧠 INTERVIEW INSIGHTS
# Reverse a string
rev = sample[::-1]
print(rev)

# Palindrome check
word = "madam"
is_palindrome = word == word[::-1]
print(is_palindrome)  # True

# Slicing vs Indexing
print(word[0])     # m (indexing)
print(word[1:4])   # ada (slicing)
# Slicing returns a substring, indexing returns a single character