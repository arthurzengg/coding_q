class Solution:
    """
    思路解析：
    要从有向图中找出一个最小的节点集合，从这些节点出发可以访问图中所有节点。
    观察发现：所有**入度为 0 的节点**，没有其他节点能到达它们，
    因此它们必须作为起点被选中。

    做法：
    - 使用一个 in_degree 数组记录每个节点的入度；
    - 遍历 edges，将每条边的终点的入度加一；
    - 再次遍历所有节点，找出入度为 0 的节点返回即可。

    时间复杂度：O(E + N)，其中 E 是边数，N 是节点数。
    空间复杂度：O(N)
    """

    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        res = []
        in_degree = [0] * n
        for u, v in edges:
            in_degree[v] += 1
        for i in range(n):
            if in_degree[i] == 0:
                res.append(i)
        return res