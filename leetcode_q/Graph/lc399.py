from collections import deque


class Solution:
    """
    # 思路：
    使用图的广度优先搜索（BFS）来解决方程求值问题。此方法通过建立一个图来表示所有的变量和它们之间的关系。
    每个变量对应图中的一个节点，方程则表示为节点间的边，边的权重为方程的结果值。

    方法：
    - 创建图：遍历所有的方程，将变量作为节点加入图中，方程的结果作为边的权重。
    - 解决查询：对每个查询使用BFS来查找从查询的起点到终点的路径，路径上的边权重相乘即为结果。
    """

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for (start, end), value in zip(equations, values):
            if start not in graph:
                graph[start] = {}
            graph[start][end] = value

            if end not in graph:
                graph[end] = {}
            graph[start][start] = 1.0
            graph[end][start] = 1 / value
            graph[end][end] = 1.0

        queue = deque()
        ans = [-1.0] * len(queries)

        for i, (qx, qy) in enumerate(queries):
            if qx not in graph or qy not in graph:
                continue
            queue.append([qx, 1.0])
            visited = set([qx])
            while queue:
                node, mul = queue.popleft()
                for neighbor, weight in graph[node].items():
                    if neighbor == qy:
                        ans[i] = mul * weight
                        break
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append([neighbor, mul * weight])
        return ans
