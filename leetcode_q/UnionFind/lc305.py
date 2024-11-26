class UnionFind:
    """
    Union-Find 数据结构，用于高效地处理和查询节点间的连通性。
    - 初始化时，每个节点指向自身，构成独立的集合。
    - 提供 `find` 方法用于查找节点的根节点，同时应用路径压缩优化。
    - 提供 `union` 方法用于合并两个节点所在的集合。
    """

    def __init__(self, m, n):
        self.parent = [i for i in range(m * n)]
        self.count = 0
        # print(self.parent)

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.count -= 1
            self.parent[root_x] = root_y
        # print(self.parent)


class Solution:
    """
    解决在二维网格上添加陆地并计算岛屿数量的问题。
    - 使用 Union-Find 数据结构来跟踪陆地单元格的连通性。
    - 对于每个添加的陆地，检查其四个方向的邻居是否也是陆地，如果是，则合并它们的集合。
    - 记录每次添加陆地后的岛屿总数。
    """

    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        uf = UnionFind(m, n)
        res = []
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
        added = set()
        for pos_x, pos_y in positions:
            if (pos_x, pos_y) not in added: #[[0,0],[0,1],[1,2],[1,2]]这个例子需要判断
                added.add((pos_x, pos_y))
                uf.count += 1
                for dx, dy in directions:
                    find_x = pos_x + dx
                    find_y = pos_y + dy
                    if 0 <= find_x < m and 0 <= find_y < n and (find_x, find_y) in added:
                        uf.union(pos_x * n + pos_y, find_x * n + find_y)
            res.append(uf.count)
        return res