def find_leftmost_one(arr):
    if not arr or not arr[0]:
        return -1  # Return -1 if the array is empty or rows are empty

    m, n = len(arr), len(arr[0])
    min_index = n  # Initialize with the maximum possible column index

    for row in arr:
        left, right = 0, n - 1
        index = n  # Default to n if 1 is not found in this row

        # Binary search for the first occurrence of 1 in the row
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == 1:
                index = mid       # Update index and search in the left half
                right = mid - 1
            else:
                left = mid + 1    # Search in the right half

        if index < min_index:
            min_index = index  # Update the global minimum index

    return min_index if min_index < n else -1  # Return -1 if no 1 is found

# Example usage:
arr = [
    [0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1, 1]
]
print(find_leftmost_one(arr))  # Output: 2

arr2 = [[0, 0, 0, 0, 0, 1, 1]]
print(find_leftmost_one(arr2))  # Output: 5