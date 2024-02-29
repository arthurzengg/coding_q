def search_word(grid, word):
    grid_size = len(grid)
    word_length = len(word)
    word_positions = []

    # Function to check if the word can be found in a specific direction
    def check_word_in_direction(start_i, start_j, delta_i, delta_j):
        end_i = start_i + (word_length - 1) * delta_i
        end_j = start_j + (word_length - 1) * delta_j

        # Check if the end position is within the grid boundaries
        if 0 <= end_i < grid_size and 0 <= end_j < grid_size:
            for k in range(word_length):
                # Check if each character of the word matches the corresponding grid cell
                if grid[start_i + k * delta_i][start_j + k * delta_j] != word[k]:
                    return False
            return True
        return False

    # Function to find occurrences of the word in a specific direction and record their positions
    def find_word_in_direction(start_i, start_j, delta_i, delta_j):
        if check_word_in_direction(start_i, start_j, delta_i, delta_j):
            word_positions.append([(start_i + k * delta_i, start_j + k * delta_j) for k in range(word_length)])

    # Check rows
    for i in range(grid_size):
        for j in range(grid_size - word_length + 1):
            find_word_in_direction(i, j, 0, 1)

    # Check columns
    for j in range(grid_size):
        for i in range(grid_size - word_length + 1):
            find_word_in_direction(i, j, 1, 0)

    # Check diagonals
    for i in range(grid_size - word_length + 1):
        for j in range(grid_size - word_length + 1):
            # Check diagonals from top-left to bottom-right
            find_word_in_direction(i, j, 1, 1)
            # Check diagonals from top-right to bottom-left
            find_word_in_direction(i, grid_size - 1, 1, -1)

    # Print occurrences of the word
    for positions in word_positions:
        print('-'.join(f'({x},{y})' for x, y in positions))

# Example usage:
grid = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'J'],
    ['K', 'L', 'M', 'N', 'O'],
    ['P', 'Q', 'R', 'S', 'T'],
    ['U', 'V', 'W', 'X', 'Y']
]

word_to_find = "ABC"
search_word(grid, word_to_find)
