def find_missing(arr):
    n = len(arr)
    
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    
    return expected_sum - actual_sum
# Example usage
arr = [1, 2, 4, 5]
missing_number = find_missing(arr)
print(f"The missing number is: {missing_number}")