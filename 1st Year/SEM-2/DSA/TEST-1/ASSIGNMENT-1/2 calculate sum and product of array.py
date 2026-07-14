def sum_and_product(arr):
    total_sum = 0
    total_product = 1
    
    for num in arr:
        total_sum += num
        total_product *= num
    
    return total_sum, total_product
# Example usage
arr = [1, 2, 3, 4]
result = sum_and_product(arr)
print(f"Sum: {result[0]}, Product: {result[1]}")