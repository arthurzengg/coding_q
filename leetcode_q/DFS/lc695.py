class Solution:
    """
    此解法用于计算二维网格中的最大岛屿面积。岛屿由四面相连的 1 表示，被水包围，即由 0 表示。
    思路：
    1. 使用深度优先搜索（DFS）遍历每一个可能的岛屿单元。
    2. 对于每个值为 1 的单元，触发 DFS 过程，将所有相邻的 1 转变为 0（标记已访问），同时计算岛屿的面积。
    3. 将每次触发的 DFS 过程得到的岛屿面积存入结果列表，随后从列表中找出最大值返回。
    4. 如果整个网格中没有岛屿（列表为空），则返回面积为 0。

    方法：
    - maxAreaOfIsland(grid): 输入一个二维网格，返回最大岛屿的面积。
    """

    def __init__(self):
        self.area = 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        n = len(grid)
        m = len(grid[0])
        res = []

        def dfs(i, j, grid):
            if i < 0 or i >= n or j < 0 or j >= m:
                return
            if grid[i][j] != 1:
                return
            if grid[i][j] == 1:
                grid[i][j] = 0
                self.area += 1
            dfs(i + 1, j, grid)
            dfs(i - 1, j, grid)
            dfs(i, j + 1, grid)
            dfs(i, j - 1, grid)

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.area = 0
                    dfs(i, j, grid)
                    res.append(self.area)
        if res == []:
            return 0
        return max(res)

