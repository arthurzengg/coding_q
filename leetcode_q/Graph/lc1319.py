from collections import defaultdict
from typing import List

class Solution:
    """
    # 思路：
    1. 检查边的数量是否足够：因为一个含有n个节点的图，至少需要n-1条边才能构成一个连通图。
    2. 构建图：使用邻接表形式构建图，对于每对连接，相互关联两个节点。
    3. 使用深度优先搜索（DFS）来确定图中的连通分量数量：初始化一个访问集合来跟踪已访问的节点。
    4. 遍历所有节点，对每一个未访问的节点，通过DFS遍历其所有可达的节点，每完成一次DFS代表找到了一个连通分量。
    5. 连通分量的数量减一即是需要的最少操作次数，因为每多一个连通分量，就需要至少一条边来将其与其他部分连接起来。
    """

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        # 如果边的数量少于n-1，则无法将所有节点连接成一个连通图
        if len(connections) < n - 1:
            return -1

        components = 0
        graph = defaultdict(list)
        # 构建图的邻接表
        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])

        visited = set()

        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
            return 1

        # 遍历所有节点，计算连通分量的数量
        for current_node in range(n):
            components += dfs(current_node)

        # 连通分量数减一即为最少需要的操作次数
        return components - 1