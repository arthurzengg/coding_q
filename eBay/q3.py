def find_local_maxima(matrix):
    if not matrix or not matrix[0]:
        return []
    m, n = len(matrix), len(matrix[0])

    result = []

    for i in range(m):
        for j in range(n):
            value = matrix[i][j]
            # Skip zeros right away
            if value == 0:
                continue

            r = value
            row_min = max(0, i - r)
            row_max = min(m - 1, i + r)
            col_min = max(0, j - r)
            col_max = min(n - 1, j + r)

            is_local_max = True  # we'll try to disprove this
            for x in range(row_min, row_max + 1):
                for y in range(col_min, col_max + 1):
                    # Skip the four corners if they're within bounds
                    corner1 = (i - r, j - r)
                    corner2 = (i - r, j + r)
                    corner3 = (i + r, j - r)
                    corner4 = (i + r, j + r)
                    if (x, y) in [corner1, corner2, corner3, corner4]:
                        continue
                    # Don't compare the center with itself
                    if (x == i and y == j):
                        continue
                    # If any neighbor is >= center, not a local max
                    if matrix[x][y] >= value:
                        is_local_max = False
                        break
                if not is_local_max:
                    break

            if is_local_max:
                result.append([i, j])

    # Sort by row, then by column
    result.sort(key=lambda cell: (cell[0], cell[1]))
    return result


# --- Example usage ---
example_matrix = [
    [3, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 2, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 3, 0, 0, 3]
]
print(find_local_maxima(example_matrix))
# Expected: [[0, 0], [2, 2]]
