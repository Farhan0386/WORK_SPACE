# -------------------------------
# Scalar Data Types (Immutable)
# -------------------------------

'''
int: Represents whole numbers without decimals.
Immutable and belongs to the 'int' class.
'''
x = 10
print("int:", x, "| type:", type(x))

'''
float: Represents numbers with decimal points.
Belongs to the 'float' class.
'''
y = 3.14
print("float:", y, "| type:", type(y))

'''
complex: Represents numbers with real and imaginary parts.
Syntax: a + bj, where j is the imaginary unit.
'''
z = 2 + 3j
print("complex:", z, "| type:", type(z))

'''
bool: Represents truth values – either True or False.
Used in logical operations and conditions.
'''
is_valid = True
print("bool:", is_valid, "| type:", type(is_valid))

'''
str: Represents a sequence of characters (text).
Immutable and enclosed in single, double, or triple quotes.
'''
message = "Hello, Python"
print("str:", message, "| type:", type(message))

# -------------------------------
# Sequence Data Types
# -------------------------------

'''
str (String): Ordered sequence of characters.
Supports indexing and slicing.
'''
text = "Python"
print("First char:", text[0])
print("Last char:", text[-1])

'''
list: Ordered, mutable collection of values.
Defined using square brackets [].
'''
nums = [10, 20, 30, 40]
print("List:", nums)
print("First item:", nums[0])
print("Last item:", nums[-1])

'''
tuple: Ordered, immutable collection of values.
Defined using parentheses ().
'''
data = (5, 15, 25)
print("Tuple:", data)
print("Second item:", data[1])

'''
dict: Unordered collection of key-value pairs.
Keys must be unique; values can repeat.
Defined using curly braces {}.
'''
info = {"Name": "Tom", "Age": 50, "Movie": "Mission Impossible"}
print("Dictionary:", info)
print("Access by key:", info["Name"])

'''
set: Unordered collection of unique elements.
Defined using curly braces {}.
Duplicates are automatically removed.
'''
s = {1, 2, 2, 3, 4}
print("Set:", s)

# -------------------------------
# String Operations
# -------------------------------

'''
Strings can be concatenated using the '+' operator.
'''
greeting = "Hello" + "World"
print("Concatenated string:", greeting)

# -------------------------------
# Type Checking
# -------------------------------

'''
Use type() to check the data type of any variable.
'''
print("Type of x:", type(x))
print("Type of y:", type(y))
print("Type of z:", type(z))
print("Type of is_valid:", type(is_valid))
print("Type of message:", type(message))