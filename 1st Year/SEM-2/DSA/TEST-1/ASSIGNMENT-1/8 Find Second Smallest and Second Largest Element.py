def second_elements(arr):
    arr = sorted(set(arr))  # remove duplicates
    if len(arr) < 2:
        return None
    return arr[1], arr[-2]

# Example usage
arr = [3, 1, 4, 1, 5, 9 ]
result = second_elements(arr)   
print(f"The second smallest and second largest elements are: {result}")