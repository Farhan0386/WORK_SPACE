def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    
    return arr[-k:] + arr[:-k]
# Example usage
arr = [1, 2, 3, 4, 5]
k = 2
rotated_arr = rotate_array(arr, k)
print(f"The array after rotating by {k} positions is: {rotated_arr}")