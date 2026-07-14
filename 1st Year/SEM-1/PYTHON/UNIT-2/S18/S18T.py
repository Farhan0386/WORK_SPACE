# ============================================
# Algorithmic Idioms – Sliding Window, Recursion vs Iteration
# Session 18 Summary – Ms. Jyoti Yadav (KRMU)
# ============================================

# -------------------------------
# Sliding Window Technique
# -------------------------------
# Definition:
# A method used to solve problems involving subarrays, substrings, or windows.
# Idea: Use results of previous window to compute the next efficiently.
# Applications: subarray sums, longest substring with unique chars, compression, image processing, networking.

# -------------------------------
# Fixed Size Sliding Window
# -------------------------------
# Steps:
# 1. Find window size K
# 2. Compute result for first window
# 3. Slide window by 1 each time, update result

# Example: Maximum sum of subarray of size k
def maxSum(arr, k):
    n = len(arr)
    if n <= k:
        print("Invalid")
        return -1

    # Initial window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide window
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
    return max_sum

# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
print(maxSum(arr, k))  # Output: 24


# -------------------------------
# Variable Size Sliding Window
# -------------------------------
# Steps:
# 1. Increase right pointer until condition fails
# 2. Shrink window by moving left pointer
# 3. Resume expanding when condition satisfies
# 4. Continue until end of array

# -------------------------------
# Applications of Sliding Window
# -------------------------------
# - Array/String manipulation
# - Data compression (LZ77)
# - Image processing (feature extraction, segmentation)
# - Signal processing (time-series analysis)
# - Network protocols (flow control, reliable transmission)

# -------------------------------
# Recursion in Python
# -------------------------------
# Definition:
# A recursive function calls itself until a base case is met.

# Example: Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120

# Example: Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))  # Output: 55


# -------------------------------
# Recursion vs Iteration
# -------------------------------
# Recursion: Function calls itself
# Iteration: Loop executes repeatedly

# Factorial using Recursion
def factorialUsingRecursion(n):
    if n == 0:
        return 1
    return n * factorialUsingRecursion(n - 1)

# Factorial using Iteration
def factorialUsingIteration(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

print(factorialUsingRecursion(5))  # Output: 120
print(factorialUsingIteration(5))  # Output: 120


# -------------------------------
# Comparison Table (Recursion vs Iteration)
# -------------------------------
# Property        | Recursion                          | Iteration
# ---------------------------------------------------------------
# Definition      | Function calls itself              | Loop executes repeatedly
# Application     | Tree traversals, DFS               | Preferred for efficiency
# Termination     | Base case                          | Condition fails
# Code Size       | Smaller for recursive problems     | Larger for recursive problems
# Time Complexity | Higher or same                     | Lower or same
# Overhead        | Function call overhead             | No overhead

