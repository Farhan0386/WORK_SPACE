def count_occurrences(arr, target):
    count = 0
    
    for num in arr:
        if num == target:
            count += 1
    
    return count

# Example usage
arr = [1, 2, 3, 4, 2, 5, 2]
target = 2 
occurrences = count_occurrences(arr, target)
print(f"The number {target} occurs {occurrences} times in the array.")