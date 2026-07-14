def sum_of_max_min(arr):
    if not arr:
        return None
    
    minimum = arr[0]
    maximum = arr[0]
    
    for num in arr:
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    
    return minimum + maximum
# Example usage
arr = [3, 1, 4, 1, 5, 9 ]   
result = sum_of_max_min(arr)
print(f"The sum of the maximum and minimum elements is: {result}")