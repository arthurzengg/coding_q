class Solution:
    """
    思路逻辑：
    本题要求计算二维网格中某个连通岛屿的周长。

    1. 使用 DFS 从任意一个值为 1 的格子出发，递归访问整块岛屿。
    2. 对每个访问到的岛屿格子，统计它四个方向上的相邻格子：
    - 如果相邻格子是水（0），或者越界，则这条边算作一条岛屿边界；
    - 否则不计入周长。
    3. 为了简化判断，你使用了 `find_around` 函数来统计当前格子四个方向上有几个是陆地；
    - 然后通过 `4 - 陆地邻居数` 来更新当前格子的周长。
    4. 使用 `visited` 数组避免重复遍历。

    最终返回所有格子贡献的周长之和。
    """
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        def find_around(i, j):
            count = 0
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for dx, dy in directions:
                nexti = i + dx
                nextj = j + dy
                if 0 <= nexti < m and 0 <= nextj < n:
                    if grid[nexti][nextj] == 1:
                        count += 1
            return count

        def dfs(i, j, visited):
            directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
            nonlocal preimeter
            if visited[i][j] or grid[i][j] == 0:
                return
            island_around = find_around(i, j)
            visited[i][j] = True
            if island_around == 0:
                preimeter += 4
            elif island_around == 1:
                preimeter += 3
            elif island_around == 2:
                preimeter += 2
            elif island_around == 3:
                preimeter += 1
            for dx, dy in directions:
                nexti = i + dx
                nextj = j + dy
                if 0 <= nexti < m and 0 <= nextj < n:
                    dfs(nexti, nextj, visited)

        preimeter = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    dfs(i, j, visited)
        return preimeter