def find_distinct(arr):
    freq = {}
    
    # Count frequency
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Print distinct elements
    for num in arr:
        if freq[num] == 1:
            print(num, end=" ")
# Example usage
arr = [1, 2, 3, 2, 4, 5, 1]
print("Distinct elements in the array:")
find_distinct(arr)