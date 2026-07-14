def two_sum(arr, target):
    n = len(arr)
    
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return True
    
    return False
# Example usage
arr = [1, 2, 3, 4, 5]
target = 7
result = two_sum(arr, target)
print(f"Two elements with sum {target} exist: {result}")