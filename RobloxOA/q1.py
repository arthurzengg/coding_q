def solution(n, m, figures):
    figures_dict = {
        'A': [[1]],
        'B': [[1, 1, 1]],
        'C': [[1, 1], [1, 1]],
        'D': [[1, 0], [1, 1], [1, 0]],
        'E': [[0, 1, 0], [1, 1, 1]],
    }

    grid = [[0] * m for _ in range(n)]

    for index, fig_letter in enumerate(figures):
        figure_index = index + 1  # Since we need to mark the grid with 1-based index
        shape = figures_dict[fig_letter]
        shape_height = len(shape)
        shape_width = len(shape[0])
        placed = False
        for row in range(n - shape_height + 1):
            for col in range(m - shape_width + 1):
                can_place = True
                for i in range(shape_height):
                    for j in range(shape_width):
                        if shape[i][j] == 1:
                            if grid[row + i][col + j] != 0:
                                can_place = False
                                break
                    if not can_place:
                        break
                if can_place:
                    # Place the shape
                    for i in range(shape_height):
                        for j in range(shape_width):
                            if shape[i][j] == 1:
                                grid[row + i][col + j] = figure_index
                    placed = True
                    break
            if placed:
                break
    return grid

n = 3
m = 5
figures =  ['A', 'D', 'E']
print(solution(n, m, figures))

n = 4
m = 4
figures = ['D', 'B', 'A', 'C']
print(solution(n, m, figures))