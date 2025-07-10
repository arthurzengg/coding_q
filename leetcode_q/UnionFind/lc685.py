from collections import defaultdict


class UnionFind:
    def __init__(self, size):
        # 初始化并查集，节点编号从 1 到 size（注意开 size+1）
        self.father = [i for i in range(size + 1)]

    def union(self, x, y):
        f_x = self.find(x)
        f_y = self.find(y)
        if f_x == f_y:
            return False
        self.father[f_x] = f_y
        return True

    def find(self, x):
        print(x)
        if self.father[x] == x:
            return x
        else:
            self.father[x] = self.find(self.father[x])
        return self.father[x]


class Solution:
    """
    思路解析：

    问题分三种情况：
    1. 图中有一个节点的入度为 2，但无环（需要删掉后加入的边）
    2. 图中有一个节点的入度为 2，且图中还有环（需要删掉先加入的边）
    3. 所有节点入度为 1，但图中有环（删掉成环的最后一条边）

    处理方式：
    - 首先检查是否存在入度为 2 的节点
    - 然后使用 Union-Find 判断删掉某条边后图是否仍为树
    """

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent_map = {}  # 记录每个节点的“父亲”边的索引
        candidate = []  # 存储出现入度为 2 的两个边的索引

        # 第一步：检查是否存在某个节点被两个节点指向（即入度为 2）
        for i, (u, v) in enumerate(edges):
            if v in parent_map:
                # 找到入度为 2 的两个边，先加入的和后加入的
                candidate = [parent_map[v], i]
                break
            parent_map[v] = i

        def is_tree_after_removal(skip_idx):
            uf = UnionFind(n)
            for i, (u, v) in enumerate(edges):
                if i == skip_idx:
                    continue
                if not uf.union(u, v):  # 出现环，不是树
                    return False
            return True

        # 如果存在入度为 2 的节点
        if candidate:
            # 删除后加入的边，看看能否构成树
            if is_tree_after_removal(candidate[1]):
                return edges[candidate[1]]
            else:
                return edges[candidate[0]]

        # 第三种情况：所有节点入度为 1，但图中有环
        uf = UnionFind(n)
        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]  # 返回成环的那条边

        return []
