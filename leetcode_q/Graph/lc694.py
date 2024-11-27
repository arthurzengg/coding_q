class Solution:
    """
    此解法用于寻找给定网格中不同形状的岛屿的数量。
    思路：
    1. 遍历整个网格，寻找岛屿的起始点（即值为1的单元格）。
    2. 对每个找到的岛屿起始点，使用深度优先搜索（DFS）遍历整个岛屿，并记录相对于起始点的相对位置。
    3. 使用集合（Set）记录岛屿的形状。通过将相对位置的集合转换成元组后存储在另一个集合中，以保证岛屿形状的唯一性。
    4. 最后，返回记录形状的集合的大小，即不同岛屿的数量。

    方法：
    - dfs(grid, i, j, find_i, find_j, location): 从 (find_i, find_j) 开始，探索整个岛屿，并记录所有点相对于 (i, j) 的位置。
    - numDistinctIslands(grid): 主函数，遍历网格并触发 dfs 来发现并记录所有独特的岛屿形状。
    """

    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        res = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    location = set()
                    self.dfs(grid, i, j, i, j, location)
                    # print(location)
                    res.add(tuple(location))
        return len(res)

    def dfs(self, grid, i, j, find_i, find_j, location):
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        grid[find_i][find_j] = 0
        location.add((find_i - i, find_j - j))
        for dx, dy in directions:
            if 0 <= find_i + dx < len(grid) and 0 <= find_j + dy < len(grid[0]) and grid[find_i + dx][find_j + dy] == 1:
                self.dfs(grid, i, j, find_i + dx, find_j + dy, location)

