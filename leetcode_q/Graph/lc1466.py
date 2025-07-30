from collections import defaultdict


class Solution:
    """
    思路如下：
    1. 我们将图分为两个部分：
        - 一个是无向图（nondirect_graph）：用于从城市 0 出发遍历所有能到的城市；
        - 一个是有向图（direct_graph）：记录原始边的方向，用于判断当前边是否需要反转。

    2. 我们从节点 0 开始做 BFS 遍历，对于每一个从当前城市 node 可达的相邻城市 v：
        - 如果这条边的原始方向是 node → v（即 node 在 direct_graph[v] 中不包含），那么这条边就是反向的，说明需要翻转，res += 1；
        - 如果不需要翻转，说明 v 原本就能到达 node。

    3. 为了避免重复访问，我们用 visited 数组标记已访问城市，在将城市 v 加入队列时就标记为 True（入队时设置，避免重复入队）。

    4. 最终 res 就是需要翻转的最少边数。
    """

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        res = 0
        nondirect_graph = defaultdict(list)
        direct_graph = defaultdict(list)

        for u, v in connections:
            nondirect_graph[u].append(v)
            direct_graph[u].append(v)
            nondirect_graph[v].append(u)

        visited = [False for _ in range(n)]
        queue = [0]
        visited[0] = True
        while queue:
            node = queue.pop(0)
            for v in nondirect_graph[node]:
                if not visited[v]:
                    if node not in direct_graph[v]:
                        res += 1
                    visited[v] = True
                    queue.append(v)
        return res
