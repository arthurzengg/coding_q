class UnionFind:
    def __init__(self, size):
        self.father = [i for i in range(size)]

    def join(self, x, y):
        x_f = self.find(x)
        y_f = self.find(y)
        if x_f == y_f:
            return True
        else:
            self.father[x_f] = y_f

    def find(self, x):
        if self.father[x] == x:
            return x
        else:
            self.father[x] = self.find(self.father[x])
        return self.father[x]


class Solution:
    """
    思路解析：

    题目给定一个图，该图是一个树（n 个节点，n-1 条边），但现在多加了一条边，总共 n 条边，导致出现了环。
    要求找出这条冗余的边，即去掉它后图仍为一棵树。

    思路：
    1. 使用并查集（Union-Find）判断是否出现环：
    - 初始化并查集，每个节点的父节点设为自己。
    - 遍历所有边，对于每条边 (u, v)，尝试将 u 和 v 所属集合合并。
    - 如果 u 和 v 已经在同一个集合中，说明这条边会产生环，即为冗余边，直接返回。

    2. 注意：题目中的节点编号是从 1 到 n，而并查集内部使用的是 0-based 索引，所以需要在调用 join() 前做减一处理：`u - 1, v - 1`

    时间复杂度：O(n α(n))，其中 α(n) 为阿克曼函数的反函数，几乎可看作常数。
    空间复杂度：O(n)
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union = UnionFind(len(edges))
        for u, v in edges:
            if union.join(u - 1, v - 1):
                return [u, v]