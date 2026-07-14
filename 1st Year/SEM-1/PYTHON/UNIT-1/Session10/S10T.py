# ----------------------------------------
# Logical Operators
# ----------------------------------------
"""
Logical operators are used to perform logical operations on Boolean values.

Operators:
- and     : Returns True if both operands are True
- or      : Returns True if at least one operand is True
- not     : Reverses the Boolean value

Examples:
True and False     => False
True or False      => True
not True           => False
"""

x = True
y = False
print("Logical AND:", x and y)
print("Logical OR:", x or y)
print("Logical NOT:", not x)

# ----------------------------------------
# Identity Operators
# ----------------------------------------
"""
Identity operators compare the memory location of two objects.

Operators:
- is       : Returns True if both variables point to the same object
- is not   : Returns True if they point to different objects

Examples:
x = 5
y = 5
x is y         => True
x is not y     => False

x1 = [1, 2]
y1 = [1, 2]
x1 is y1       => False (different memory locations)
"""

a = 5
b = 5
print("Identity (a is b):", a is b)

# ----------------------------------------
# Membership Operators
# ----------------------------------------
"""
Membership operators test whether a value exists in a sequence (list, string, tuple, dict).

Operators:
- in       : True if value is found in the sequence
- not in   : True if value is not found in the sequence

Examples:
3 in [1, 2, 3]           => True
'H' in "Hello"           => True
'hello' not in "Hello"   => True
1 in {1: 'a', 2: 'b'}     => True (checks keys)
'a' in {1: 'a'}           => False (not a key) beacuse 'a' is a value
"""

numbers = [1, 2, 3, 4, 5]
print("Membership (3 in numbers):", 3 in numbers)

# ----------------------------------------
# Bitwise Operators
# ----------------------------------------
"""
Bitwise operators perform operations on binary representations of integers.

Operators:
- &   : Bitwise AND
- |   : Bitwise OR
- ^   : Bitwise XOR
- ~   : Bitwise NOT
- <<  : Left Shift
- >>  : Right Shift

Examples (x = 10 -> 1010, y = 4 -> 0100):
x & y     => 0
x | y     => 14
x ^ y     => 14
~x        => -11
x << 1    => 20
x >> 1    => 5
"""

x = 10  # 1010
y = 4   # 0100
print("Bitwise AND:", x & y)
print("Bitwise OR:", x | y)
print("Bitwise XOR:", x ^ y)
print("Bitwise NOT (~x):", ~x)
print("Bitwise Left Shift:", x << 1)
print("Bitwise Right Shift:", x >> 1)

# ----------------------------------------
# Bitwise Shift Explanation (simple)
# ----------------------------------------
"""
Left shift (x << n):
- Shifts bits of x to the left by n places.
- For non-negative integers, it's equivalent to x * (2**n).
Example: 3 (0b11) << 2 -> 12 (0b1100)

Right shift (x >> n):
- Shifts bits of x to the right by n places.
- For non-negative integers, it's equivalent to x // (2**n).
For negative integers, Python preserves the sign (arithmetic shift).
Example: 12 (0b1100) >> 2 -> 3 (0b11)
"""

print("\n-- Shift examples --")
a = 3
print("3 in binary:", bin(a))
print("3 << 2 ->", a << 2, "binary:", bin(a << 2))
print("12 >> 2 ->", 12 >> 2, "binary:", bin(12 >> 2))
# negative example (sign-preserving)
n = -13
print("-13 >> 2 ->", n >> 2, " (floor division behavior for negatives)")

# ----------------------------------------
# Combined Operator Program
# ----------------------------------------
"""
This program demonstrates all four types of operators in one place.
"""

# Logical
x = True
y = False
result_logical = x and y

# Identity
a = 5
b = 5
result_identity = a is b

# Membership
numbers = [1, 2, 3, 4, 5]
result_membership = 3 in numbers

# Bitwise
num1 = 10
num2 = 4
result_bitwise = num1 ^ num2

print("\n--- Combined Operator Results ---")
print("Logical:", result_logical)
print("Identity:", result_identity)
print("Membership:", result_membership)
print("Bitwise:", result_bitwise)