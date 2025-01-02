from collections import deque


class Solution:
    """
    此解法用于解决被围绕的区域问题，即将所有被 'X' 围绕的 'O' 转换为 'X'，
    而与边界直接或间接相连的 'O' 不会被转换。

    思路：
    1. 从棋盘的边界开始，找到所有的 'O'，并认为这些 'O' 是不会被转换的，因为它们与边界相连。
    2. 使用广度优先搜索（BFS）从这些边界的 'O' 出发，将所有与它们相连的 'O' 标记为 '#',
       表示这些 'O' 是安全的，不会被转换。
    3. 遍历整个棋盘，将所有未被标记为 '#' 的 'O' 转换为 'X'，因为它们被完全围绕。
    4. 将所有标记为 '#' 的位置恢复为 'O'。
    """

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        queue = deque()

        for i in range(m):
            if board[i][0] == 'O':
                queue.append((i, 0))
            if board[i][n - 1] == 'O':
                queue.append((i, n - 1))

        for j in range(n):
            if board[0][j] == 'O':
                queue.append((0, j))
            if board[m - 1][j] == 'O':
                queue.append((m - 1, j))

        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        while queue:
            i, j = queue.popleft()
            board[i][j] = '#'

            for di, dj in directions:
                next_i = di + i
                next_j = dj + j
                if 0 <= next_i < m and 0 <= next_j < n:
                    if board[next_i][next_j] == 'O':
                        board[next_i][next_j] = '#'
                        queue.append((next_i, next_j))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'
