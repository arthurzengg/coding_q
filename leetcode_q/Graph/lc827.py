from collections import defaultdict


class Solution:
    """
    思路逻辑：
    本题要求在一个仅包含 0 和 1 的二维网格中，最多可以翻转一个 0 为 1，使得最终岛屿的面积最大。岛屿定义为上下左右连接的连续 1 的区域。

    解决步骤如下：

    1. 使用 DFS 遍历整张地图，将每个独立的岛屿用不同的 `mark` 编号标记，并记录每个岛屿的面积到 `island_map` 中。DFS 的过程中将原本为 1 的格子变成其对应的岛屿编号 mark，以便后续识别和访问。
    - 使用 visited 数组避免重复遍历。
    - 从 mark=2 开始编号，防止与原始的 0/1 冲突。

    2. 枚举每一个为 0 的格子，考虑将其翻转成 1 的情况。
    - 观察它上下左右 4 个方向的格子，收集相邻的岛屿编号（避免重复加入同一个岛屿，使用 `visited_island` 去重）。
    - 将当前格子与相邻岛屿的面积相加，得到翻转这个 0 所能构成的最大岛面积。
    - 用 max_area 记录历史最大值。

    3. 特殊情况处理：
    - 如果整个 grid 全是 1，没有 0，DFS 遍历后没有任何翻转机会，此时最大岛面积就是 `island_map` 中的最大值。

    时间复杂度为 O(n²)，空间复杂度为 O(n²)，其中 n 是网格的边长。
    """

    def largestIsland(self, grid: List[List[int]]) -> int:
        island_map = defaultdict(int)
        mark = 2
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]

        def dfs(i, j, grid, island_map, visited, mark):
            nonlocal count
            if visited[i][j] or grid[i][j] == 0:
                return
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
            visited[i][j] = True
            grid[i][j] = mark
            count += 1
            for dx, dy in directions:
                nexti = i + dx
                nextj = j + dy
                if 0 <= nexti < m and 0 <= nextj < n:
                    dfs(nexti, nextj, grid, island_map, visited, mark)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = 0
                    dfs(i, j, grid, island_map, visited, mark)
                    island_map[mark] = count
                    mark += 1

        max_area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    area = 1
                    directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
                    visited_island = set()
                    for dx, dy in directions:
                        nexti = i + dx
                        nextj = j + dy
                        if 0 <= nexti < m and 0 <= nextj < n and grid[nexti][nextj] not in visited_island:
                            if grid[nexti][nextj] != 0:
                                area += island_map[grid[nexti][nextj]]
                                visited_island.add(grid[nexti][nextj])
                    max_area = max(max_area, area)
        for key, value in island_map.items():
            max_area = max(max_area, value)
        return max_area