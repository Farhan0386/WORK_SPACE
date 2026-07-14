def check_sorted(arr):
    n = len(arr)
    
    if n <= 1:
        return "Forward"
    
    is_increasing = True
    is_decreasing = True
    
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            is_increasing = False
        if arr[i] < arr[i + 1]:
            is_decreasing = False
    
    if is_increasing:
        return "Forward"
    elif is_decreasing:
        return "Backward"
    else:
        return "Not Sorted"

# Example usage
arr = [1, 2, 3, 4, 5]
result = check_sorted(arr)
print(f"The array is sorted: {result}")