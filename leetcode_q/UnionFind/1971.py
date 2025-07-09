from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        self.father = [i for i in range(n)]

    def join(self, x, y):
        fx = self.find(x)
        fy = self.find(y)
        if fx != fy:
            self.father[fx] = fy

    def same(self, x, y):
        fatherx = self.find(x)
        fathery = self.find(y)
        if fatherx == fathery:
            return True
        return False


    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]


class Solution:
    """
    中文思路解析：

    题目要求判断在一个无向图中，是否存在从 source 到 destination 的路径。

    本题可以使用并查集（Union-Find）来解决：
    1. 并查集是一种用于处理集合合并与查找的高效数据结构，适合用来判断图中节点是否属于同一连通分量。
    2. 首先初始化一个并查集结构，每个节点初始时都是独立的集合。
    3. 遍历 edges 数组，对每一条边 (u, v)，调用 union.join(u, v)，将 u 和 v 所在的集合合并。
    4. 合并完成后，判断 source 和 destination 是否属于同一个集合（即判断 union.same(source, destination)）。
    - 如果在同一个集合中，说明它们是连通的，返回 True；
    - 否则返回 False。

    时间复杂度：
    - 初始化并查集：O(n)
    - 每条边 union 操作近似 O(1)，总共 O(E)
    - 查询是否连通同样近似 O(1)

    适用于节点较多、查询多次的连通性问题。
    """
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        union = UnionFind(n)
        for u, v in edges:
            union.join(u, v)

        if union.same(source, destination):
            return True
        else:
            return False