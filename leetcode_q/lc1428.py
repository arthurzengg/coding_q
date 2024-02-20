# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # Get the dimensions of the binary matrix
        rows, cols = binaryMatrix.dimensions()
        # Initialize the minimum column index to infinity, as a placeholder for comparison
        min_col = float('inf')

        # Iterate over each row to perform binary search
        for row in range(rows):
            # Set the initial low and high pointers for the binary search
            low, high = 0, cols - 1
            while low <= high:
                # Calculate the middle index between low and high
                mid = low + (high - low) // 2
                # Use the API to get the value at the current cell
                if binaryMatrix.get(row, mid) == 1:
                    # Update min_col if a new leftmost 1 is found
                    min_col = min(min_col, mid)
                    # Move the high pointer to search the left half
                    high = mid - 1
                else:
                    # Move the low pointer to search the right half
                    low = mid + 1

        # If min_col was updated, return its value; otherwise, return -1 indicating no 1 was found
        return min_col if min_col != float('inf') else -1
