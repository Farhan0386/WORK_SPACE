def find_duplicate(arr):
    seen = set()
    
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    
# Example usage
arr = [1, 3, 4, 2, 2]   
duplicate_number = find_duplicate(arr)
print(f"The duplicate number is: {duplicate_number}")