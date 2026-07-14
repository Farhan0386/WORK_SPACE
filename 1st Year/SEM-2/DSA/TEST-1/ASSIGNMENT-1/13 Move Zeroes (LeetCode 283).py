def move_zeroes(arr):
    pos = 0  # position for next non-zero
    
    # Move non-zero elements forward
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos] = arr[i]
            pos += 1
    
    # Fill remaining positions with 0
    for i in range(pos, len(arr)):
        arr[i] = 0
    
    return arr

# Example usage
arr = [0, 1, 0, 3, 12]
result = move_zeroes(arr)
print(f"The array after moving zeroes is: {result}")