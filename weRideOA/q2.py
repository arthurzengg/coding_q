def minMoves(maze, x, y):
    from collections import deque

    n = len(maze)
    m = len(maze[0])

    # Collect the positions of all the coins
    coin_positions = []
    coin_indices = {}  # Map from position to index
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 2:
                idx = len(coin_positions)
                coin_positions.append((i, j))
                coin_indices[(i, j)] = idx

    k = len(coin_positions)  # Number of coins

    # Initialize visited states: visited[row][col][collected_coins_bitmask]
    visited = [[[False] * (1 << k) for _ in range(m)] for _ in range(n)]

    # Initialize starting collected_coins bitmask
    start_collected = 0
    if maze[0][0] == 2:
        pos = (0, 0)
        idx = coin_indices[pos]
        start_collected |= (1 << idx)

    # Initialize the BFS queue
    queue = deque()
    queue.append((0, 0, start_collected, 0))  # (row, col, collected_coins, moves)
    visited[0][0][start_collected] = True

    # Possible movements
    directions = [(-1,0),(1,0),(0,-1),(0,1)]  # Up, Down, Left, Right

    while queue:
        row, col, collected, moves = queue.popleft()

        # Check if goal state is reached
        if (row, col) == (x, y) and collected == (1 << k) - 1:
            return moves

        # Explore adjacent cells
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < m:
                cell_value = maze[nr][nc]
                if cell_value != 1:  # Not blocked
                    new_collected = collected
                    if cell_value == 2:
                        idx = coin_indices[(nr, nc)]
                        new_collected |= (1 << idx)
                    if not visited[nr][nc][new_collected]:
                        visited[nr][nc][new_collected] = True
                        queue.append((nr, nc, new_collected, moves + 1))

    # If we reach here, it's impossible
    return -1

print(minMoves([[0,2,1],[1,2,0],[1,0,0]],2,2))
print(minMoves([[0,2,0],[0,0,1],[1,1,1]],1,1))
print(minMoves([[0,1,0],[1,0,1],[0,2,2]],1,1))
print(minMoves([[0,2,0],[1,1,2],[1,0,0]],2,1))