def most_frequent(arr):
    freq = {}
    max_count = 0
    result = None
    
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
        
        if freq[num] > max_count:
            max_count = freq[num]
            result = num
    
    return result
# Example usage
arr = [1, 2, 3, 2, 4, 5, 1]
most_freq = most_frequent(arr)
print(f"The most frequent element is: {most_freq}")