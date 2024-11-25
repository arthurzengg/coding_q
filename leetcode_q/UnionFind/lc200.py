class UnionFind:
    """
    Union-Find 数据结构，用于高效地处理和查询节点间的连通性。
    - 初始化时，每个节点指向自身，构成独立的集合。
    - 提供 `find` 方法用于查找节点的根节点，同时应用路径压缩优化。
    - 提供 `union` 方法用于合并两个节点所在的集合，应用按秩合并优化。
    """

    def __init__(self, grid):
        self.parent = [i for i in range(len(grid) * len(grid[0]))]
        self.count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.count += 1

    def find(self, x):
        if x == self.parent[x]:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_y] = root_x
            self.count -= 1


class Solution:
    """
    # 思路：
    1. 初始化并查集：对每个为'1'的位置初始化，并查集中的父节点和秩。
    2. 遍历网格：对每个为'1'的单元格，将其与四周的'1'进行连接。
    3. 应用并查集的 `union` 操作：对每个为'1'的单元格的四周单元格，如果也是'1'，则合并。
    4. 合并过程中，连通分量的总数会根据需要减少。
    5. 最终并查集中的连通分量总数即为岛屿的数量。
    """

    def numIslands(self, grid: List[List[str]]) -> int:
        uf = UnionFind(grid)
        direction = ((0, 1), (0, -1), (1, 0), (-1, 0))
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    for dx, dy in direction:
                        find_i = dx + i
                        find_j = dy + j
                        if 0 <= find_i < len(grid) and 0 <= find_j < len(grid[0]) and grid[find_i][find_j] == '1':
                            uf.union(i * len(grid[0]) + j, find_i * len(grid[0]) + find_j)
        return uf.count