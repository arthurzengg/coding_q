class Solution:
    """
    步骤
    1. 建图 —— 邻接表 `graph[u] = [(v, w), ...]`
    2. 初始化 —— dist[k] = 0，其余为 +∞，小根堆 heap=[(0, k)]
    3. while 堆非空：
         - 弹出目前距离最小的节点 (d, u)
         - 如果 d > dist[u] 说明是“过期”条目，跳过
         - 遍历 u 的邻边 (v, w)，尝试松弛：
             若 dist[u] + w < dist[v]:
                 更新 dist[v]
                 将 (dist[v], v) 推入堆
    4. 返回 max(dist[1:])；若仍有 +∞ 说明无法全部到达，返回 -1

    复杂度
    ----------
    - 邻接表 + 小根堆：O(E log V)
    - 空间：O(V + E)

    代码里使用 `if d > dist[u]: continue` 的原因
    -------------------------------------------
    同一个节点可能因为发现更短路径而被多次推入堆，旧条目就成了“过期数据”。
    该判断保证每个节点只会用 **最终最短** 的距离去继续松弛邻居，既避免不必要的计算，也防止错误更新。
    """

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. 建图
        graph = [[] for _ in range(n + 1)]
        for u, v, w in times:
            graph[u].append((v, w))

        # 2. 初始化
        dist = [float('inf') for _ in range(n + 1)]
        dist[k] = 0
        queue = [(k, 0)]

        # 3. Dijkstra
        while queue:
            u, d = queue.pop(0)
            if d > dist[u]:  # 过滤过期条目
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    queue.append((v, dist[v]))
            queue.sort()

        if max(dist[1:]) == float('inf'):
            return -1
        else:
            return max(dist[1:])